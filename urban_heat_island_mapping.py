# Urban Heat Island Mapping with ML (Synthetic Data)
# Author: Amos Meremu Dogiye
# GitHub: https://github.com/GTVSOFT
# Note: This script is for use in the Earth Engine Python API (via geemap or ee)

import ee
import geemap

# Initialize Earth Engine
ee.Initialize()

NUM_POINTS = 200
RANDOM_SEED = 42
EXPORT_SCALE = 100

# Define AOI
aoi = ee.Geometry.Rectangle([77.55, 12.85, 77.65, 12.95])  # Bangalore-like region

# Generate synthetic observation points
points = ee.FeatureCollection.randomPoints({
    'region': aoi,
    'points': NUM_POINTS,
    'seed': RANDOM_SEED
}).map(lambda pt: pt.set({
    'temperature': ee.Number(35)
        .add(ee.Number(pt.geometry().coordinates().get(0)).subtract(77.6).abs().multiply(-10))
        .add(ee.Number(pt.geometry().coordinates().get(1)).subtract(12.9).abs().multiply(-10))
        .add(ee.Number.random().multiply(2))
}))

# Synthetic thermal bands
thermal1 = ee.Image.random(RANDOM_SEED).multiply(5).add(30).rename('thermal1')
thermal2 = ee.Image.random(RANDOM_SEED + 1).multiply(5).add(30).rename('thermal2')
predictors = thermal1.addBands(thermal2).clip(aoi)

# Sample thermal values at points
samples = predictors.sampleRegions({
    'collection': points,
    'properties': ['temperature'],
    'scale': EXPORT_SCALE
})

# Train Random Forest regressor
rf = ee.Classifier.smileRandomForest(numberOfTrees=100)    .setOutputMode('REGRESSION')    .train(
        features=samples,
        classProperty='temperature',
        inputProperties=['thermal1', 'thermal2']
    )

# Predict across AOI
predictedTemp = predictors.classify(rf).clip(aoi)

# Visualization
Map = geemap.Map()
Map.centerObject(aoi, 13)
Map.addLayer(points, {'color': 'red'}, 'Temperature Points')
Map.addLayer(predictedTemp, {'min': 28, 'max': 38, 'palette': ['blue', 'yellow', 'red']}, 'Predicted UHI Map')
Map.addLayer(aoi, {}, 'AOI Boundary')
Map

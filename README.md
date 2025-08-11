Urban Heat Island Mapping with ML (Thermal Imagery)

The approach can easily be adapted for real-world datasets (e.g., Landsat 8/9, MODIS, ECOSTRESS), enabling environmental researchers, urban planners, and policymakers to identify, monitor, and mitigate urban heat effects.
✨ Features

    Synthetic Data Generation – Over 100 random spatial points within a user-defined AOI.

    Thermal Simulation – Creates synthetic temperature values and thermal bands.

    Machine Learning Prediction – Uses Random Forest regression to interpolate temperature data.

    Heat Map Visualization – Displays predicted urban heat island zones.

    Adaptable Workflow – Easily switch from synthetic to real thermal satellite imagery.

    Export Capabilities – Results can be saved for further GIS processing.

📂 Dataset

The synthetic dataset used in this project is available in Excel format:
📥 Download synthetic_uhi_points.xlsx

Dataset Columns:

    id – Unique point identifier

    longitude – Point longitude in decimal degrees

    latitude – Point latitude in decimal degrees

    temperature – Simulated surface temperature (°C)

🛠 Requirements
For Google Earth Engine Script

    Google Earth Engine account

    Basic JavaScript knowledge

For Offline Python Dataset Generation (optional)

    Python 3.8+

    Pandas

    NumPy

    openpyxl (for Excel export)

Install Python dependencies:

pip install pandas numpy openpyxl

🚀 Usage
Option 1 – Run in Google Earth Engine

    Sign in to Google Earth Engine Code Editor.

    Copy and paste the provided JavaScript code into the editor.

    Adjust the AOI (Area of Interest) coordinates if needed.

    Run the script to:

        Generate synthetic temperature observation points

        Train the Random Forest model

        Visualize predicted UHI zones

    Optionally export the prediction raster for GIS analysis.

Option 2 – Generate Dataset Offline in Python

    Clone this repository:

git clone https://github.com/GTVSOFT/Urban-Heat-Island-Mapping-with-ML-Thermal-Imagery.git
cd Urban-Heat-Island-Mapping-with-ML-Thermal-Imagery

Run the dataset generation script:

    python generate_uhi_dataset.py

    The dataset will be saved as synthetic_uhi_points.xlsx in the project folder.

📊 Example Outputs

    Synthetic Temperature Points – Red dots representing simulated observations.

    Predicted UHI Map – Gradient map showing temperature variations.

    Difference Map (optional) – Shows spatial differences between modeled and observed values.

🔄 Adapting to Real Data

To use real satellite data:

    Replace the synthetic thermal band generation with actual Landsat 8/9 TIRS or ECOSTRESS thermal bands.

    Update preprocessing steps to include atmospheric correction and cloud masking.

    Adjust model training parameters for the dataset’s spatial and spectral characteristics.

📜 License

This project is released under the MIT License – you are free to use, modify, and distribute it with attribution.
👤 Author: Amos Meremu Dogiye
GitHub: https://github.com/GTVSOFT

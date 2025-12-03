# Mining Safety Incidents Analysis

This project analyzes a dataset of mining safety incidents to identify patterns and risk factors. It includes a comprehensive data preprocessing and visualization pipeline.

## Project Structure

- `preprocessing_visualization.ipynb`: The main Jupyter Notebook containing the data cleaning, feature engineering, and visualization steps.
- `dataset/safety_incidents.csv`: The raw dataset.
- `analysis.py`: Python script for additional analysis.

## AI Assistance with Windsurf

This project was developed with the assistance of Windsurf, an AI-powered coding assistant.

### Effective Prompts

The following types of prompts were particularly effective:

- **Pipeline Creation**: "Create a comprehensive data preprocessing pipeline for the `safety_incidents.csv` dataset..."
- **Debugging**: "Debug this error: [error message]" helped in resolving issues with feature engineering and data types.
- **Visualization**: "Create a visualization to show the distribution of..."

### Modifications and Manual Interventions

While Windsurf generated much of the code, some manual modifications were necessary:

- **Missing Data Simulation**: The original dataset had no missing values, so we manually added code to simulate missing data in 'worker_age' and 'years_experience' to demonstrate imputation techniques.
- **Path Corrections**: Adjusted file paths to ensure the notebook could correctly locate the dataset.
- **Git Configuration**: Manually handled git commands and remote repository configuration.

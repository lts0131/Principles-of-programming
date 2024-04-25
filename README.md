# Principles of programming

## Task 1: ANALYSIS and DESIGN

### 1. Data Cleaning
- Loaded data on Colab and performed analysis to obtain clean data.

### 2. Data Visualizations
- **Figure 1:** Two-by-two relationship analysis of all variables to identify correlations.
- **Figure 2:** Heat map for correlation analysis to determine relevant parameters.
- **Figure 3:** Bivariate distribution between `salary_in_usd` and `experience_level`.

### 3. Prediction Model Selection
- Identified the problem as a regression problem through exploratory data analysis (EDA).
- Chose the XGBoost model due to the medium-sized dataset, large number of features, and requirement for high precision in predictions.

### 4. UML Diagram
- Used two classes: one for data handling and one for tools.
- Data Processing Class:
  - Constants: `df` for DataFarm, `model` for the model, and `model_fit` for the trained model.
  - Methods: `doClean` (data cleaning), `build_chart` (create data graphs), `train_data` (train the model), and `forecasts` (prediction).
- Tools Class:
  - One method for converting images to base64.

## Task 2: IMPLEMENTATION

### 1. User-Friendly Interface
- Developed a Flask web project for a user-friendly interface.

### 2. Training Predictive Model
- Loaded data into the model, performed modeling, and evaluated the model's credibility.

### 3. Testing and Evaluation
- Combined prediction and model training as depicted in the diagram.

### 4. System Implementation
- Entered parameters to predict `salary` values.

### 5. Improvement Suggestions
- Automate address prediction based on user's IP.
- Increase sample size for improved prediction accuracy.
- Enhance input interface aesthetics.
- Add input data accuracy checks.

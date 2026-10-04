# 🏠 Gurgaon Real Estate Price Prediction & Recommendation

An end-to-end **Machine Learning and Analytics web application** that predicts property prices, visualises real-estate market trends, and recommends similar apartments across **100+ sectors of Gurgaon (Gurugram), India**.

The project covers the complete Machine Learning workflow from **data preprocessing and feature engineering to model comparison, hyperparameter tuning, model serialization, and Streamlit deployment**.

---

## 📸 Application Preview

### 🏠 Home / Dashboard

![Dashboard Preview](https://github.com/cpravin2110/Real-estate-capstone/blob/5fce48f0249fdff26c6f168d3ad17e36e078ca48/Img/Screenshot%202026-10-04%20190904.png)

### 💰 Price Prediction

![Price Prediction - Input](https://github.com/cpravin2110/Real-estate-capstone/blob/5fce48f0249fdff26c6f168d3ad17e36e078ca48/Img/Screenshot%202026-10-04%20190652.png)

![Price Prediction - Output](https://github.com/cpravin2110/Real-estate-capstone/blob/5fce48f0249fdff26c6f168d3ad17e36e078ca48/Img/Screenshot%202026-10-04%20190726.png)

### 📊 Analytics Dashboard

![Analytics Dashboard](https://github.com/cpravin2110/Real-estate-capstone/blob/5fce48f0249fdff26c6f168d3ad17e36e078ca48/Img/Screenshot%202026-10-04%20190751.png)

### 🏢 Apartment Recommendation

![Apartment Recommendation](https://github.com/cpravin2110/Real-estate-capstone/blob/5fce48f0249fdff26c6f168d3ad17e36e078ca48/Img/Screenshot%202026-10-04%20190802.png)


---

## 🚀 Live Demo & Repository

### 🌐 Live Application

👉 **[Open Live Demo](https://real-estate-capstone-pravinchavan.streamlit.app/)**

### 💻 GitHub Repository

👉 **[View Source Code](https://github.com/cpravin2110/Real-estate-capstone)**

---

## 🏷️ Technologies

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.1-F7931E?logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Tuned-189AB4)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployment-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)

---

## 📌 Project Overview

The **Gurgaon Real Estate Price Prediction & Recommendation** project is an end-to-end Machine Learning application designed to analyze real-estate properties across **100+ sectors of Gurgaon**.

The application provides three major functionalities:

1. 💰 **Property Price Prediction**
2. 📊 **Real-Estate Analytics Dashboard**
3. 🏢 **Similar Apartment Recommendation**

The Machine Learning pipeline includes:

**Data Cleaning → Feature Engineering → Feature Selection → Encoding → Scaling → Model Comparison → Hyperparameter Tuning → Final Model → Deployment**

---

## 📌 Highlights

- Built a complete end-to-end **Machine Learning workflow** from data preprocessing to deployment.
- Worked with approximately **3,500 cleaned property listings** across **104 Gurgaon sectors**.
- Benchmarked **11 regression algorithms**.
- Used **10-fold cross-validation** for model evaluation.
- Compared **R² and MAE** across multiple Machine Learning models.
- Experimented with:
  - Ordinal Encoding
  - One-Hot Encoding
  - Target Encoding
  - StandardScaler
  - PCA
- Applied **log transformation (`log1p`)** to the target price to handle price skewness.
- Compared different preprocessing strategies to determine their effect on model performance.
- Performed **GridSearchCV hyperparameter tuning** for Random Forest and XGBoost.
- XGBoost tuning covered **192 parameter combinations × 10 folds = 1,920 fits**.
- Best tuned XGBoost achieved a **cross-validation R² of 0.905688**.
- Final tuned XGBoost achieved a **hold-out test MAE of approximately 0.1084 crore**.
- Built a reusable **scikit-learn Pipeline** containing preprocessing and the trained XGBoost model.
- Serialized the final pipeline using **Pickle**.
- Deployed the application using **Streamlit Community Cloud**.
- Added an interactive real-estate analytics dashboard.
- Added a content-based apartment recommendation system using cosine similarity.

---

# 🖥️ App Features

| Page | Description |
|---|---|
| **💰 Price Predictor** | Predict property price using property type, sector, BHK, bathrooms, balconies, age/possession, built-up area, furnishing, servant room, store room, luxury category and floor category. |
| **📊 Analytics** | Explore sector-wise price trends, price-per-sqft, property distributions, BHK analysis, area vs price relationships and other market insights. |
| **🏢 Recommend Apartment** | Find properties within a selected radius and recommend the 5 most similar apartments using precomputed cosine-similarity matrices. |

---

# 📍 Dataset

The dataset contains approximately **3,500 cleaned property listings** covering **104 sectors of Gurgaon (Gurugram)**.

### Target Variable

```text
price
```

The target represents the property price in **₹ crore**.

### Features Used

| Feature | Description |
|---|---|
| `property_type` | Flat or independent house |
| `sector` | Gurgaon sector / location |
| `bedRoom` | Number of bedrooms |
| `bathroom` | Number of bathrooms |
| `balcony` | Number/type of balconies |
| `built_up_area` | Built-up area in sq ft |
| `agePossession` | Property age / possession category |
| `furnishing_type` | Unfurnished / Semi-furnished / Furnished |
| `servant room` | Servant room availability |
| `store room` | Store room availability |
| `luxury_category` | Luxury category derived from amenities |
| `floor_category` | Low / Mid / High floor category |

---

# 🧠 Machine Learning Workflow

The project follows a complete Machine Learning pipeline:

```text
                    ┌─────────────────────┐
                    │    Raw Property     │
                    │        Data         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Cleaning &   │
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Feature Selection  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Target Transformation│
                    │    log1p(price)     │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │      Preprocessing Experiments │
              │                                 │
              │ Ordinal / One-Hot / Target     │
              │ Encoding + StandardScaler      │
              │ PCA                            │
              └───────────────┬─────────────────┘
                              │
                              ▼
                  ┌─────────────────────────┐
                  │ 11 Regression Models    │
                  │ + 10-Fold CV            │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Model Comparison         │
                  │ R² + MAE                │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Hyperparameter Tuning   │
                  │      GridSearchCV       │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   Tuned XGBoost Model   │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │   Pickle Serialization  │
                  │      pipeline2.pkl      │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │ Streamlit Web Application│
                  └─────────────────────────┘
```

---

# ⚙️ Machine Learning Process

## 1. Data Cleaning

The raw real-estate data was cleaned before training the Machine Learning models.

Major preprocessing steps included:

- Handling missing values
- Correcting data types
- Removing irrelevant columns
- Handling inconsistent values
- Feature engineering
- Feature selection
- Preparing categorical and numerical features

---

## 2. Target Transformation

Property prices are highly skewed.

Therefore, the target variable was transformed using:

```python
y_transformed = np.log1p(y)
```

After prediction, the values were converted back to the original price scale using:

```python
np.expm1(y_pred)
```

This helps the model work with a more stable target distribution.

---

## 3. Feature Scaling

Numerical features were standardized using:

```python
StandardScaler()
```

The numerical features include:

```text
bedRoom
bathroom
built_up_area
servant room
store room
```

Scaling helps models such as Linear Regression, Ridge, SVR and other algorithms work effectively when features have different ranges.

---

# 🔤 Categorical Encoding Experiments

Different categorical encoding techniques were tested to understand their effect on model performance.

## 1. Ordinal Encoding

Used for categorical variables where categories can be represented numerically.

```python
OrdinalEncoder()
```

---

## 2. One-Hot Encoding

One-Hot Encoding was tested for categorical variables.

```python
OneHotEncoder(drop='first')
```

This was especially useful for models where independent categorical representations are beneficial.

---

## 3. Target Encoding

Target Encoding was tested for the high-cardinality `sector` feature.

```python
TargetEncoder()
```

This converts each category into a value based on the target variable and can reduce the dimensionality problem associated with high-cardinality categorical variables.

---

## 4. PCA

Principal Component Analysis was also tested.

```python
PCA(n_components=0.95)
```

The PCA configuration retained **95% of the variance**.

However, the PCA experiment produced lower performance compared with the later target-encoding approach, so PCA was not used in the final model.

---

# 🤖 Models Compared

A total of **11 regression algorithms** were evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Support Vector Regression
5. Decision Tree
6. Random Forest
7. Extra Trees
8. Gradient Boosting
9. AdaBoost
10. MLP Regressor
11. XGBoost

---

# 📏 Model Evaluation

Two main evaluation metrics were used.

## R² Score

R² measures how much of the variation in the target variable is explained by the model.

Higher R² is better.

```text
Higher R² → Better explanatory performance
```

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted values.

Lower MAE is better.

```text
Lower MAE → Lower prediction error
```

In this project, MAE was calculated after converting the log-transformed predictions back to the original **₹ crore scale**.

---

# 🔄 Cross-Validation Strategy

For model comparison, **10-fold K-Fold Cross-Validation** was used.

```python
KFold(
    n_splits=10,
    shuffle=True,
    random_state=42
)
```

R² was used as the cross-validation scoring metric.

A separate **80/20 train-test split** was used for hold-out evaluation and MAE calculation.

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

# 📊 Results

## PCA Experiment — 95% Variance Retained

| Model | R² | MAE |
|---|---:|---:|
| **Extra Trees** | **0.842277** | **0.597515** |
| Random Forest | 0.823143 | 0.632654 |
| SVR | 0.824158 | 0.664211 |
| XGBoost | 0.828562 | 0.665898 |
| Gradient Boosting | 0.820660 | 0.683959 |
| MLP | 0.824408 | 0.692488 |
| Decision Tree | 0.635964 | 0.880226 |
| AdaBoost | 0.688970 | 0.908792 |
| Ridge | 0.763858 | 0.909826 |
| Linear Regression | 0.763819 | 0.909848 |
| Lasso | -0.003598 | 1.576392 |

### PCA Experiment Takeaway

The PCA-based approach did not provide the best performance.

The best model in this experiment was **Extra Trees with R² = 0.842277 and MAE = 0.597515**.

Because PCA reduced the feature representation and did not improve the results, it was not selected for the final deployment pipeline.

---

# 🎯 Target Encoding Experiment

After experimenting with different preprocessing approaches, Target Encoding was tested for the high-cardinality `sector` feature.

| Model | R² | MAE |
|---|---:|---:|
| **XGBoost** | **0.898501** | 0.483447 |
| Extra Trees | 0.893811 | 0.473364 |
| Random Forest | 0.893625 | **0.466807** |
| Gradient Boosting | 0.883640 | 0.524772 |
| SVR | 0.863266 | 0.583070 |
| MLP | 0.852904 | 0.598311 |
| Linear Regression | 0.828997 | 0.714540 |
| Ridge | 0.829011 | 0.715103 |
| Decision Tree | 0.802443 | 0.582683 |
| AdaBoost | 0.816529 | 0.683549 |
| Lasso | -0.003598 | 1.576392 |

### Observation

- **XGBoost achieved the highest R² = 0.898501**
- **Random Forest achieved the lowest MAE = 0.466807**
- XGBoost and Random Forest were therefore shortlisted for further hyperparameter tuning.

---

# 🔧 Hyperparameter Tuning

Hyperparameter tuning was performed using **GridSearchCV with 10-fold cross-validation**.

Two models were tuned:

- Random Forest
- XGBoost

---

## 🌲 Random Forest Tuning

The Random Forest search explored:

```text
n_estimators
max_depth
max_features
max_samples
```

Total combinations:

```text
128 combinations
×
10 folds
=
1,280 fits
```

Best parameters:

```python
{
    'n_estimators': 200,
    'max_depth': 30,
    'max_features': 'sqrt',
    'max_samples': 1.0
}
```

Best cross-validation R²:

```text
0.890985
```

Hold-out test MAE:

```text
0.18622825573352284
```

---

# 🚀 XGBoost Hyperparameter Tuning

XGBoost was tuned using the following search space:

```text
n_estimators:
[100, 200, 300, 500]

max_depth:
[3, 5, 7, 10]

learning_rate:
[0.01, 0.05, 0.1]

subsample:
[0.8, 1.0]

colsample_bytree:
[0.8, 1.0]
```

Total combinations:

```text
4 × 4 × 3 × 2 × 2
=
192 combinations
```

With 10-fold cross-validation:

```text
192 × 10
=
1,920 fits
```

---

# 🏆 Best XGBoost Configuration

```python
XGBRegressor(
    n_estimators=500,
    max_depth=7,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
```

### Best Cross-Validation Performance

```text
R² = 0.9056879367
```

Approximately:

```text
R² = 0.905688
```

### Hold-Out Test Performance

```text
MAE = 0.10839851482591882 crore
```

Approximately:

```text
MAE ≈ 0.1084 crore
```

Since:

```text
1 crore = ₹100 lakh
```

the MAE is approximately:

```text
₹10.84 lakh
```

---

# 📈 Performance Progression

| Stage | Model | R² | MAE |
|---|---|---:|---:|
| PCA Experiment | Extra Trees | 0.842277 | 0.597515 |
| Target Encoding Experiment | XGBoost | 0.898501 | 0.483447 |
| Hyperparameter Tuning | Random Forest | 0.890985 | **0.186228** |
| **Final Tuned Model** | **XGBoost** | **0.905688** | **0.108399** |

> **Note:** The R² values shown for the tuned models are their **10-fold cross-validation scores**, while the MAE values shown for the tuned Random Forest and XGBoost are **hold-out test-set MAE values** calculated on the original price scale.

---

# 🥇 Why XGBoost Was Selected

XGBoost was selected as the final model because it provided the strongest overall performance in the final evaluation.

### Final XGBoost results:

- **Cross-validation R²:** 0.905688
- **Hold-out Test MAE:** 0.108399 crore
- **Approximately:** ₹10.84 lakh average absolute error

The tuned XGBoost model also improved over the earlier XGBoost experiment:

```text
Before tuning:
R² = 0.898501

After tuning:
R² = 0.905688
```

This demonstrates the improvement obtained through hyperparameter optimization.

---

# 🔄 Final Machine Learning Pipeline

The final application uses a serialized Machine Learning pipeline.

```text
                    User Input
                        │
                        ▼
             ┌─────────────────────┐
             │ Input DataFrame     │
             │ 12 Property Features│
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Preprocessing     │
             └──────────┬──────────┘
                        │
          ┌─────────────┼──────────────┐
          │             │              │
          ▼             ▼              ▼
   StandardScaler   OrdinalEncoder   OneHotEncoder
          │             │              │
          │             │              │
          └─────────────┼──────────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Tuned XGBoost       │
             │ Regressor           │
             └──────────┬──────────┘
                        │
                        ▼
                Log-scale Output
                        │
                        ▼
                  np.expm1()
                        │
                        ▼
              Predicted Price
                ₹ Crore
```

---

# 🔧 Deployed Pipeline

The deployed application uses:

```text
pipeline2.pkl
```

The pipeline combines preprocessing and the trained XGBoost model.

### Input Features

```text
property_type
sector
bedRoom
bathroom
balcony
agePossession
built_up_area
servant room
store room
furnishing_type
luxury_category
floor_category
```

### Preprocessing

```text
Numerical Features
        │
        ▼
  StandardScaler
        │
        ▼
Categorical Features
        │
        ├── OrdinalEncoder
        │
        └── OneHotEncoder
                │
                ▼
          XGBoost Model
                │
                ▼
       log-scale prediction
                │
                ▼
            np.expm1()
                │
                ▼
        Price in ₹ Crore
```

Keeping preprocessing and the Machine Learning model inside a single pipeline ensures that the same transformations are applied during prediction.

---

# 💰 Price Prediction Output

The application accepts property details and sends them through the trained pipeline.

The model generates a predicted price on the log-transformed scale, which is converted back using:

```python
np.expm1(prediction)
```

The application then displays the estimated property price in **₹ crore**.

---

# 🏢 Recommendation Engine

The application also contains a content-based apartment recommendation system.

### Similarity Recommendation

Three precomputed cosine-similarity matrices are used to identify similar properties.

The similarity matrices are combined using weighted scores:

```text
0.5
0.8
1.0
```

The system then ranks properties and returns the **5 most similar apartments**.

### Location-Based Recommendation

A precomputed location-distance matrix is used to find properties within a selected distance/radius from a location.

```text
Selected Location
       │
       ▼
Location Distance Matrix
       │
       ▼
Properties within Radius
       │
       ▼
Recommended Properties
```

---

# 📊 Analytics Dashboard

The Analytics page provides interactive visualizations for exploring the Gurgaon real-estate market.

### Included Analysis

- Sector-wise price-per-square-foot analysis
- Gurgaon sector geomap
- Feature word cloud
- Area vs Price scatter plots
- Flat vs House comparison
- BHK distribution
- BHK price box plots
- Property price distribution
- Property type analysis

The dashboard helps users understand market patterns beyond the Machine Learning prediction.

---

# 🛠️ Tech Stack

| Area | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Encoding | OrdinalEncoder, OneHotEncoder, TargetEncoder |
| Feature Scaling | StandardScaler |
| Dimensionality Reduction | PCA |
| Visualization | Plotly, Matplotlib, Seaborn, WordCloud |
| Web Application | Streamlit |
| Model Serialization | Pickle |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |
| Development | Jupyter Notebook |

---

# 📁 Project Structure

```text
Real-estate-capstone/
│
├── Home.py
│
├── pages/
│   ├── 1_Price Predictor.py
│   ├── 2_Analytics.py
│   └── 3_Recommend Appartment.py
│
├── datasets/
│   ├── cosine_sim1.pkl
│   ├── cosine_sim2.pkl
│   ├── cosine_sim3.pkl
│   ├── data_viz1.csv
│   ├── feature_text.pkl
│   └── location_distance.pkl
│
├── df.pkl
├── pipeline2.pkl
├── latlong_scraper.py
├── requirements.txt
│
└── README.md
```

### File Description

| File / Folder | Purpose |
|---|---|
| `Home.py` | Main Streamlit landing page |
| `1_Price Predictor.py` | Property price prediction |
| `2_Analytics.py` | Interactive analytics dashboard |
| `3_Recommend Appartment.py` | Similar apartment and radius-based recommendation |
| `df.pkl` | Feature dataframe used by the application |
| `pipeline2.pkl` | Trained preprocessing + XGBoost pipeline |
| `datasets/` | Visualization, similarity and location-distance data |
| `latlong_scraper.py` | Sector latitude/longitude processing |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

# ▶️ Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/cpravin2110/Real-estate-capstone.git
```

## 2. Navigate to the Project

```bash
cd Real-estate-capstone
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run Streamlit

```bash
streamlit run Home.py
```

The application will open in the browser.

---

# 📦 Model & Dependency Compatibility

The serialized Machine Learning pipeline was created using the scikit-learn ecosystem.

The project uses:

```text
scikit-learn 1.5.x
```

Therefore, the corresponding version should be maintained in:

```text
requirements.txt
```

This helps avoid compatibility problems while loading the pickled pipeline.

---

# ☁️ Deployment

The application is deployed using:

```text
Streamlit Community Cloud
```

Deployment workflow:

```text
Local Development
       │
       ▼
GitHub Repository
       │
       ▼
Streamlit Community Cloud
       │
       ▼
Live Web Application
```

### Live Application

👉 https://real-estate-capstone-pravinchavan.streamlit.app/

---

# 🚧 Limitations & Future Improvements

Although the application provides useful predictions and analytics, there are several areas that can be improved.

### Current Limitations

- Prices represent listing prices and may differ from final transaction prices.
- The dataset may not represent the complete Gurgaon real-estate market.
- Market prices can change over time.
- The current prediction range is based on a fixed error estimate.

### Future Improvements

- Add dynamic prediction intervals based on property price.
- Add **SHAP-based model explainability**.
- Add more recent real-estate listings.
- Implement model monitoring and drift detection.
- Add proximity features such as:
  - Metro stations
  - Schools
  - Hospitals
  - Shopping centres
  - Major roads
- Add additional location-based features.
- Retrain the model periodically with new market data.

---

# 📌 Key Takeaways

This project demonstrates an end-to-end Machine Learning workflow rather than only training a single model.

### Key technical learnings:

- Data cleaning and feature engineering
- Feature selection
- Target transformation using `log1p`
- Inverse transformation using `expm1`
- Numerical feature scaling
- Ordinal Encoding
- One-Hot Encoding
- Target Encoding
- PCA
- Regression model comparison
- K-Fold Cross-Validation
- GridSearchCV
- Hyperparameter tuning
- XGBoost
- Random Forest
- Model evaluation using R² and MAE
- Scikit-learn Pipelines
- Pickle model serialization
- Streamlit application development
- Git and GitHub
- Cloud deployment

---

# 📊 Final Model Summary

| Metric | Final Result |
|---|---:|
| Dataset | ~3,500 property listings |
| Locations | 104 Gurgaon sectors |
| Algorithms Compared | 11 |
| Cross-Validation | 10-Fold K-Fold |
| XGBoost Search | 192 combinations |
| XGBoost Total Fits | 1,920 |
| Best XGBoost CV R² | **0.905688** |
| Random Forest Test MAE | **0.186228 crore** |
| XGBoost Test MAE | **0.108399 crore** |
| XGBoost Test MAE | **≈ ₹10.84 lakh** |
| Final Model | **Tuned XGBoost** |
| Deployment | **Streamlit Community Cloud** |

---

# 👨‍💻 Author

## Pravin Chavan

**Data Science | Machine Learning | GenAI Enthusiast**

Final-year B.E. Computer Engineering Student

### Connect With Me

🔗 **LinkedIn:**  
https://www.linkedin.com/in/iampravinchavan

💻 **GitHub:**  
https://github.com/cpravin2110

🌐 **Portfolio:**  
https://cpravin2110.github.io/PravinPortfolio/

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ **Star** on GitHub.

Thank you for checking out the project! 🚀

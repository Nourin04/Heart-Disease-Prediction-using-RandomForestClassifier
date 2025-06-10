# Heart-Disease-Prediction-using-RandomForestClassifier

An interactive machine learning web app that predicts the risk of heart disease based on medical inputs. Built using [Streamlit](https://streamlit.io/) and trained on a supervised learning model.
---

## 🚀 Live Demo

👉 [Click here to try the app](https://heart-disease-prediction-rf.streamlit.app/)


---
## 🧠 ML Model Details

- **Algorithm Used**: Random Forest Classifier  
- **Accuracy**: 98% on test set  
- **Metrics Used**: Accuracy, Precision, Recall, F1-Score  

### 🔍 **Feature Explanations**

1. **`age`**
   ➤ Age of the patient in years
   ▸ Example: 45, 60, etc.

2. **`sex`**
   ➤ Gender of the patient
   ▸ 0 = Female, 1 = Male

3. **`chest pain type (cp)`**
   ➤ Type of chest pain experienced
   ▸ 0 = Typical angina
   ▸ 1 = Atypical angina
   ▸ 2 = Non-anginal pain
   ▸ 3 = Asymptomatic

4. **`resting blood pressure (trestbps)`**
   ➤ Patient’s resting blood pressure (in mm Hg) on admission
   ▸ Example: 120, 140, etc.

5. **`serum cholestoral (chol)`**
   ➤ Serum cholesterol level in mg/dl
   ▸ Example: 200, 240, etc.

6. **`fasting blood sugar > 120 mg/dl (fbs)`**
   ➤ 1 = True, 0 = False
   ▸ Whether fasting blood sugar is greater than 120 mg/dl

7. **`resting electrocardiographic results (restecg)`**
   ➤ Results from resting ECG test
   ▸ 0 = Normal
   ▸ 1 = ST-T wave abnormality (T wave inversion, ST elevation/depression)
   ▸ 2 = Probable or definite left ventricular hypertrophy

8. **`maximum heart rate achieved (thalach)`**
   ➤ Max heart rate achieved during exercise test
   ▸ Example: 150, 170, etc.

9. **`exercise induced angina (exang)`**
   ➤ Pain during exercise
   ▸ 1 = Yes, 0 = No

10. **`oldpeak`**
    ➤ ST depression induced by exercise relative to rest (a measure of abnormality in ECG)
    ▸ Example: 1.2, 0.8, etc.

11. **`slope`**
    ➤ Slope of the peak exercise ST segment
    ▸ 0 = Upsloping
    ▸ 1 = Flat
    ▸ 2 = Downsloping

12. **`ca`**
    ➤ Number of major vessels (0–3) colored by fluoroscopy (dye injection to visualize blood flow)
    ▸ Example: 0, 1, 2, 3

13. **`thal`**
    ➤ Type of defect found
    ▸ 0 = Normal
    ▸ 1 = Fixed defect (no blood flow in some part of the heart)
    ▸ 2 = Reversible defect (temporary blood flow issue)

14. **`target`** (this might be in your dataset depending on the version)
    ➤ Indicates the presence of heart disease
    ▸ 0 = No disease
    ▸ 1 = Disease present
---

## 🛠️ Tech Stack

| Tech           | Use                         |
|----------------|-----------------------------|
| `Python`       | Core logic and ML model     |
| `scikit-learn` | Training ML models          |
| `Streamlit`    | Frontend UI                 |
| `joblib`       | Save/load model             |
| `pandas`       | Data handling               |
| `numpy`        | Array manipulation          |

---

## 📌 Features

- User-friendly UI to input medical attributes
- Predicts heart disease risk instantly
- Based on Random Forest Classifier
- Model trained on real-world heart disease dataset
- Gives clear feedback with medical-friendly warnings

---




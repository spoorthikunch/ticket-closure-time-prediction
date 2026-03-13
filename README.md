# 🎫 Ticket Closure Time Prediction

Regression model to predict IT service ticket resolution time.
Random Forest achieved **Test R² 0.81** and **5-fold CV R² 0.78**,
outperforming XGBoost and ANN baselines.

## 📊 Results

| Model | Train R² | Test R² | CV R² (5-fold) |
|---|---|---|---|
| Random Forest ✅ | 0.96 | 0.81 | 0.78 |
| XGBoost | 0.94 | 0.79 | 0.75 |
| ANN | 0.71 | 0.57 | — |
| Linear Regression | 0.61 | 0.58 | — |

## 🎯 Key Engineering Decision

**Data leakage prevention** — Identified and removed 16 
post-creation features that would not be available at 
prediction time (e.g. resolution notes, closing codes).

Without this step the model would appear highly accurate 
in training but fail completely in production. This reflects 
a critical real-world ML engineering discipline.

## 🔍 Features Used
- Category and Subcategory
- Priority, Impact and Urgency
- Reassignment Count
- Time-based features (hour, day, month)

## 🛠 Tech Stack
Python • Scikit-learn • XGBoost • TensorFlow • Pandas • Streamlit • Joblib

## 🔄 Project Workflow
- Data preprocessing — missing values, encoding, scaling
- Feature engineering — time-based feature extraction
- Data leakage analysis — removed 16 post-creation columns
- Model benchmarking — Linear Regression, Random Forest, XGBoost, ANN
- Cross validation — 5-fold CV for generalization check
- Final model serialised with joblib and deployed via Streamlit

## 🚀 Run Locally
\```bash
git clone https://github.com/spoorthikunch/ticket-closure-time-prediction.git
cd ticket-closure-time-prediction
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
\```

## 📁 Repository Structure
- `Ticket_Closure_Time_Prediction.ipynb` — Complete modeling workflow
- `app.py` — Streamlit deployment
- `requirements.txt` — Dependencies

> Note: Trained model file not included due to size.
> Regenerate by running the notebook.

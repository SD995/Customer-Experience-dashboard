
📊 **Customer Experience Dashboard — NexGen Logistics**  
AI-Powered Sentiment Analysis • Hybrid Risk Scoring • Customer Intelligence Tool

This project is a full-featured analytics dashboard built for the NexGen Logistics case study (Option 4).
It identifies at-risk customers, analyzes customer sentiment, reveals top issues, and provides actionable insights using both:

- **VADER (rule-based NLP)**
- **Machine Learning (TF-IDF + Logistic Regression)**
- **Hybrid Risk Scoring Model (Rating + Sentiment + Issue Severity + Recommendation Score)**

The dashboard is built using Streamlit, making it interactive, fast, and easy to use.
Users can upload their own CSV file or use the default dataset included.

---

## 🚀 Key Features

**1. Upload Your Own CSV**
- Supports custom customer feedback CSV files
- Auto-detects feedback columns
- Preprocesses text automatically

**2. VADER Sentiment Analysis**
- Provides quick baseline sentiment: Positive, Neutral, Negative

**3. Machine Learning Sentiment Model**
- Model: TF-IDF + Logistic Regression
- Trains on your dataset
- Evaluates accuracy
- Shows classification report
- Predicts ML sentiment for each feedback

**4. Hybrid Risk Scoring System (Advanced AI Feature)**
- Calculates customer risk based on:
  - Rating (40%): Low ratings → High risk
  - Sentiment (30%): Negative tone → High risk
  - Issue Category Severity (20%): “Damaged/Wrong Item” = more risky
  - Recommendation Likelihood (10%): “Would not recommend” = risky
- Final output: High Risk, Medium Risk, Low Risk

**5. Visual Dashboards**
- Rating distribution
- Issue category frequency
- Sentiment pie chart
- Rating trend over time
- All powered with Plotly for interactive visualization

**6. Top Words Analysis**
- Extracts most frequent meaningful words from feedback

**7. Complete Data Table**
- Shows raw feedback, VADER sentiment, ML sentiment, hybrid risk score, final risk label, issue category, date

---

## 🏗 Tech Stack

**Frontend**
- Streamlit

**NLP**
- NLTK VADER
- Preprocessing (stopwords, cleaning, tokenizing)

**Machine Learning**
- Scikit-Learn (TFIDF + Logistic Regression)
- Train/Test Split
- Accuracy Score
- Classification Report

**Visualization**
- Plotly

**Other**
- Pandas
- NumPy
- Python 3.x

---

## 📁 Project Structure

```
Customer-Experience-dashboard/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── customer_feedback.csv
│
└── modules/
    ├── data_loader.py
    ├── preprocess.py
    ├── analysis.py
    ├── visualizations.py
    ├── utils.py
    ├── ml_model.py
    └── hybrid_risk.py
```

---

## ⚙️ How to Run the Project

1. **Clone the repo**
   ```sh
   git clone https://github.com/SD995/Customer-Experience-dashboard.git
   cd Customer-Experience-dashboard
   ```

2. **Create a virtual environment**
   (Using conda)
   ```sh
   conda create -n cx_dashboard python=3.11
   conda activate cx_dashboard
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**
   ```sh
   streamlit run app.py
   ```

5. **Open in browser**
   Automatically opens at:
   👉 http://localhost:8501

---

## 📌 Dataset Requirements

Your CSV must contain:

| Column                        | Required | Example                      |
|-------------------------------|----------|------------------------------|
| feedback / feedback_text / comment | Yes      | “Delivery was late”          |
| rating                        | Yes      | 1–5                          |
| issue_category                | Optional | “delay”, “damaged item”      |
| feedback_date                 | Optional | 2024-01-12                   |
| would_recommend               | Optional | “Yes/No”                     |

See `data/customer_feedback.csv` for a sample.

---

## 🧠 How Hybrid Risk Model Works

Hybrid Risk Score = 
0.4 × RatingRisk +
0.3 × SentimentRisk +
0.2 × IssueSeverity +
0.1 × RecommendationRisk

Then converts score → risk bucket:

| Score   | Risk Level  |
|---------|-------------|
| ≥ 0.70  | High Risk   |
| 0.40–0.69 | Medium Risk |
| < 0.40  | Low Risk    |

This is how the dashboard identifies at-risk customers.

---

## 📊 Screenshots


### Dashboard Screenshots

#### KPI Section
![KPI Section](assets/Screenshot%202025-11-19%20225208.png)

#### ML Accuracy
![ML Accuracy](assets/Screenshot%202025-11-19%20225225.png)

#### Charts
![Charts](assets/Screenshot%202025-11-19%20225245.png)
![Charts 2](assets/Screenshot%202025-11-19%20225255.png)
![Charts 3](assets/Screenshot%202025-11-19%20225305.png)

#### Risk Table
![Risk Table](assets/Screenshot%202025-11-19%20225322.png)
![Risk Table 2](assets/Screenshot%202025-11-19%20233823.png)

---

## 🙌 Author

**Subrata Das**  
 OFIServices — Option 4 (Customer Experience Dashboard)

*Note: NexGen Logistics is the case study company. The original company that gave the problem statement is OFIservices.*

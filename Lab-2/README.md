# ARTI 308 - Machine Learning: Lab 2

## Identifying ML Problems, Selecting Open Datasets, and Drawing a Methodology Diagram

---

## Dataset Information

**Dataset Name:** Student Performance Dataset  
**Source:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/320/student+performance

### Dataset Description

The Student Performance dataset contains data about student achievement in secondary education from two Portuguese schools. The data was collected through school reports and questionnaires, capturing student grades along with demographic, social, and school-related features.

**Dataset Characteristics:**
- **Number of Instances:** 395 students
- **Number of Features:** 30 attributes + 3 grade columns (G1, G2, G3)
- **Feature Types:** Integer, Categorical, Binary
- **Missing Values:** None

---

## Machine Learning Problem Definition

### Problem Type: Regression

### Target Variable: G3 (Final Grade)
- The target variable G3 represents the final year grade issued at the 3rd period
- Values range from 0 to 20
- G3 has strong correlation with G1 (1st period grade) and G2 (2nd period grade)

### Problem Statement

> **"Given a student's demographic information, family background, social factors, and school-related attributes, predict their final grade (G3) in the course."**

### Why Regression?

This is a **Regression** problem because:
1. The target variable (G3) is **continuous/numerical**
2. We aim to predict a **specific grade value**, not a category
3. The output is a real number within the range [0, 20]

### Alternative Approach

This problem can also be approached as **Classification** by converting grades into categories:
- **Binary Classification:** Pass (G3 ≥ 10) vs Fail (G3 < 10)
- **Multi-class Classification:** Grade levels (A, B, C, D, F)

---

## Key Features

| Feature | Type | Description |
|---------|------|-------------|
| school | Categorical | Student's school (GP or MS) |
| sex | Binary | Student's sex (F or M) |
| age | Integer | Student's age (15-22) |
| Medu | Integer | Mother's education level (0-4) |
| Fedu | Integer | Father's education level (0-4) |
| studytime | Integer | Weekly study time (1-4 scale) |
| failures | Integer | Number of past class failures |
| absences | Integer | Number of school absences |
| G1 | Integer | First period grade (0-20) |
| G2 | Integer | Second period grade (0-20) |
| **G3** | Integer | **Final grade (0-20) - TARGET** |

---

## Repository Contents

```
├── README.md                       # This file - Dataset and problem description
├── Lab2_Student_Performance.ipynb  # Jupyter Notebook with data loading and inspection
├── student_performance.csv         # Dataset file
└── methodology_diagram.png         # ML workflow methodology diagram
```

---

## Methodology

The machine learning workflow for this project follows these steps:

1. **Dataset Selection** - Choose appropriate dataset from UCI Repository
2. **Data Loading** - Load CSV data using Pandas
3. **Data Preprocessing** - Handle missing values, encode categorical variables, normalize features
4. **Train/Test Split** - Divide data into training and testing sets (e.g., 80/20)
5. **Model Training** - Train regression models (Linear Regression, Random Forest, etc.)
6. **Model Evaluation** - Evaluate using metrics like MSE, RMSE, R² score
7. **Results Analysis** - Analyze and interpret the results

---

## How to Run

1. Clone this repository
2. Ensure you have Python and Jupyter Notebook installed
3. Install required packages: `pip install pandas`
4. Open `Lab2_Student_Performance.ipynb` in Jupyter Notebook
5. Run all cells to see the data loading and inspection results

---

## References

- Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T
- P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto, Portugal, April, 2008.

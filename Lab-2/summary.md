# Dataset & Machine Learning Problem Summary

## Dataset: Student Performance

The **Student Performance Dataset** (UCI Machine Learning Repository) contains records for **395 students** from two Portuguese secondary schools. Data was collected via school reports and questionnaires, capturing 30 input features across three categories:

- **Demographic:** age, sex, home address, family size
- **Social:** parental education and jobs, alcohol consumption, romantic relationships, free time
- **Academic:** study time, past failures, school support, absences, first and second period grades (G1, G2)

There are no missing values, and features are a mix of numerical and categorical types.

## Machine Learning Problem

**Type:** Regression

**Goal:** Predict a student's **final grade (G3)**, a numerical score ranging from 0 to 20, based on their demographic background, family environment, and academic history.

This is a regression problem because the target variable G3 is continuous. A natural alternative framing is binary classification — predicting whether a student passes (G3 ≥ 10) or fails — but the regression formulation preserves the full grade information and allows for more nuanced predictions.

**Key challenge:** G3 is strongly correlated with G1 and G2 (earlier period grades), so the model must learn which non-grade features independently explain final performance.

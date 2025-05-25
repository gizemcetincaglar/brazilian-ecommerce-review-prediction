# 🛍️ Brazilian E-Commerce Review Prediction

## 📌 Project Description

This project aims to predict whether a customer's product review will be 5 stars using supervised learning techniques. We use the public dataset provided by [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), which includes data about orders, products, customers, and reviews from Brazilian e-commerce.

---

## Bağlantılar
https://www.kaggle.com/code/gizemetinalar/notebook56725a62e7,
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---


## 🧠 Problem Statement

Can we predict whether a product review will be 5 stars based on order, product, and customer data?

- **Target:** `is_five_star` (1 if review_score == 5, otherwise 0)
- **Task Type:** Binary Classification

---

## 📂 Dataset Used

We merged the following CSVs from the dataset:

- `olist_orders_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`

All were joined on `order_id`.

---

## 🔍 Exploratory Data Analysis (EDA)

- Distribution of review scores
- Imbalance in target (`is_five_star`)
- Relationships between features and the target

---

## 🧹 Data Preprocessing

- Null value handling
- Label encoding for categorical features
- Feature selection
- Train-test split

---

## 🤖 Model Used

- **Model:** Decision Tree Classifier
- **Optimization:** GridSearchCV
- **Metrics:** Accuracy, Confusion Matrix, Precision, Recall, F1 Score

---

## 🎯 Best Parameters (via GridSearchCV)

```python
max_depth=10  
min_samples_split=5  
criterion='entropy'


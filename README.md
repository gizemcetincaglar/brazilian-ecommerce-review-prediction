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

##  Gelecekteki Geliştirme Fikirleri

-  **Topluluk Modelleri (Ensemble Models) Denenebilir:**  
  Random Forest veya XGBoost gibi topluluk tabanlı algoritmalar ile modelin genel doğruluğu ve genelleme kapasitesi artırılabilir.

-  **Özellik Önem Sıralaması Görselleştirilebilir:**  
  Modelin hangi sütunlara ne kadar önem verdiği görselleştirilerek yorumlama yapılabilir. Bu sayede sadeleştirme (feature selection) uygulanabilir.

- ⚖ **Veri Dengesizliği İçin SMOTE Uygulanabilir:**  
  Sınıf dağılımı dengesizse, Synthetic Minority Over-sampling Technique (SMOTE) yöntemi ile veri artırma yapılabilir.

-  **Model Arayüz ile Yayınlanabilir (Deploy):**  
  Streamlit veya Flask gibi frameworkler kullanılarak model bir web arayüzüne entegre edilebilir ve kullanıcıların canlı tahmin yapması sağlanabilir.

-  **Gözetimsiz Öğrenme Yöntemleri Eklenebilir:**  
  Bonus olarak, k-means gibi gözetimsiz algoritmalar ile müşteri kümelendirme veya ürün segmentasyonu yapılabilir.


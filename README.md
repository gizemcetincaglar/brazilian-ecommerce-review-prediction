# Brezilya E-Ticaret 5 Yıldızlı Değerlendirme Tahmini

## Proje Açıklaması

Bu projede, bir müşterinin yaptığı ürün değerlendirmesinin 5 yıldız olup olmayacağını gözetimli öğrenme yöntemleriyle tahmin etmeyi amaçladım.  
Bu amaç doğrultusunda Olist tarafından sağlanan Brezilya e-ticaret veri seti kullanıldı. Veri seti siparişler, ürünler, müşteriler ve değerlendirmeleri içermektedir.

---

## Bağlantılar

- Kaggle Notebook: https://www.kaggle.com/code/gizemetinalar/notebook56725a62e7  
- Kaggle Olist Veri Seti: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## Problem Tanımı

Sipariş, ürün ve müşteri bilgilerinden yola çıkarak bir değerlendirme puanının 5 yıldız olup olmayacağı tahmin edilebilir mi?

- Hedef Değişken: `is_five_star` (eğer `review_score` = 5 ise 1, aksi halde 0)  
- Problem Türü: İkili sınıflandırma

---

## Kullanılan Veri Seti

Aşağıdaki CSV dosyaları `order_id` alanı üzerinden birleştirilerek analizde kullanılmıştır:

- olist_orders_dataset.csv  
- olist_order_reviews_dataset.csv  
- olist_order_items_dataset.csv  
- olist_products_dataset.csv

---

## Keşifsel Veri Analizi (EDA)

- Değerlendirme puanlarının dağılımı incelendi  
- Hedef değişkendeki (`is_five_star`) sınıf dengesizliği kontrol edildi  
- Özelliklerle hedef değişken arasındaki ilişkiler analiz edildi

---

## Veri Ön İşleme

- Gereksiz sütunlar kaldırıldı  
- Eksik veriler temizlendi  
- Kategorik veriler sayısal verilere dönüştürüldü  
- Hedef değişken (`is_five_star`) oluşturuldu  
- Veriler eğitim ve test seti olarak ayrıldı (80/20 oranında)

---

## Kullanılan Model

- Model: Karar Ağacı (Decision Tree Classifier)  
- Optimizasyon: GridSearchCV (5 katlı çapraz doğrulama)  
- Değerlendirme Metrikleri: Doğruluk, Karışıklık Matrisi, Precision, Recall, F1 Skoru

---

## GridSearchCV ile En İyi Parametreler

```python
max_depth = 10  
min_samples_split = 5  
criterion = 'entropy'

# brazilian-ecommerce-review-prediction

Bu repo, Global AI Hub bootcamplerinde template olarak kullanmanız amacıyla tasarlanmıştır. Bu proje, Olist tarafından sağlanan Brezilya e-ticaret veri seti ile müşterilerin ürün değerlendirmelerinin 5 yıldız olup olmayacağını tahmin etmeye yönelik bir sınıflandırma (classification) çalışmasıdır.

---

## Giriş

Bu projede, Kaggle üzerinde yayınlanan [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) veri seti kullanılmıştır.  
Hedefimiz, müşterilerin bir siparişi 5 yıldızla değerlendirip değerlendirmeyeceğini tahmin etmektir.

Çalışma boyunca;

- `olist_orders_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`

veri dosyaları birleştirilerek analiz için uygun hale getirilmiştir.

Kullanılan algoritmalar:
- Karar Ağacı (Decision Tree Classifier)
- GridSearchCV ile hiperparametre optimizasyonu

---

## Metrikler

Model başarı oranları test verisi üzerinden değerlendirilmiştir.

- **Test Doğruluğu (Accuracy):** ~0.82  
- **Ek metrikler:** Karışıklık Matrisi, Precision, Recall, F1 Skoru

Yorum:
Modelin sınıflar arası dengeli bir tahmin performansı sergilediği gözlemlenmiştir. Hiperparametre optimizasyonu sonucunda modelin doğruluk oranı artırılmıştır. Özelliklerin hedef değişken ile ilişkisi analiz edilmiştir.

---

## Ekler

Bu proje kapsamında aşağıdaki gibi ek geliştirme fikirleri önerilmiştir:

- Random Forest ve XGBoost gibi topluluk modelleri ile doğruluk artırılabilir
- SMOTE gibi veri dengeleme yöntemleri uygulanabilir
- Özellik önem sıralaması görselleştirilebilir
- Streamlit veya Flask kullanılarak web arayüzü ile model dağıtımı yapılabilir (deployment)
- Bonus olarak k-means gibi gözetimsiz öğrenme yöntemleriyle müşteri segmentasyonu yapılabilir

Not: Streamlit arayüzü için ayrı bir `UI` klasörü eklenebilir.

---

## Sonuç ve Gelecek Çalışmalar

Bu proje, sınıflandırma problemleri üzerine güçlü bir başlangıç oluşturmakta ve model performansını artırmak için çeşitli yollar sunmaktadır. Gelecek çalışmalar kapsamında:

- Model farklı veri kümeleri ile test edilebilir
- Model deploy edilerek son kullanıcıya sunulabilir
- Gerçek zamanlı veri toplama mekanizmaları entegre edilebilir
- Arayüz tasarımı geliştirilebilir

Bu proje, kariyer yolculuğunuzda makine öğrenmesi temellerini göstermek ve ileride geliştireceğiniz projeler için bir temel sunmak amacıyla hazırlanmıştır.

---

## Linkler

Aşağıda projeye ait Kaggle bağlantıları yer almaktadır:

- Notebook: [https://www.kaggle.com/code/gizemetinalar/notebook56725a62e7](https://www.kaggle.com/code/gizemetinalar/notebook56725a62e7)  
- Veri Seti: [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

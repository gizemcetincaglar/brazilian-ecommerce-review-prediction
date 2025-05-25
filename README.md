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

Bu proje kapsamında aşağıdaki gibi ek geliştirme çalışmaları yapılmıştır:

- `ui/` klasörü içerisinde yer alan `app.py` dosyası ile **Streamlit arayüzü** geliştirilmiştir.
- Bu arayüz sayesinde kullanıcı, sipariş bilgilerini girerek modelin tahminine gerçek zamanlı olarak ulaşabilmektedir.

Ek olarak aşağıdaki fikirler ilerleyen geliştirme adımları için önerilmiştir:

- Random Forest ve XGBoost gibi topluluk modelleri ile doğruluk artırılabilir
- SMOTE gibi veri dengeleme yöntemleri uygulanabilir
- Özellik önem sıralaması görselleştirilebilir
- Flask veya FastAPI ile alternatif arayüz yöntemleri denenebilir
- Gözetimsiz öğrenme (ör. k-means) ile müşteri segmentasyonu yapılabilir

---

## Sonuç ve Gelecek Çalışmalar

Bu proje, sınıflandırma problemleri üzerine güçlü bir başlangıç oluşturmakta ve model performansını artırmak için çeşitli yollar sunmaktadır. Gelecek çalışmalar kapsamında:

- Model farklı veri kümeleri ile test edilebilir
- Geliştirilen arayüz daha kullanıcı dostu hale getirilebilir
- Model, dinamik verilerle çalışabilecek şekilde genişletilebilir
- Proje bir web uygulamasına dönüştürülerek son kullanıcıya açılabilir

Bu proje, kariyer yolculuğunuzda makine öğrenmesi temellerini göstermek ve ileride geliştireceğiniz projeler için bir temel sunmak amacıyla hazırlanmıştır.

---

## Linkler

Proje ile ilgili bağlantılar aşağıda yer almaktadır:

- Kaggle Notebook: [https://www.kaggle.com/code/gizemetinalar/notebook56725a62e7](https://www.kaggle.com/code/gizemetinalar/notebook56725a62e7)  
- Kullanılan Veri Seti: [https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

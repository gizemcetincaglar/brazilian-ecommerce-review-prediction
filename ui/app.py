import streamlit as st
import pickle
import pandas as pd

# Model yükleme
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Brezilya E-Ticaret - 5 Yıldız Tahmin Uygulaması")
st.write("Müşteri sipariş bilgilerine göre 5 yıldızlı değerlendirme alınıp alınamayacağını tahmin edin.")

# Örnek girişler
product_category = st.selectbox("Ürün Kategorisi (Kodlanmış)", [0, 1, 2, 3, 4])
payment_type = st.selectbox("Ödeme Türü (Kodlanmış)", [0, 1, 2, 3])
price = st.number_input("Ürün Fiyatı", min_value=0.0, step=1.0)
freight_value = st.number_input("Kargo Ücreti", min_value=0.0, step=1.0)
order_status = st.selectbox("Sipariş Durumu (Kodlanmış)", [0, 1, 2])

# Diğer özellikler eklenebilir...

# Tahmin
if st.button("Tahmini Hesapla"):
    input_data = pd.DataFrame([[
        product_category,
        payment_type,
        price,
        freight_value,
        order_status
    ]], columns=["product_category_name_encoded", "payment_type", "price", "freight_value", "order_status"])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Bu siparişin 5 yıldızlı değerlendirme alma olasılığı yüksek!")
    else:
        st.warning("Bu siparişin 5 yıldız alma olasılığı düşük.")


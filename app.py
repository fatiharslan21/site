import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(
    page_title="Sadece Senin İçin",
    page_icon="🌸",
    layout="centered"
)

# --- CSS VE ANİMASYONLAR ---
# Burası sitenin makyajı. Yazıların yavaşça gelmesini ve şık durmasını sağlıyor.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@300;500&display=swap');

/* Genel Arka Plan */
.stApp {
    background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    background-image: url("https://www.transparenttextures.com/patterns/cubes.png"); /* Hafif doku */
}

/* Yazıların bulunduğu kutu tasarımı */
.card-container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    text-align: center;
    border: 1px solid #ffe6e6;
    animation: fadeIn 2s;
}

/* Fade In Animasyonu (Yavaşça belirme) */
@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* Başlık Fontu */
h1 {
    font-family: 'Dancing Script', cursive;
    color: #c06c84;
    font-size: 3rem !important;
    margin-bottom: 20px;
}

/* Normal Yazı Fontu */
p {
    font-family: 'Quicksand', sans-serif;
    font-size: 1.4rem;
    color: #555;
    line-height: 1.8;
}

/* Buton Tasarımı */
.stButton>button {
    background-color: #c06c84;
    color: white;
    border-radius: 30px;
    padding: 10px 30px;
    border: none;
    font-family: 'Quicksand', sans-serif;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(192, 108, 132, 0.3);
}

.stButton>button:hover {
    background-color: #6c5b7b;
    transform: scale(1.05);
}

/* Çiçekler */
.sakura {
    position: fixed;
    top: -10%;
    z-index: 0;
    user-select: none;
    animation-name: fall, shake;
    animation-duration: 12s, 4s;
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: infinite, infinite;
}
@keyframes fall { 0% {top: -10%;} 100% {top: 100%;} }
@keyframes shake { 0% {transform: translateX(0px) rotate(0deg);} 50% {transform: translateX(80px) rotate(20deg);} 100% {transform: translateX(0px) rotate(0deg);} }

</style>
""", unsafe_allow_html=True)

# Çiçek Efekti (Arka planda süzülenler)
flowers_html = "".join([f"""
<div class="sakura" style="left: {i * 5}%; animation-delay: {i * 0.8}s; color: #ffb7b2; font-size: {20 + (i % 10)}px;">❀</div>
""" for i in range(15)])
st.markdown(flowers_html, unsafe_allow_html=True)

# --- SAYFA GEÇİŞ MANTIĞI ---
if 'page' not in st.session_state:
    st.session_state.page = 0


def next_page():
    st.session_state.page += 1


def restart():
    st.session_state.page = 0


# --- İÇERİK AKIŞI ---

# Boşluk bırakalım ki ortalı dursun
st.write("")
st.write("")

# 1. SAHNE: Giriş
if st.session_state.page == 0:
    st.markdown("""
    <div class="card-container">
        <h1>Biraz Konuşabilir miyiz?</h1>
        <p>Sana söylemek istediklerim var. Ama aceleyle değil, yavaş yavaş...</p>
        <p>Sadece kalbini dinlemeye hazırsan, butona bas.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        st.button("Dinliyorum...", on_click=next_page)

# 2. SAHNE: Empati (Geçmiş)
elif st.session_state.page == 1:
    st.markdown("""
    <div class="card-container">
        <h1>Seni Anlıyorum...</h1>
        <p>Geçmişin bıraktığı izleri görebiliyorum. Güvenmenin senin için ne kadar zor olduğunu, 
        tekrar üzülmekten ne kadar korktuğunu biliyorum.</p>
        <p>Haklısın. İnsan kendini korumalı...</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        st.button("Devam et...", on_click=next_page)

# 3. SAHNE: Güven ve Farklılık
elif st.session_state.page == 2:
    st.markdown("""
    <div class="card-container">
        <h1>Ama Ben Onlar Değilim</h1>
        <p>Ben senin duvarlarını yıkmak için savaşmaya gelmedim. 
        Ben sadece o duvarların kapısında, sen hazır olana kadar beklemeye geldim.</p>
        <p>Benim yanımda gardını indirdiğinde karşılaşacağın tek şey şefkat olur.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        st.button("Peki ya sonra?", on_click=next_page)

# 4. SAHNE: Final (Teklif)
elif st.session_state.page == 3:
    st.balloons()
    st.markdown("""
    <div class="card-container">
        <h1>Biz Çok Güzel Olabiliriz</h1>
        <p>Biliyorum korkuyorsun, ama korkularımız mutluluğumuzun önüne geçmesin.</p>
        <p>Bana güvenmen için sana zaman, sabır ve sonsuz bir anlayış vadediyorum.</p>
        <p><b>Benimle bu yolda, yavaşça yürümeye var mısın?</b></p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        # Buraya tıklandığında başa döner, istersen buraya WhatsApp linki koyabilirsin.
        st.button("Başa Dön 🌹", on_click=restart)
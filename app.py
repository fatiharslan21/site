import streamlit as st
import time

# --- BURAYI SEN DOLDURACAKSIN ---
# Tırnakların içine en son sayfada çıkacak o vurucu notunu yaz.
OZEL_NOT = """ 
Biliyorum geçmişte yaşananları değiştiremem ama yerlerine en güzel anıları birlikte koyabileceğimizi biliyorum.
Ben her şeye yeniden başlamaya, en baştan, en güzel halimizle tanışmaya hazırım. En güzel halimiz olmasa da her halini de sevecek olmanın mutluluğu içindeyim.
Ben tıpkı ailenin yanında olduğun gibi huzurlu ve rahat olacağın kişi, başını koyacağın bir omuz, sırtını yaslayacağın bir duvar olmaya hazırım.
Her zaman burada olacağıma söz veriyorum. İyi ki varsın..
"""

# Sayfa Ayarları
st.set_page_config(
    page_title="Sana Özel...",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS VE TASARIM (MOBİL UYUMLU VE HIZLI) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Montserrat:wght@300;400&display=swap');

/* Arka Plan */
.stApp {
    background: linear-gradient(135deg, #fff5f7 0%, #e3eeff 100%);
}

/* KART TASARIMI (Buzlu Cam) */
.glass-card {
    background: rgba(255, 255, 255, 0.70);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 40px 20px; /* Mobilde kenar boşlukları azaldı */
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.4);
    text-align: center;
    margin-top: 20px;
    width: 100%;
    max-width: 600px; /* Geniş ekranlarda çok yayılmasın */
    margin-left: auto;
    margin-right: auto;

    /* HIZLANDIRILMIŞ ANİMASYON (1.2 Saniye) */
    animation: dreamyFade 1.2s ease-out;
}

/* MOBİL İÇİN ÖZEL AYARLAR */
@media only screen and (max-width: 600px) {
    .glass-card {
        padding: 30px 15px;
        margin-top: 10px;
    }
    h1 {
        font-size: 1.8rem !important; /* Mobilde başlık biraz daha küçülsün */
    }
    p {
        font-size: 1rem !important;
    }
}

/* GEÇİŞ ANİMASYONU */
@keyframes dreamyFade {
    0% { opacity: 0; transform: translateY(20px); filter: blur(5px); }
    100% { opacity: 1; transform: translateY(0); filter: blur(0px); }
}

/* BAŞLIK */
h1 {
    font-family: 'Dancing Script', cursive;
    color: #b84b5c;
    font-size: 2.2rem;
    margin-bottom: 20px;
    font-weight: normal;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

/* YAZI */
p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1rem;
    color: #555;
    line-height: 1.6;
    margin-bottom: 25px;
}

/* BUTON */
.stButton>button {
    background-color: #b84b5c;
    color: white;
    border-radius: 50px;
    padding: 12px 35px;
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    border: none;
    box-shadow: 0 4px 15px rgba(184, 75, 92, 0.2);
    width: 100%; /* Mobilde butona basmak kolay olsun */
}
.stButton>button:hover {
    background-color: #8c3a4a;
    transform: scale(1.02);
}

/* MÜZİK ÇALAR GİZLEME (Opsiyonel: Eğer oynatıcı çok çirkin durursa bunu açarız) */
/* audio { width: 100%; margin-top: 20px; } */

</style>
""", unsafe_allow_html=True)

# Çiçek Efekti (Z-index -1 ile yazının arkasında)
flowers_html = "".join([f"""
<div style="position: fixed; left: {i * 8}%; top: -10%; z-index: -1; 
animation: fall {8 + i}s linear infinite; color: #ffcce0; font-size: {15 + (i % 10)}px;">❀</div>
<style>@keyframes fall {{ 0% {{top: -10%; transform: rotate(0deg);}} 100% {{top: 100%; transform: rotate(360deg);}} }}</style>
""" for i in range(12)])
st.markdown(flowers_html, unsafe_allow_html=True)

# --- MÜZİK ÇALAR ---
# Eğer 'muzik.mp3' dosyası varsa çalışır, yoksa hata vermez, sessizce geçer.
try:
    st.audio("muzik.mp3", format="audio/mp3")
except:
    pass  # Müzik dosyası yoksa site bozulmasın

# --- SAYFA MANTIĞI ---
if 'page' not in st.session_state:
    st.session_state.page = 0


def next_page():
    time.sleep(0.1)
    st.session_state.page += 1


def restart():
    st.session_state.page = 0


# Ortalamak için boşluk
st.write("")

# 1. GİRİŞ
if st.session_state.page == 0:
    st.markdown(f"""
    <div class="glass-card">
        <h1>Biraz Konuşabilir miyiz?</h1>
        <p>Sadece senin ve benim olduğum, acele etmemiz gerekmeyen bir hikaye...</p>
        <p>Hazır hissettiğinde başla.</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Dinliyorum...", on_click=next_page)

# 2. EMPATİ
elif st.session_state.page == 1:
    st.markdown("""
    <div class="glass-card">
        <h1>Korkularını Görüyorum</h1>
        <p>Güvenmenin, o duvarları indirmenin ne kadar zor olduğunu biliyorum.<br>
        Geçmişte canın yandı ve kendini korumak istiyorsun.</p>
        <p>Bu çok insani, çok haklı bir his...</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Devam et...", on_click=next_page)

# 3. GÜVEN
elif st.session_state.page == 2:
    st.markdown("""
    <div class="glass-card">
        <h1>Ama Ben Farklı Bir Yerdeyim</h1>
        <p>Ben senin savaşacağın bir cephe değilim.<br>
        Ben, yorulduğunda dinlenebileceğin gölgenim.</p>
        <p>Acelemiz yok. Sen ne zaman "gel" dersen, ben o zaman bir adım atarım.</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Son söz...", on_click=next_page)

# 4. FİNAL (ÖZEL NOTUN BURADA ÇIKACAK)
elif st.session_state.page == 3:
    st.balloons()
    st.markdown(f"""
    <div class="glass-card">
        <h1>Biz Çok Güzel Olabiliriz...</h1>
        <p>{OZEL_NOT}</p>
        <p style="font-size: 0.9rem; color: #b84b5c; margin-top:30px;">(Kalbimi buraya bıraktım...)</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("En Başa Dön 🌹", on_click=restart)

import streamlit as st
import time

# --- SENİN YAZACAĞIN KISIM ---
OZEL_NOT = """ Biliyorum geçmişte yaşananları değiştiremem ama yerlerine en güzel anıları birlikte koyabileceğimizi biliyorum.
Ben tıpkı ailenin yanında olduğun gibi yanında huzurlu ve rahat olacağın kişi, başını koyacağın bir omuz, sırtını yaslayacağın bir duvar olmaya hazırım.
Ben zor olanı başarmaya, seninle en güzel hikayeyi yazmaya talibim.
Sadece elini uzatman yeterli.İyi ki varsın..
"""

# Sayfa Ayarları
st.set_page_config(
    page_title="Sana Özel...",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS SİHRİ (TASARIM VE ANİMASYONLAR) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@300;500&display=swap');

/* Arka Plan */
.stApp {
    background: linear-gradient(135deg, #fff0f3 0%, #e6e6fa 100%);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* KART TASARIMI */
.glass-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(15px);
    border-radius: 25px;
    padding: 40px 20px;
    box-shadow: 0 10px 40px rgba(255, 105, 180, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.6);
    text-align: center;
    margin-top: 30px;
    margin-bottom: 20px; /* Butonla arasındaki boşluk */
    animation: slideUp 1s ease-out;
}

@keyframes slideUp {
    0% { opacity: 0; transform: translateY(40px) scale(0.9); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}

/* BUTON TASARIMI */
/* Butonun rengi ve şekli burada ayarlanır, konumu aşağıda Python ile ayarlanacak */
.stButton>button {
    background: linear-gradient(45deg, #d63384, #ff6b6b);
    color: white;
    border-radius: 50px;
    padding: 15px 0px; /* İç boşluk */
    width: 100%;       /* Bulunduğu kolonun tamamını kaplasın */
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1rem;
    font-weight: 500;
    border: none;
    box-shadow: 0 5px 15px rgba(214, 51, 132, 0.4);
    transition: all 0.3s ease;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(214, 51, 132, 0.7); }
    70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(214, 51, 132, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(214, 51, 132, 0); }
}

.stButton>button:hover {
    background: linear-gradient(45deg, #ff6b6b, #d63384);
    transform: translateY(-2px);
    animation: none;
}

/* Yazı Stilleri */
h1 {
    font-family: 'Dancing Script', cursive;
    color: #c84b6c;
    font-size: 2.5rem;
    margin-bottom: 20px;
    text-shadow: 2px 2px 0px rgba(255,255,255,0.5);
}

p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.2rem;
    color: #666;
    line-height: 1.6;
}

/* YAĞAN NESNELER (Kalp ve Çiçek) */
.falling-object {
    position: fixed;
    top: -10%;
    z-index: 0;
    user-select: none;
    animation-name: fall, sway;
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: infinite, infinite;
}

@keyframes fall { 0% {top: -10%; opacity: 1;} 100% {top: 105%; opacity: 0.2;} }
@keyframes sway { 0% {transform: translateX(0px) rotate(0deg);} 50% {transform: translateX(50px) rotate(180deg);} 100% {transform: translateX(0px) rotate(360deg);} }

</style>
""", unsafe_allow_html=True)

# --- EFEKTLERİ OLUŞTURMA ---
objects_html = ""
for i in range(15):
    objects_html += f"""
    <div class="falling-object" style="left: {i * 7}%; animation-duration: {10 + i}s, {3 + (i % 3)}s; animation-delay: {i * 0.5}s; font-size: {20 + (i % 10)}px; color: #ffb7b2;">🌸</div>
    <div class="falling-object" style="left: {(i * 7) + 3}%; animation-duration: {12 + i}s, {4 + (i % 3)}s; animation-delay: {i * 0.8}s; font-size: {15 + (i % 5)}px; color: rgba(255, 0, 80, 0.4);">❤️</div>
    """
st.markdown(objects_html, unsafe_allow_html=True)

# --- SAYFA MANTIĞI ---
if 'page' not in st.session_state:
    st.session_state.page = 0


def next_page():
    time.sleep(0.1)
    st.session_state.page += 1


def restart():
    st.session_state.page = 0


# --- SAYFALAR ---

# Sayfa ortalaması için boşluk
st.write("")

# 1. GİRİŞ
if st.session_state.page == 0:
    st.markdown("""
    <div class="glass-card">
        <h1>Bir Hikayemiz Olsun...</h1>
        <p>Bazı kelimeler yüze söylenemez, bazı hisler aceleye gelmez.</p>
        <p>Sadece kalbini dinlemeye hazırsan...</p>
    </div>
    """, unsafe_allow_html=True)

    # BUTONU ORTALAMAK İÇİN KOLON SİSTEMİ
    # [1, 1, 1] demek ekranı 3'e böl, ortadakini (col2) kullan demektir.
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.button("Başla ❤️", on_click=next_page)

# 2. GEÇMİŞ
elif st.session_state.page == 1:
    st.markdown("""
    <div class="glass-card">
        <h1>Seni Hissediyorum</h1>
        <p>Geçmişin ağırlığını, omuzlarındaki o görünmez yükü görüyorum.<br>
        Güvenmek senin için dik bir yokuş, biliyorum.</p>
        <p>Korkmakta çok haklısın...</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.button("Ama...", on_click=next_page)

# 3. GÜVEN
elif st.session_state.page == 2:
    st.markdown("""
    <div class="glass-card">
        <h1>Ben Buradayım</h1>
        <p>Ben senin yaralarını deşmeye değil, sarmaya geldim.<br>
        Duvarlarını yıkmaya değil, kapında beklemeye geldim.</p>
        <p>Acelemiz yok. Sen "hazırım" diyene kadar buradayım.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.button("Ve Son Olarak...", on_click=next_page)

# 4. FİNAL
elif st.session_state.page == 3:
    st.balloons()
    st.markdown(f"""
    <div class="glass-card">
        <h1>Yeni Bir Başlangıç?</h1>
        <p>{OZEL_NOT}</p>
        <p style="font-size: 0.9rem; color: #c84b6c; margin-top:30px;">(Cevabını bekliyor olacağım...)</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.button("Başa Dön 🌹", on_click=restart)
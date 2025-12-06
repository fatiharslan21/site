import streamlit as st
import time

# Sayfa Ayarları (Sekme ismi ve ikonu)
st.set_page_config(
    page_title="Sadece Senin İçin...",
    page_icon="🌹",
    layout="centered"
)

# --- CSS TASARIMI (SİHRİN OLDUĞU YER) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Montserrat:wght@300;400&display=swap');

/* Arka Plan */
.stApp {
    background: linear-gradient(135deg, #fff5f7 0%, #e3eeff 100%);
}

/* KART TASARIMI (Buzlu Cam Efekti) */
.glass-card {
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(10px); /* Arkasını hafif buzlu gösterir */
    -webkit-backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 50px 30px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.18);
    text-align: center;
    margin-top: 50px;

    /* Animasyon Tanımları */
    animation: dreamyFade 2.5s ease-out;
}

/* GEÇİŞ ANİMASYONU (Rüya Efekti) */
@keyframes dreamyFade {
    0% { 
        opacity: 0; 
        transform: translateY(30px) scale(0.95);
        filter: blur(10px); /* Başlangıçta bulanık */
    }
    100% { 
        opacity: 1; 
        transform: translateY(0) scale(1);
        filter: blur(0px); /* Sonunda net */
    }
}

/* BAŞLIK AYARLARI (Küçültüldü ve Zarifleştirildi) */
h1 {
    font-family: 'Dancing Script', cursive;
    color: #b84b5c; /* Soluk Gül Rengi */
    font-size: 2.2rem !important; /* Boyut küçültüldü */
    margin-bottom: 25px;
    font-weight: normal;
}

/* DÜZ YAZI AYARLARI */
p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1rem;
    color: #5d5d5d;
    line-height: 1.8;
    margin-bottom: 30px;
}

/* BUTON TASARIMI (Daha Soft) */
.stButton>button {
    background-color: #b84b5c;
    color: white;
    border-radius: 50px;
    padding: 12px 40px;
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    border: none;
    transition: all 0.4s ease;
    box-shadow: 0 4px 15px rgba(184, 75, 92, 0.2);
}

.stButton>button:hover {
    background-color: #8c3a4a;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(184, 75, 92, 0.4);
}

/* SÜZÜLEN ÇİÇEKLER (Sakura) */
.sakura {
    position: fixed;
    top: -10%;
    z-index: -1; /* Yazının arkasında kalsın */
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

# Çiçekleri Oluşturma
flowers_html = "".join([f"""
<div class="sakura" style="left: {i * 7}%; animation-delay: {i * 1.2}s; color: #ffcce0; font-size: {18 + (i % 10)}px;">❀</div>
""" for i in range(12)])
st.markdown(flowers_html, unsafe_allow_html=True)

# --- SAYFA MANTIĞI ---
if 'page' not in st.session_state:
    st.session_state.page = 0


def next_page():
    time.sleep(0.2)  # Tıklama hissiyatı için minik bekleme
    st.session_state.page += 1


def restart():
    st.session_state.page = 0


# --- SAYFALAR VE İÇERİKLER ---

# Sayfa içeriğini ortalamak için boşluk
st.write("")

# 1. GİRİŞ SAYFASI
if st.session_state.page == 0:
    st.markdown("""
    <div class="glass-card">
        <h1>Bir Hikaye Anlatabilir miyim?</h1>
        <p>Sadece senin ve benim olduğum, acele etmemiz gerekmeyen bir hikaye...</p>
        <p>Hazır hissettiğinde başla.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        st.button("Dinliyorum...", on_click=next_page)

# 2. EMPATİ SAYFASI
elif st.session_state.page == 1:
    st.markdown("""
    <div class="glass-card">
        <h1>Korkularını Görüyorum</h1>
        <p>Güvenmenin, o duvarları indirmenin ne kadar zor olduğunu biliyorum.<br>
        Geçmişte canın yandı ve kendini korumak istiyorsun.</p>
        <p>Bu çok insani, çok haklı bir his...</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        st.button("Devam et...", on_click=next_page)

# 3. GÜVEN SAYFASI
elif st.session_state.page == 2:
    st.markdown("""
    <div class="glass-card">
        <h1>Ama Ben Farklı Bir Yerdeyim</h1>
        <p>Ben senin savaşacağın bir cephe değilim.<br>
        Ben, yorulduğunda dinlenebileceğin gölgenim.</p>
        <p>Acelemiz yok. Sen ne zaman "gel" dersen, ben o zaman bir adım atarım.<br>
        Senden tek isteğim, bana o kapıyı aralık bırakman.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        st.button("Son söz...", on_click=next_page)

# 4. FİNAL SAYFASI
elif st.session_state.page == 3:
    # Finalde konfetiler patlasın
    st.balloons()

    st.markdown("""
    <div class="glass-card">
        <h1>Güzel Olabiliriz...</h1>
        <p>Geçmişin gölgesi, geleceğin ışığını kapatmasın.</p>
        <p>Benimle bu yolda, korkmadan, yavaş yavaş yürümeye var mısın?<br>
        Söz veriyorum, o kalbi el üstünde tutacağım.</p>
        <p style="font-size: 0.9rem; color: #b84b5c;">(Cevabını bana yazarsın...)</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.write("")
        st.button("En Başa Dön 🌹", on_click=restart)
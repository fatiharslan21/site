import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(
    page_title="Sadece Senin İçin",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS TASARIMI (Görsel Büyü ve Çiçekler) ---
# Burası sitenin kalbi. Arka planı, fontları ve o süzülen çiçekleri burada ayarlıyoruz.
page_bg_img = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300;400&display=swap');

/* Arka Plan Gradyanı */
.stApp {
    background: linear-gradient(to bottom right, #fff0f5, #e6e6fa);
    font-family: 'Montserrat', sans-serif;
}

/* Başlık Fontu */
h1 {
    font-family: 'Great Vibes', cursive;
    color: #d63384;
    text-align: center;
    font-size: 3.5rem !important;
    text-shadow: 2px 2px 4px #00000020;
}

/* Düz Yazı Stili */
p {
    color: #4a4a4a;
    font-size: 1.2rem;
    line-height: 1.6;
    text-align: justify;
}

/* --- ÇİÇEK ANİMASYONU --- */
.sakura {
    position: fixed;
    top: -10%;
    z-index: 9999;
    user-select: none;
    cursor: default;
    animation-name: fall, shake;
    animation-duration: 10s, 3s;
    animation-timing-function: linear, ease-in-out;
    animation-iteration-count: infinite, infinite;
    animation-play-state: running, running;
}

@keyframes fall {
    0% {top: -10%;}
    100% {top: 100%;}
}

@keyframes shake {
    0% {transform: translateX(0px) rotate(0deg);}
    50% {transform: translateX(80px) rotate(20deg);}
    100% {transform: translateX(0px) rotate(0deg);}
}

/* Çiçek Yaprağı Görünümü */
.petal {
    color: #ffb7b2;
    font-size: 20px;
}
</style>
"""

# Çiçekleri ekrana rastgele dağıtan HTML bloğu
flowers_html = "".join([f"""
<div class="sakura petal" style="left: {i * 5}%; animation-delay: {i * 0.5}s; font-size: {15 + (i % 10)}px;">🌸</div>
<div class="sakura petal" style="left: {(i * 5) + 2}%; animation-delay: {(i * 0.5) + 2}s; font-size: {10 + (i % 5)}px;">❀</div>
""" for i in range(20)])

st.markdown(page_bg_img + flowers_html, unsafe_allow_html=True)

# --- İÇERİK KISMI ---

# 1. Giriş: Yumuşak bir karşılama
st.title("Biraz Durup Dinlenmen İçin...")
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Buraya onunla veya seninle ilgili güzel, soft bir fotoğraf koyabilirsin.
    # st.image("senin_resmin.jpg", caption="Huzur...")
    pass

st.write("")
st.write("")

# 2. Empati Bölümü: Onu anladığını hissettir
st.markdown("""
Biliyorum, bazen güvenmek uçurumun kenarında yürümek gibi geliyor. 
Geçmişin gölgesi üzerine düştüğünde, kendini korumak için duvarlar örmen çok doğal. 
Sana kızmıyorum, aksine seni anlıyorum. O duvarlar seni üzülmekten koruyor sanıyorsun...
""")

st.write("")

# 3. Güven Mesajı: "Ben Farklıyım" değil, "Ben Buradayım"
with st.expander("💌 İçimden geçenleri okumak ister misin?", expanded=False):
    st.markdown("""
    Ben senin geçmişindeki fırtınalar değilim. Ben o fırtınalar dindiğinde sığınabileceğin, 
    sakin bir liman olmak istiyorum sadece.

    Korkularını yok saymanı beklemiyorum. Sadece şunu bilmeni istiyorum:
    **Benim yanımda gardını düşürdüğünde sırtından vurulmazsın, sadece sarılıp sarmalanırsın.**

    Acelemiz yok. Zamanla, yavaş yavaş... Çiçeklerin acele etmeden açtığı gibi.
    """)

st.write("")
st.write("")

# 4. İnteraktif Kapanış: Vurucu Nokta
st.info("Eğer bir gün o duvarların arkasından bakmak istersen, ben tam olarak burada olacağım.")

if st.button("🌹 Benimle Bir Şans Denemeye Ne Dersin?"):
    st.balloons()  # Ekrana balonlar/çiçekler uçar
    st.success("Bu yolculukta yalnız yürümeyeceğine söz veriyorum. Teşekkür ederim...")
    # Burada isteğe bağlı olarak bir müzik başlatabilirsin
    # st.audio("sizin_sarkiniz.mp3", format="audio/mp3", start_time=0)

else:
    st.write("*(Cevabın ne olursa olsun, değerin bende hep aynı kalacak...)*")
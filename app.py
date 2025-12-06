import streamlit as st
import base64
import streamlit.components.v1 as components

# --- AYARLAR ---
st.set_page_config(page_title="Sana Özel", page_icon="❤️", layout="wide", initial_sidebar_state="collapsed")

# --- STREAMLIT ARAYÜZÜNÜ GİZLEME VE TAM EKRAN AYARLARI ---
st.markdown("""
    <style>
        /* Üst barı ve menüyü gizle */
        header {visibility: hidden;}
        [data-testid="stHeader"] {display: none;}

        /* Alt bilgiyi (footer) gizle */
        footer {visibility: hidden;}

        /* Sayfa içeriğini genişlet ve boşlukları sil */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* iframe'in etrafındaki boşlukları kaldır */
        iframe {
            display: block; 
            border: none;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)


# --- MÜZİK DOSYASINI OKUMA VE GÖMME ---
def get_audio_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None


# 'muzik.mp3' dosyasının 'app.py' ile aynı klasörde olduğundan emin ol
muzik_b64 = get_audio_base64("muzik.mp3")
muzik_html = ""
if muzik_b64:
    muzik_html = f"""
    <audio id="bg-music" loop>
        <source src="data:audio/mp3;base64,{muzik_b64}" type="audio/mp3">
    </audio>
    """

# --- HTML/CSS/JS KODU (PRO VERSİYON) ---
html_code = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@300;400;600&display=swap');

    /* TEMEL AYARLAR */
    body, html {{
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100vh;
        overflow: hidden; /* Kaydırmayı engelle */
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }}

    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* KART YAPISI */
    .container {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        max-width: 500px;
        text-align: center;
        z-index: 10;
    }}

    .card {{
        background: rgba(255, 255, 255, 0.85);
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: all 0.5s ease;
        opacity: 0;
        transform: scale(0.8);
        display: none;
    }}

    .card.active {{
        display: block;
        opacity: 1;
        transform: scale(1);
        animation: fadeIn 0.8s forwards;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    h1 {{
        font-family: 'Dancing Script', cursive;
        color: #D80027; 
        font-size: 2.5rem;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }}

    p {{
        font-size: 1.1rem;
        line-height: 1.6;
        color: #444;
        margin-bottom: 30px;
    }}

    /* BUTON */
    .btn {{
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        border: none;
        color: white;
        padding: 15px 40px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 50px;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);
        outline: none;
    }}

    .btn:hover {{
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 75, 43, 0.6);
    }}

    /* YAĞMUR EFEKTİ */
    .emoji {{
        position: fixed;
        top: -10vh;
        z-index: 1;
        animation-name: fall;
        animation-timing-function: linear;
    }}

    @keyframes fall {{
        to {{ transform: translateY(110vh) rotate(720deg); }}
    }}

</style>
</head>
<body>

    {muzik_html}

    <div class="container">
        <div id="slide1" class="card active">
            <h1>Bir Hikayemiz Olsun...</h1>
            <p>Bazı kelimeler yüze söylenemez, bazı hisler aceleye gelmez.<br>Sadece kalbini dinlemeye hazırsan...</p>
            <button class="btn" onclick="nextSlide(1)">Başla ❤️</button>
        </div>

        <div id="slide2" class="card">
            <h1>Seni Anlıyorum</h1>
            <p>Geçmişin ağırlığını, omuzlarındaki o görünmez yükü görüyorum. Güvenmek senin için dik bir yokuş, biliyorum.<br><br>Korkmakta çok haklısın...</p>
            <button class="btn" onclick="nextSlide(2)">Ama...</button>
        </div>

        <div id="slide3" class="card">
            <h1>Ben Buradayım</h1>
            <p>Ben senin yaralarını deşmeye değil, sarmaya geldim. Duvarlarını yıkmaya değil, kapında beklemeye geldim.<br><br>Acelemiz yok. Sen "hazırım" diyene kadar buradayım.</p>
            <button class="btn" onclick="nextSlide(3)">Ve Son Olarak...</button>
        </div>

        <div id="slide4" class="card">
            <h1>Yeni Bir Başlangıç?</h1>
            <p>Canım Selenay, Biliyorum geçmişte yaşananları değiştiremem ama yerlerine en güzel anıları birlikte koyabiliriz.
            <br><br>
            Tıpkı ailenin yanında olduğun gibi yanında huzurlu ve rahat olacağın kişi, başını koyacağın bir omuz, sırtını yaslayacağın bir duvar olmaya hazırım.
            Ben zor olanı başarmaya, seninle en güzel hikayeyi yazmaya talibim.
            <br><br>
            Beş kırmızı ışığın söneceği ve mükemmel bir yarışa başlayacağımız o anı iple çekiyorum. Sadece elini uzatman yeterli. İyi ki varsın..</p>
            <p style="font-size: 0.9rem; color: #D80027; margin-top:20px; font-weight:bold;">(Cevabını bekliyor olacağım...)</p>
            <button class="btn" onclick="location.reload()">Başa Dön 🌹</button>
        </div>
    </div>

    <script>
        // Müzik Başlatma (İlk etkileşimde)
        var music = document.getElementById("bg-music");
        function playMusic() {{
            if(music && music.paused) {{
                music.play().catch(e => console.log(e));
                music.volume = 0.6;
            }}
        }}

        // Slayt Geçişi
        function nextSlide(current) {{
            playMusic();
            document.getElementById('slide' + current).classList.remove('active');

            setTimeout(() => {{
                document.getElementById('slide' + (current + 1)).classList.add('active');
            }}, 300);

            if (current === 3) startConfetti();
        }}

        // Yağmur Efekti
        function createRain() {{
            const emojis = ['🌸', '❤️', '🌹', '✨'];
            setInterval(() => {{
                const el = document.createElement('div');
                el.classList.add('emoji');
                el.innerText = emojis[Math.floor(Math.random() * emojis.length)];
                el.style.left = Math.random() * 100 + 'vw';
                el.style.animationDuration = (Math.random() * 3 + 2) + 's';
                el.style.fontSize = (Math.random() * 20 + 20) + 'px';
                document.body.appendChild(el);
                setTimeout(() => el.remove(), 5000);
            }}, 200);
        }}
        createRain();

        // Konfeti
        function startConfetti() {{
             setInterval(() => {{
                const el = document.createElement('div');
                el.classList.add('emoji');
                el.innerText = '🎉';
                el.style.left = Math.random() * 100 + 'vw';
                el.style.animationDuration = '2.5s';
                document.body.appendChild(el);
                setTimeout(() => el.remove(), 2500);
            }}, 100);
        }}
    </script>
</body>
</html>
"""

# Yüksekliği artırdık ki mobilde kaydırma çubuğu çıkmasın
components.html(html_code, height=900, scrolling=False)
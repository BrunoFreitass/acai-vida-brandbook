# python
import streamlit as st
from pathlib import Path
import io
import zipfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# ==================================================
# CONFIGURAÇÃO
# ==================================================

st.set_page_config(
    import base64

def imagem_base64(caminho):
    arquivo = Path(caminho)
    if not arquivo.exists():
        return ""

    with open(arquivo, "rb") as img:
        return base64.b64encode(img.read()).decode()

fundo = imagem_base64(FUNDO_CAPA)

if fundo:
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{fundo}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .main .block-container {{
        background: rgba(255,255,255,0.88);
        padding: 2rem;
        border-radius: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)
    page_title="Açaí Vida | Brandbook",
    page_icon="logo_01.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# 🎨 CSS COM ANIMAÇÕES SUAVES
# ==================================================

st.markdown("""
<link rel="stylesheet"
href="https://fonts.cdnfonts.com/css/armonioso">

<style>

/* fade-in geral */
body {
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* títulos */
.title {
    font-family: 'Armonioso', cursive;
    font-size: 54px;
    font-weight: 900;
    color: #4B1E2F;
    animation: slideUp 0.8s ease-in-out;
}

.subtitle {
    color: #777;
    animation: fadeIn 1.2s ease-in-out;
}

/* entrada de seções */
section, div.block-container {
    animation: fadeIn 1s ease-in-out;
}

/* cards de cores */
div[style*="background"] {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

div[style*="background"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* imagens hover */
img {
    transition: transform 0.3s ease;
}

img:hover {
    transform: scale(1.02);
}

/* slide up */
@keyframes slideUp {
    from {
        transform: translateY(20px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA (LOGO + NOME ESQUERDA)
# ==================================================

logo = Path("logo_01.png")

col1, col2 = st.columns([1,5])

with col1:
    if logo.exists():
        st.image(str(logo), width=120)

with col2:
    st.markdown("<div class='title'>AÇAÍ VIDA</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Brandbook Acadêmico • Identidade Visual</div>", unsafe_allow_html=True)
    st.info("""

📁 Imagens de Fundo

CAPA → fundo_01.png

IDENTIDADE → fundo_02.png

CONCEITO → fundo_03.png

TIPOGRAFIA → fundo_04.png

PALETA → fundo_04.png

APLICAÇÕES → fundo_05.png

MOCKUPS → fundo_01.png
""")

st.divider()

# ==================================================
# IDENTIDADE VISUAL
# ==================================================

st.header("01 • Identidade Visual")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Logo Principal")
    st.image("logo_01.png", width=250)

with col2:
    st.subheader("Logos diversas")
    st.image("Logos_01.png", width=500)

st.divider()

# ==================================================
# CONCEITO
# ==================================================

st.header("02 • Conceito da Marca")

st.write("""
A Açaí Vida representa energia, cultura amazônica e identidade visual forte.
""")

st.divider()

# ==================================================
# TIPOGRAFIA
# ==================================================

st.header("03 • Tipografia")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Gelato Luxe")
    st.image("gelato.png")
    st.caption("Fonte principal da marca")

with col2:
    st.subheader("Poppins Bold")
    st.image("poppins.png")
    st.caption("Fonte secundária")

with col3:
    st.subheader("Montserrat Regular")
    st.image("montserrat.png")
    st.caption("Fonte de apoio")

st.divider()

# ==================================================
# PALETA DE CORES (LOGO AO LADO)
# ==================================================

st.header("04 • Paleta de Cores")

col_logo, col_cores = st.columns([1,3])

with col_logo:
    st.image("logo_01.png", width=120)

with col_cores:

    cores = [
        ("Roxo Açaí", "#5B2A8C"),
        ("Verde Energia", "#D2D914"),
        ("Amarelo Tropical", "#F2CB05"),
        ("Branco Neve", "#FDFBFE"),
        ("Roxo Profundo", "#2D0B48"),
    ]

    cols = st.columns(3)

    for i, (nome, cor) in enumerate(cores):

        with cols[i % 3]:

            text_color = "black" if cor.upper() == "#FDFBFE" else "white"

            st.markdown(f"""
            <div style="
                background:{cor};
                padding:22px;
                border-radius:12px;
                text-align:center;
                font-weight:bold;
                color:{text_color};
            ">
            {nome}<br>{cor}
            </div>
            """, unsafe_allow_html=True)

st.divider()

# ==================================================
# APLICAÇÃO
# ==================================================

st.header("05 • Aplicação da Marca")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🥤 Copo Comercial")
    st.image("acai_01.png")
    st.image("acai_02.png")

with col2:
    st.subheader("🍨 Taça Premium")
    st.image("sorvete_02.png")
    st.image("banner_01.png")

st.divider()

# ==================================================
# MOCKUPS
# ==================================================

st.header("06 • Mockups")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("out_01.png", caption="Outdoor")

with col2:
    st.image("uniforme_01.png", caption="Uniforme")

with col3:
    st.image("insta_01.png", caption="Instagram")

st.divider()

# ==================================================
# COMENTÁRIOS E AVALIAÇÕES
# ==================================================

st.header("07 • Comentários e Avaliações")

comentarios = st.text_area(
    "Comentários",
    height=200,
    placeholder="Digite observações, sugestões ou avaliações do projeto..."
)

avaliacao = st.slider(
    "Avaliação Geral",
    min_value=1,
    max_value=10,
    value=10
)

st.divider()

# ==================================================
# EXPORTAÇÃO
# ==================================================

st.header("08 • Exportação")

def gerar_pdf():

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawString(180, 750, "AÇAÍ VIDA")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(160, 730, "Brandbook Acadêmico")

    if Path("logo_01.png").exists():
        pdf.drawImage(
            "logo_01.png",
            240,
            520,
            width=120,
            height=120
        )

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer
    
def gerar_zip():

    buffer = io.BytesIO()

    with zipfile.ZipFile(
    buffer,
    "w",
    zipfile.ZIP_DEFLATED
) as z:

        arquivos = [
            "Logos_01.png",
            "acai_01.png",
            "acai_02.png",
            "banner_01.png",
            "fundo_01.png",
            "fundo_02.png",
            "fundo_03.jpg",
            "fundo_05.png",
            "gelato.png",
            "insta_01.png",
            "logo_01.png",
            "mirtilo.png",
            "montserrat.png",
            "out_01.png",
            "poppins.png",
            "sorvete_01.png",
            "sorvete_02.png",
            "uniforme_01.png",
        ]

        for f in arquivos:
            if Path(f).exists():
                z.write(f)

    buffer.seek(0)
    return buffer

st.download_button("📄 Baixar PDF", gerar_pdf(), "brandbook.pdf", "application/pdf")

st.download_button("📦 Baixar KIT (.zip)", gerar_zip(), "kit_acai.zip", "application/zip")

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("Açaí Vida • Brandbook Acadêmico • 2026")

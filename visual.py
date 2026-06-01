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
    page_title="Açaí Vida | Brandbook",
    page_icon="editaveis/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# CSS SIMPLES (SEM QUEBRAR STREAMLIT)
# ==================================================

st.markdown("""
<style>

.title {
    font-size: 54px;
    font-weight: 900;
    color: #4B1E2F;
    margin-bottom: 0px;
}

.subtitle {
    color: #777;
    margin-top: 0px;
}

.section {
    margin-top: 25px;
}

.card {
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #eee;
}

.color-box {
    padding: 20px;
    border-radius: 12px;
    color: white;
    font-weight: bold;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA (LOGO + NOME À ESQUERDA — ESTÁVEL)
# ==================================================

logo = Path("editaveis/logo.png")

col1, col2 = st.columns([1,5])

with col1:
    if logo.exists():
        st.image(str(logo), width=120)

with col2:
    st.markdown("<div class='title'>AÇAÍ VIDA</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Brandbook Acadêmico • Identidade Visual</div>", unsafe_allow_html=True)

st.divider()

# ==================================================
# FUNÇÃO TÍTULO
# ==================================================

def titulo(n, t):
    st.markdown(f"## {n}")
    st.header(t)

# ==================================================
# IDENTIDADE VISUAL
# ==================================================

titulo("01", "Identidade Visual")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Logo Principal")
    st.image("editaveis/logo.png", width=250)

with col2:
    st.subheader("Logos diversas")
    st.image("editaveis/logos.png", width=500)

st.divider()

# ==================================================
# CONCEITO
# ==================================================

titulo("02", "Conceito da Marca")

st.write("""
A Açaí Vida representa energia, cultura amazônica e identidade visual forte.
""")

st.divider()

# ==================================================
# 🎨 PALETA DE CORES (LOGO AO LADO)
# ==================================================

titulo("03", "Paleta de Cores")

col_logo, col_cores = st.columns([1, 3])

with col_logo:
    st.image("editaveis/logo.png", width=140)

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

            st.markdown(f"""
            <div style="
                background:{cor};
                padding:22px;
                border-radius:12px;
                text-align:center;
                font-weight:bold;
                color:white;
            ">
            {nome}<br>{cor}
            </div>
            """, unsafe_allow_html=True)

st.divider()

# ==================================================
# APLICAÇÃO DA MARCA
# ==================================================

titulo("04", "Aplicação da Marca")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🥤 Copo Comercial")
    st.image("editaveis/açai.01.png")

with col2:
    st.subheader("🍨 Taça Premium")
    st.image("editaveis/açai.02.png")

st.divider()

# ==================================================
# MOCKUPS
# ==================================================

titulo("05", "Mockups da Marca")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🥤 Copo")
    st.image("editaveis/acai.03.png", use_container_width=True)

with col2:
    st.markdown("### 👕 Uniforme")
    st.image("editaveis/uniforme.png", use_container_width=True)

with col3:
    st.markdown("### 📱 Instagram")
    st.image("editaveis/insta.jpg", use_container_width=True)

st.divider()

# ==================================================
# 📦 ZIP KIT
# ==================================================

def gerar_zip():

    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, "w") as z:

        arquivos = [
            "editaveis/logo.png",
            "editaveis/logos_diversas.png",
            "editaveis/acai.01.png",
            "editaveis/acai.02.png",
            "editaveis/acai.03.png",
            "editaveis/uniforme.png",
            "editaveis/insta.jpg",
        ]

        for f in arquivos:
            if Path(f).exists():
                z.write(f)

    buffer.seek(0)
    return buffer

st.download_button(
    "📦 Baixar Kit da Marca (.zip)",
    data=gerar_zip(),
    file_name="acai_vida_kit.zip",
    mime="application/zip"
)

st.divider()

# ==================================================
# 📄 PDF SIMPLES
# ==================================================

def gerar_pdf():

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawString(180, 750, "AÇAÍ VIDA")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(160, 730, "Brandbook Acadêmico")

    if Path("editaveis/logo.png").exists():
        pdf.drawImage("editaveis/logo.png", 240, 520, width=120, height=120)

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer

st.download_button(
    "📄 Baixar Brandbook PDF",
    data=gerar_pdf(),
    file_name="brandbook_acai_vida.pdf",
    mime="application/pdf"
)

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("Açaí Vida • Brandbook Acadêmico • 2026")

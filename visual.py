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
# CSS LIMPO (SEM CONFLITO)
# ==================================================

st.markdown("""
<style>

.title {
    font-size: 56px;
    font-weight: 900;
    text-align: center;
    color: #4B1E2F;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #777;
    margin-bottom: 20px;
}

.center {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA (LOGO + NOME CENTRALIZADO DE VERDADE)
# ==================================================

logo = Path("editaveis/logo.png")

# 🔥 CENTRALIZAÇÃO REAL (SEM HTML QUEBRADO)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown('<div class="center">', unsafe_allow_html=True)

    if logo.exists():
        st.image(str(logo), width=170)

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='title'>AÇAÍ VIDA</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Brandbook Acadêmico • Identidade Visual</div>", unsafe_allow_html=True)

st.caption("Instituto Federal de Roraima • Projeto Acadêmico • 2026")

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
# PALETA DE CORES (CARDS)
# ==================================================

titulo("03", "Paleta de Cores")

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
            padding:25px;
            border-radius:14px;
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
    st.image("editaveis/acai.01.png")

with col2:
    st.subheader("🍨 Taça Premium")
    st.image("editaveis/acai.02.png")

st.divider()

# ==================================================
# MOCKUPS
# ==================================================

titulo("05", "Mockups")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("editaveis/acai.03.png", caption="Copo")

with col2:
    st.image("editaveis/uniforme.png", caption="Uniforme")

with col3:
    st.image("editaveis/insta.jpg", caption="Instagram")

st.divider()

# ==================================================
# ZIP KIT COMPLETO
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
# PDF SIMPLES (ESTÁVEL)
# ==================================================

def gerar_pdf():

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawCentredString(300, 750, "AÇAÍ VIDA")

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(300, 730, "Brandbook Acadêmico")

    if Path("editaveis/logo.png").exists():
        pdf.drawImage("editaveis/logo.png", 220, 520, width=150, height=150)

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

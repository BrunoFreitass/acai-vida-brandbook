# python
import streamlit as st
from pathlib import Path
import io
import zipfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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
# CSS
# ==================================================

st.markdown("""
<style>

.title {
    font-size: 54px;
    font-weight: 900;
    text-align: center;
    color: #4B1E2F;
}

.subtitle {
    text-align: center;
    color: #777;
}

.card {
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #eee;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA
# ==================================================

logo = Path("editaveis/logo.png")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if logo.exists():
        st.image(str(logo), width=160)

st.markdown("<div class='title'>AÇAÍ VIDA</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Brandbook Acadêmico • Identidade Visual</div>", unsafe_allow_html=True)

st.divider()

# ==================================================
# FUNÇÃO
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
    st.image("editaveis/logos_diversas.png", width=500)

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
# PALETA DE CORES
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
        st.markdown(
            f"""
            <div style="
                background:{cor};
                padding:25px;
                border-radius:12px;
                color:white;
                text-align:center;
                font-weight:bold;
            ">
            {nome}<br>{cor}
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# ==================================================
# 🍨 APLICAÇÃO DA MARCA (RESTAURADO COMPLETO)
# ==================================================

titulo("04", "Aplicação da Marca")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🥤 Copo Comercial (acai.01)")

    img1 = Path("editaveis/acai.01.png")  # 📌 AQUI COLOCA O COPO

    if img1.exists():
        st.image(str(img1))
    else:
        st.warning("Coloque aqui: editaveis/acai.01.png")

with col2:

    st.subheader("🍨 Taça Premium (acai.02)")

    img2 = Path("editaveis/acai.02.png")  # 📌 AQUI COLOCA A TAÇA

    if img2.exists():
        st.image(str(img2))
    else:
        st.warning("Coloque aqui: editaveis/acai.02.png")

st.divider()

# ==================================================
# 📱 MOCKUPS RESTAURADO
# ==================================================

titulo("05", "Mockups da Marca")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Copo")
    st.image("editaveis/acai.03.png")  # 📌 MOCKUP

with col2:

    st.subheader("Uniforme")
    st.image("editaveis/uniforme.png")  # 📌 UNIFORME

with col3:

    st.subheader("Instagram")
    st.image("editaveis/insta.jpg")  # 📌 SOCIAL

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

zip_file = gerar_zip()

st.download_button(
    "📦 Baixar Kit da Marca (.zip)",
    data=zip_file,
    file_name="acai_vida_kit.zip",
    mime="application/zip"
)

# ==================================================
# 📄 PDF SIMPLES (ESTRUTURA)
# ==================================================

def gerar_pdf():

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(300, 750, "AÇAÍ VIDA")

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(300, 730, "Brandbook Acadêmico")

    logo_path = "editaveis/logo.png"

    if Path(logo_path).exists():
        pdf.drawImage(logo_path, 220, 550, width=150, height=150)

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer

pdf_file = gerar_pdf()

st.download_button(
    "📄 Baixar Brandbook PDF",
    data=pdf_file,
    file_name="brandbook_acai_vida.pdf",
    mime="application/pdf"
)

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("Açaí Vida • Brandbook Acadêmico • 2026")

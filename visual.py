# python
import streamlit as st
from pathlib import Path
import io
import zipfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

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
# CSS (STYLE AGÊNCIA)
# ==================================================

st.markdown("""
<style>

.title {
    font-size: 56px;
    font-weight: 900;
    text-align: center;
    color: #4B1E2F;
}

.subtitle {
    text-align: center;
    color: #777;
    margin-bottom: 20px;
}

.card {
    background: #fff;
    border-radius: 14px;
    padding: 15px;
    border: 1px solid #eee;
}

.color-card {
    padding: 25px;
    border-radius: 14px;
    color: white;
    font-weight: bold;
    text-align: center;
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
        st.image(str(logo), width=170)

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

col1, col2 = st.columns([2,2])

with col1:
    st.subheader("Logo Principal")
    st.image("editaveis/logo.png", width=250)

with col2:
    st.subheader("Paleta de Cores")

# ==================================================
# PALETA (CARDS PROFISSIONAIS)
# ==================================================

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
            color:{'black' if cor in ['#FDFBFE', '#F2CB05'] else 'white'};
            font-weight:bold;
            text-align:center;
        ">
        {nome}<br>{cor}
        </div>
        """, unsafe_allow_html=True)

        if st.button("📋 Copiar HEX", key=f"copy_{i}"):
            st.success(f"Copiado: {cor}")

st.divider()

# ==================================================
# LOGOS DIVERSAS
# ==================================================

titulo("02", "Logos diversas")

st.image("editaveis/logos_diversas.png", width=600)

st.divider()

# ==================================================
# CONCEITO
# ==================================================

titulo("03", "Conceito da Marca")

st.write("""
A Açaí Vida representa energia, cultura amazônica e identidade visual forte.
""")

st.divider()

# ==================================================
# 📄 PDF PROFISSIONAL (COM LOGO + DESIGN)
# ==================================================

def gerar_pdf():

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Capa
    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawCentredString(300, 750, "AÇAÍ VIDA")

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(300, 725, "Brandbook de Identidade Visual")

    # Logo no PDF
    logo_path = "editaveis/logo.png"
    if Path(logo_path).exists():
        pdf.drawImage(logo_path, 220, 550, width=150, height=150, preserveAspectRatio=True)

    # Linha
    pdf.line(50, 500, 550, 500)

    # Paleta
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, 470, "Paleta de Cores:")

    cores_pdf = [
        "#5B2A8C",
        "#D2D914",
        "#F2CB05",
        "#2D0B48"
    ]

    y = 440
    for c in cores_pdf:
        pdf.setFont("Helvetica", 12)
        pdf.drawString(60, y, f"- {c}")
        y -= 20

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer

pdf_file = gerar_pdf()

st.download_button(
    "📄 Baixar Brandbook PDF",
    data=pdf_file,
    file_name="acai_vida_brandbook.pdf",
    mime="application/pdf"
)

st.divider()

# ==================================================
# 📦 ZIP KIT COMPLETO DA MARCA
# ==================================================

def gerar_zip():

    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, "w") as z:

        arquivos = [
            "editaveis/logo.png",
            "editaveis/logos_diversas.png",
            "editaveis/acai.01.png",
            "editaveis/acai.02.png"
        ]

        for file in arquivos:
            if Path(file).exists():
                z.write(file)

        # adiciona PDF dentro do zip
        z.writestr("brandbook.pdf", pdf_file.getvalue())

    buffer.seek(0)
    return buffer

zip_file = gerar_zip()

st.download_button(
    "📦 Baixar Kit Completo da Marca (.zip)",
    data=zip_file,
    file_name="acai_vida_kit_marca.zip",
    mime="application/zip"
)

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("Açaí Vida • Brandbook Acadêmico • 2026")

# python
import streamlit as st
from pathlib import Path
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

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
# CSS (ESTILO BEHANCE / FIGMA)
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
    margin-bottom: 20px;
}

.card {
    background: #ffffff;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #eee;
    margin-bottom: 10px;
}

.color-box {
    padding: 20px;
    border-radius: 12px;
    color: white;
    font-weight: bold;
    margin-bottom: 8px;
}

button {
    border-radius: 8px;
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

col1, col2 = st.columns([2,2])

with col1:
    st.subheader("Logo Principal")
    st.image("editaveis/logo.png", width=250)

with col2:
    st.subheader("Paleta Base")

# ==================================================
# PALETA (CARDS + COPY HEX)
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
            padding:20px;
            border-radius:12px;
            color:white;
            font-weight:bold;
            text-align:center;
        ">
        {nome}<br>{cor}
        </div>
        """, unsafe_allow_html=True)

        # COPY BUTTON
        if st.button("📋 Copiar HEX", key=f"copy_{i}"):
            st.write(f"Copiado: {cor}")

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
# EXPORTAÇÃO PDF
# ==================================================

titulo("04", "Exportar Brandbook")

def gerar_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(100, 750, "Brandbook Açaí Vida")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 720, "Identidade Visual - Projeto Acadêmico")

    pdf.save()
    buffer.seek(0)
    return buffer

pdf_file = gerar_pdf()

st.download_button(
    label="📄 Baixar Brandbook PDF",
    data=pdf_file,
    file_name="acai_vida_brandbook.pdf",
    mime="application/pdf"
)

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("Açaí Vida • Brandbook Acadêmico • 2026")

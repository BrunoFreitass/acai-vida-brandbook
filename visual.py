# python
import streamlit as st
from pathlib import Path
import io
import zipfile
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# ==================================================
# IMAGENS DE FUNDO
# ==================================================

FUNDO_CAPA = "fundo_01.png"
FUNDO_IDENTIDADE = "fundo_02.png"
FUNDO_CONCEITO = "fundo_03.png"
FUNDO_TIPOGRAFIA = "fundo_04.png"
FUNDO_PALETA = "fundo_04.png"
FUNDO_APLICACOES = "fundo_05.png"
FUNDO_MOCKUPS = "fundo_01.png"

# ==================================================
# CONFIGURAÇÃO
# ==================================================

st.set_page_config(
    page_title="Açaí Vida | Brandbook",
    page_icon="logo_01.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# FUNDO DA APLICAÇÃO
# ==================================================

def imagem_base64(caminho):
    arquivo = Path(caminho)

    if not arquivo.exists():
        return None

    with open(arquivo, "rb") as img:
        return base64.b64encode(img.read()).decode()

fundo = imagem_base64(FUNDO_CAPA)

if fundo:
    st.markdown(f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpeg;base64,{fundo}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    .main .block-container {{
        background: rgba(255,255,255,0.90);
        border-radius: 20px;
        padding: 2rem;
    }}

    </style>
    """, unsafe_allow_html=True)

# ==================================================
# 🎨 CSS COM ANIMAÇÕES SUAVES
# ==================================================

if fundo:
    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/jpeg;base64,{fundo}") !important;
            background-size: cover !important;
            background-position: center center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}

        [data-testid="stHeader"] {{
            background: transparent !important;
        }}

        .main .block-container {{
            background-color: rgba(255,255,255,0.88);
            padding: 2rem;
            border-radius: 24px;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

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
st.divider()

# ==================================================
# IDENTIDADE VISUAL
# ==================================================

st.header("01 • Identidade Visual")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Logo Principal")
    st.image("logo_01.png", use_container_width=True)

with col2:
    st.subheader("Logos diversas")
    st.image("Logos_01.png", use_container_width=True)

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
    st.image("gelato.png", use_container_width=True)
    st.caption("Fonte principal da marca")

with col2:
    st.subheader("Poppins Bold")
    st.image("poppins.png", use_container_width=True)
    st.caption("Fonte secundária")

with col3:
    st.subheader("Montserrat Regular")
    st.image("montserrat.png", use_container_width=True)
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
    st.image("acai_01.png", use_container_width=True)
    st.image("acai_02.png", use_container_width=True)

with col2:
    st.subheader("🍨 Taça Premium")
    st.image("sorvete_02.png", use_container_width=True)
    st.image("banner_01.png", use_container_width=True)

st.divider()

# ==================================================
# MOCKUPS
# ==================================================

st.header("06 • Mockups")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("out_01.png", caption="Outdoor", use_container_width=True)

with col2:
    st.image("uniforme_01.png", caption="Uniforme", use_container_width=True)

with col3:
    st.image("insta_01.png", caption="Instagram", use_container_width=True)

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
            "fundo_03.png",
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

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

def banner(imagem):
    if Path(imagem).exists():
        with open(imagem, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        
        ext = Path(imagem).suffix.replace(".", "").lower()
        mime = f"image/{ext}" if ext in ["png", "jpg", "jpeg"] else "image/png"
        
        # Converte em HTML controlado impedindo quebra de páginas ou grandes lacunas
        st.markdown(
            f'<img src="data:{mime};base64,{data}" style="width:100%; max-height:200px; object-fit:cover; border-radius:16px; margin-bottom:20px; margin-top:10px;">',
            unsafe_allow_html=True
        )

# ==================================================
# 🎨 CSS CUSTOMIZADO
# ==================================================

st.markdown("""
<link rel="stylesheet" href="https://fonts.cdnfonts.com/css/armonioso">
<style>
.block-container{
    max-width:1400px;
    padding-top:0rem;
}
.title{
    font-family:'Armonioso', cursive;
    font-size:72px;
    color:#4B1E2F;
}
.subtitle{
    font-size:22px;
    color:#666;
}
img{
    border-radius:16px;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA
# ==================================================

banner(FUNDO_CAPA)

col1, col2 = st.columns([1, 4])

with col1:
    if Path("logo_01.png").exists():
        st.image(
            "logo_01.png",
            use_container_width=True
        )

with col2:
    st.markdown(
        "<div class='title'>AÇAÍ VIDA</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Brandbook Acadêmico • Identidade Visual</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
**Cliente:** Açaí Vida

**Ano:** 2026

**Projeto de Extensão:** Brandbook
""")

# ==================================================
# IDENTIDADE VISUAL
# ==================================================

banner(FUNDO_IDENTIDADE)

st.header("01 • Identidade Visual")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Logo Principal")
    st.image("logo_01.png", use_container_width=True)

with col2:
    st.subheader("Logos diversas")
    st.image("Logos_01.png", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# CONCEITO
# ==================================================

banner(FUNDO_CONCEITO)

st.header("02 • Conceito da Marca")

st.write("""
A Açaí Vida representa energia, cultura amazônica e identidade visual forte.
""")

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# TIPOGRAFIA
# ==================================================

banner(FUNDO_TIPOGRAFIA)

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

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# PALETA DE CORES
# ==================================================

banner(FUNDO_PALETA)

st.header("04 • Paleta de Cores")

col_logo, col_cores = st.columns([1, 3])

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

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# APLICAÇÃO
# ==================================================

banner(FUNDO_APLICACOES)

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

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# MOCKUPS
# ==================================================

banner(FUNDO_MOCKUPS)

st.header("06 • Mockups")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("out_01.png", caption="Outdoor", use_container_width=True)

with col2:
    st.image("uniforme_01.png", caption="Uniforme", use_container_width=True)

with col3:
    st.image("insta_01.png", caption="Instagram", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# COMENTÁRIOS E AVALIAÇÕES
# ==================================================

st.header("07 • Comentários e Avaliações")

comentarios = st.text_area(
    "Comentários",
    height=200,
    placeholder="Digite observações, sugestões ou avaliações do projeto..."
)

col1, col2 = st.columns(2)

with col1:
    avaliacao = st.slider(
        "Avaliação Geral",
        1,
        10,
        10
    )

with col2:
    st.metric(
        "Nota",
        f"{avaliacao}/10"
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# EXPORTAÇÃO
# ==================================================

st.header("08 • Exportação")

def gerar_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(
        buffer,
        pagesize=letter
    )

    pdf.setTitle("Brandbook Brandbook Açaí Vida")
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(160, 760, "AÇAÍ VIDA")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(150, 735, "Brandbook Acadêmico")

    if Path("logo_01.png").exists():
        pdf.drawImage(
            "logo_01.png",
            220,
            520,
            width=160,
            height=160,
            preserveAspectRatio=True
        )

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer

def gerar_zip():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
        arquivos = [
            "Logos_01.png",
            "acai_01.png",
            "acai_02.png",
            "banner_01.png",
            "fundo_01.png",
            "fundo_02.png",
            "fundo_03.png",
            "fundo_04.png",
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

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# RODAPÉ
# ==================================================

st.caption("Açaí Vida • Brandbook Acadêmico • 2026")

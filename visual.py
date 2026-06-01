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
    initial_sidebar_state="expanded"
)

# ==================================================
# CSS (ESTILO SITE / BEHANCE)
# ==================================================

st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.title {
    font-size: 54px;
    font-weight: 900;
    color: #4B1E2F;
}

.subtitle {
    color: #777;
}

.section {
    padding-top: 40px;
    padding-bottom: 40px;
    border-bottom: 1px solid #eee;
}

.card {
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #eee;
}

.color-card {
    padding: 25px;
    border-radius: 12px;
    color: white;
    text-align: center;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# MENU LATERAL (SCROLL NAVIGATION)
# ==================================================

st.sidebar.title("📌 Brandbook")

menu = st.sidebar.radio(
    "Navegação",
    [
        "Capa",
        "Identidade",
        "Tipografia",
        "Cores",
        "Aplicação",
        "Mockups",
        "Exportação"
    ]
)

# ==================================================
# CAPA
# ==================================================

if menu == "Capa":

    logo = Path("editaveis/logo.png")

    col1, col2 = st.columns([1,5])

    with col1:
        if logo.exists():
            st.image(str(logo), width=120)

    with col2:
        st.markdown("<div class='title'>AÇAÍ VIDA</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Brandbook Acadêmico • Identidade Visual</div>", unsafe_allow_html=True)

    st.write("Scroll para navegar pelo brandbook.")

# ==================================================
# IDENTIDADE VISUAL
# ==================================================

if menu == "Identidade":

    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.header("Identidade Visual")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Logo Principal")
        st.image("editaveis/logo.png", width=250)

    with col2:
        st.subheader("Logos diversas")
        st.image("editaveis/logos.png", width=500)

# ==================================================
# TIPOGRAFIA
# ==================================================

if menu == "Tipografia":

    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.header("Tipografia da Marca")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Gelato Luxe")
        st.image("editaveis/gelato.png")
        st.caption("Fonte principal")

    with col2:
        st.subheader("Poppins Bold")
        st.image("editaveis/poppins.png")
        st.caption("Fonte secundária")

    with col3:
        st.subheader("Montserrat")
        st.image("editaveis/montserrat.png")
        st.caption("Fonte de apoio")

# ==================================================
# CORES
# ==================================================

if menu == "Cores":

    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.header("Paleta de Cores")

    col_logo, col_cores = st.columns([1,3])

    with col_logo:
        st.image("editaveis/logo.png", width=120)

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

# ==================================================
# APLICAÇÃO
# ==================================================

if menu == "Aplicação":

    st.header("Aplicação da Marca")

    col1, col2 = st.columns(2)

    with col1:
        st.image("editaveis/acai.01.png")

    with col2:
        st.image("editaveis/acai.02.png")

# ==================================================
# MOCKUPS
# ==================================================

if menu == "Mockups":

    st.header("Mockups")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("editaveis/acai.03.png", caption="Copo")

    with col2:
        st.image("editaveis/uniforme.png", caption="Uniforme")

    with col3:
        st.image("editaveis/insta.jpg", caption="Instagram")

# ==================================================
# EXPORTAÇÃO
# ==================================================

if menu == "Exportação":

    st.header("Exportar Material")

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

    def gerar_zip():

        buffer = io.BytesIO()

        with zipfile.ZipFile(buffer, "w") as z:

            arquivos = [
                "editaveis/logo.png",
                "editaveis/logos.png",
                "editaveis/acai.01.png",
                "editaveis/acai.02.png",
                "editaveis/acai.03.png",
                "editaveis/uniforme.png",
                "editaveis/insta.jpg",
                "editaveis/gelato.png",
                "editaveis/poppins.png",
                "editaveis/montserrat.png",
            ]

            for f in arquivos:
                if Path(f).exists():
                    z.write(f)

        buffer.seek(0)
        return buffer

    st.download_button("📄 Baixar PDF", gerar_pdf(), "brandbook.pdf", "application/pdf")

    st.download_button("📦 Baixar KIT (.zip)", gerar_zip(), "kit_acai.zip", "application/zip")

# ==================================================
# RODAPÉ
# ==================================================

st.sidebar.caption("Açaí Vida • Brandbook 2026")

import streamlit as st
from pathlib import Path
import io
import zipfile
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

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
# DEFINIÇÃO DE FUNÇÕES (Mover para cima)
# ==================================================

def banner(imagem):
    """Renderiza uma imagem de banner cobrindo toda a largura."""
    if Path(imagem).exists():
        with open(imagem, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        
        ext = Path(imagem).suffix.replace(".", "").lower()
        mime = f"image/{ext}" if ext in ["png", "jpg", "jpeg"] else "image/png"
        
        # Converte em HTML controlado impedindo quebra de páginas ou grandes lacunas
        # Usando CSS flex e object-fit para cobrir a área e conectar
        st.markdown(
            f"""
            <div style="display: flex; width: 100%; justify-content: center; overflow: hidden;">
                <img src="data:{mime};base64,{data}" style="width: 100%; height: auto; object-fit: cover; margin-bottom: 0px; margin-top: 0px;">
            </div>
            """,
            unsafe_allow_html=True
        )

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
# 🎨 CSS CUSTOMIZADO
# ==================================================

st.markdown("""
<link rel="stylesheet" href="https://fonts.cdnfonts.com/css/armonioso">
<style>
/* Remove espaçamentos e margens padrão do Streamlit para conectar blocos */
.main .block-container {
    max-width: 100% !important;
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
}

/* Garante que imagens ocupem toda a largura do container e se conectem */
[data-testid="stImage"] img {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    margin-bottom: 0px !important;
    border-radius: 0px !important;
}

/* Remove lacunas entre elementos horizontais (colunas) */
[data-testid="stHorizontalBlock"] {
    gap: 0rem !important;
}

/* Estilos de texto */
.conteudo-texto {
    padding: 60px 80px;
    background-color: transparent; /* Permite que o fundo do container se estenda */
}

.title {
    font-family: 'Armonioso', cursive;
    font-size: 72px;
    color: #4B1E2F;
}

.subtitle {
    font-size: 22px;
    color: #666;
}

/* Estiliza o container para o feedback e comentários */
.secao-interativa {
    background-color: #f7f7f7;
    padding: 60px 80px;
    border-radius: 16px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA
# ==================================================

banner(FUNDO_CAPA)

st.markdown("""
<div class='conteudo-texto'>
    <div class='title'>AÇAÍ VIDA</div>
    <div class='subtitle'>Brandbook Acadêmico • Identidade Visual</div>
    <p>
        **Cliente:** Açaí Vida<br>
        **Ano:** 2026<br>
        **Projeto de Extensão:** Brandbook
    </p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# IDENTIDADE VISUAL
# ==================================================

banner(FUNDO_IDENTIDADE)

st.header("01 • Identidade Visual")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Logo Principal")
    if Path("logo_01.png").exists():
        st.image("logo_01.png", use_container_width=True)

with col2:
    st.subheader("Logos diversas")
    if Path("Logos_01.png").exists():
        st.image("Logos_01.png", use_container_width=True)

# Adiciona espaçamento controlado para as próximas seções
st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# CONCEITO
# ==================================================

banner(FUNDO_CONCEITO)

st.header("02 • Conceito da Marca")

st.write("""
<div class='conteudo-texto'>
    A Açaí Vida representa energia, cultura amazônica e identidade visual forte.
    O conceito foi desenhado para evocar a vibração e o frescor dos ingredientes, com uma linguagem urbana e autêntica.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# TIPOGRAFIA
# ==================================================

banner(FUNDO_TIPOGRAFIA)

st.header("03 • Tipografia")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Gelato Luxe")
    if Path("gelato.png").exists():
        st.image("gelato.png", use_container_width=True)
    st.caption("Fonte principal da marca")

with col2:
    st.subheader("Poppins Bold")
    if Path("poppins.png").exists():
        st.image("poppins.png", use_container_width=True)
    st.caption("Fonte secundária")

with col3:
    st.subheader("Montserrat Regular")
    if Path("montserrat.png").exists():
        st.image("montserrat.png", use_container_width=True)
    st.caption("Fonte de apoio")

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# PALETA DE CORES
# ==================================================

banner(FUNDO_PALETA)

st.header("04 • Paleta de Cores")

cores = [
    ("Roxo Açaí", "#5B2A8C"),
    ("Verde Energia", "#D2D914"),
    ("Amarelo Tropical", "#F2CB05"),
    ("Branco Neve", "#FDFBFE"),
    ("Roxo Profundo", "#2D0B48"),
]

# Grid de cores
cols_cores = st.columns(3)
for i, (nome, cor) in enumerate(cores):
    with cols_cores[i % 3]:
        text_color = "black" if cor.upper() == "#FDFBFE" else "white"
        st.markdown(f"""
        <div style="
            background:{cor};
            padding:22px;
            border-radius:12px;
            text-align:center;
            font-weight:bold;
            color:{text_color};
            margin-bottom: 20px;
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
    if Path("acai_01.png").exists():
        st.image("acai_01.png", use_container_width=True)
    if Path("acai_02.png").exists():
        st.image("acai_02.png", use_container_width=True)

with col2:
    st.subheader("🍨 Taça Premium")
    if Path("sorvete_02.png").exists():
        st.image("sorvete_02.png", use_container_width=True)
    if Path("banner_01.png").exists():
        st.image("banner_01.png", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# MOCKUPS
# ==================================================

banner(FUNDO_MOCKUPS)

st.header("06 • Mockups")

col1, col2, col3 = st.columns(3)

with col1:
    if Path("out_01.png").exists():
        st.image("out_01.png", caption="Outdoor", use_container_width=True)

with col2:
    if Path("uniforme_01.png").exists():
        st.image("uniforme_01.png", caption="Uniforme", use_container_width=True)

with col3:
    if Path("insta_01.png").exists():
        st.image("insta_01.png", caption="Instagram", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# COMENTÁRIOS E AVALIAÇÕES
# ==================================================

# Usa um container estilizado para feedback
st.markdown("""
<div class='secao-interativa'>
    <h2>07 • Feedback & Comentários</h2>
</div>
""", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([2, 1])

    with col1:
        comentario_texto = st.text_area(
            "Deixe suas observações",
            height=150,
            placeholder="Digite observações, sugestões ou avaliações do projeto...",
            key="comentario"
        )
        botao_enviar = st.button("Enviar Comentário")

    with col2:
        avaliacao_nota = st.slider(
            "Avaliação Geral",
            min_value=1,
            max_value=10,
            value=10,
            step=1,
            key="avaliacao"
        )
        st.metric(
            "Sua Nota",
            f"{avaliacao_nota}/10"
        )

# Inicializa e exibe a lista de comentários usando st.session_state
if 'lista_comentarios' not in st.session_state:
    st.session_state.lista_comentarios = []

if botao_enviar:
    # Adiciona o novo comentário ao estado da sessão se o campo não estiver vazio
    if st.session_state.comentario.strip():
        st.session_state.lista_comentarios.append({
            'texto': st.session_state.comentario.strip(),
            'nota': st.session_state.avaliacao
        })
        # Limpa o campo de texto (isso precisa de um truque de callback no Streamlit)
        # Por enquanto, apenas atualizamos e exibimos
        st.rerun()
    else:
        st.warning("O campo de comentário não pode estar vazio.")

# Exibe os comentários existentes de forma elegante
if st.session_state.lista_comentarios:
    st.write("---")
    st.subheader("Comentários Recentes:")
    for comentario in reversed(st.session_state.lista_comentarios):
        st.markdown(f"""
        <div style="background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #4B1E2F;">
            <strong>Nota: {comentario['nota']}/10</strong><br>
            {comentario['texto']}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# EXPORTAÇÃO
# ==================================================

st.header("08 • Exportação")

# Funções de exportação
@st.cache_data
def gerar_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(
        buffer,
        pagesize=letter
    )

    pdf.setTitle("Brandbook Açaí Vida")
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

@st.cache_data
def gerar_zip():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
        arquivos = [
            "Logos_01.png", "acai_01.png", "acai_02.png", "banner_01.png",
            "fundo_01.png", "fundo_02.png", "fundo_03.png", "fundo_04.png",
            "fundo_05.png", "gelato.png", "insta_01.png", "logo_01.png",
            "mirtilo.png", "montserrat.png", "out_01.png", "poppins.png",
            "sorvete_01.png", "sorvete_02.png", "uniforme_01.png",
        ]

        for f in arquivos:
            if Path(f).exists():
                z.write(f)

    buffer.seek(0)
    return buffer

# Usa colunas para os botões de download
col1, col2 = st.columns(2)

with col1:
    st.download_button("📄 Baixar PDF", gerar_pdf(), "brandbook.pdf", "application/pdf")

with col2:
    st.download_button("📦 Baixar KIT (.zip)", gerar_zip(), "kit_acai.zip", "application/zip")

st.markdown("<br><br>", unsafe_allow_html=True)

# ==================================================
# RODAPÉ
# ==================================================

st.markdown("""
<div style="text-align: center; color: #666; font-size: 14px; padding-bottom: 20px;">
    Açaí Vida • Brandbook Acadêmico • 2026
</div>
""", unsafe_allow_html=True)

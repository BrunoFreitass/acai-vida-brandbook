import streamlit as st
from pathlib import Path
import io
import zipfile
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# ==================================================
# CONFIGURAÇÃO DA PÁGINA (Deve ser o primeiro comando)
# ==================================================
st.set_page_config(
    page_title="Açaí Vida | Brandbook",
    page_icon="logo_01.png",
    layout="wide",
    initial_sidebar_state="collapsed"
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
# 🎨 CSS CUSTOMIZADO (ESTILO BEHANCE - SEM EMENDAS)
# ==================================================
st.markdown("""
<link rel="stylesheet" href="https://fonts.cdnfonts.com/css/armonioso">
<style>
/* Remove as margens laterais e superiores do app */
.block-container {
    max-width: 100% !important;
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
}

/* Zera o espaço vertical padrão entre os blocos do Streamlit */
[data-testid="stVerticalBlock"] > div {
    padding-bottom: 0rem !important;
    margin-bottom: 0rem !important;
}

/* Remove o espaçamento das colunas para conectar imagens horizontais */
[data-testid="stHorizontalBlock"] {
    gap: 0rem !important;
}

/* Força as imagens a preencherem o bloco sem cantos arredondados ou lacunas */
img {
    width: 100% !important;
    border-radius: 0px !important;
    margin: 0px !important;
    padding: 0px !important;
    display: block !important;
}

/* Containers de conteúdo textual (adiciona margem interna apenas onde há texto) */
.conteudo-texto {
    padding: 40px 80px;
    background-color: #FDFBFE;
    color: #333333;
}

.title {
    font-family: 'Armonioso', cursive;
    font-size: 72px;
    color: #4B1E2F;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 22px;
    color: #666;
    margin-bottom: 20px;
}

/* Estilização da seção de comentários interativos */
.secao-interativa {
    background-color: #2D0B48;
    color: white;
    padding: 60px 80px;
}
</style>
""", unsafe_allow_html=True)

# Função para renderizar os banners de fundo sem quebras
def banner(imagem):
    if Path(imagem).exists():
        with open(imagem, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
        ext = Path(imagem).suffix.replace(".", "").lower()
        mime = f"image/{ext}" if ext in ["png", "jpg", "jpeg"] else "image/png"
        
        st.markdown(
            f'<img src="data:{mime};base64,{data}" style="width:100%; max-height:400px; object-fit:cover;">',
            unsafe_allow_html=True
        )

# Inicializa o histórico de comentários na sessão para não sumir ao interagir
if "historico_comentarios" not in st.session_state:
    st.session_state.historico_comentarios = []

# ==================================================
# CAPA (Estilo Behance - Imagem Completa)
# ==================================================
banner(FUNDO_CAPA)

st.markdown("""
<div class="conteudo-texto">
    <div class="title">AÇAÍ VIDA</div>
    <div class="subtitle">Brandbook Acadêmico • Identidade Visual</div>
    <p><b>Cliente:</b> Açaí Vida<br>
    <b>Ano:</b> 2026<br>
    <b>Projeto de Extensão:</b> Brandbook</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# 01 • IDENTIDADE VISUAL
# ==================================================
banner(FUNDO_IDENTIDADE)

st.markdown('<div class="conteudo-texto"><h2>01 • Identidade Visual</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if Path("logo_01.png").exists():
        st.image("logo_01.png", use_container_width=True)
with col2:
    if Path("Logos_01.png").exists():
        st.image("Logos_01.png", use_container_width=True)

# ==================================================
# 02 • CONCEITO DA MARCA
# ==================================================
banner(FUNDO_CONCEITO)

st.markdown("""
<div class="conteudo-texto">
    <h2>02 • Conceito da Marca</h2>
    <p>A Açaí Vida representa energia, cultura amazônica e identidade visual forte. 
    O design foi planejado para transmitir o frescor do fruto combinado com a vibração urbana e tropical moderna.</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# 03 • TIPOGRAFIA
# ==================================================
banner(FUNDO_TIPOGRAFIA)

st.markdown('<div class="conteudo-texto"><h2>03 • Tipografia</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    if Path("gelato.png").exists():
        st.image("gelato.png", use_container_width=True)
    st.markdown("<div style='padding: 0 20px;'><p><b>Gelato Luxe</b><br>Fonte principal da marca</p></div>", unsafe_allow_html=True)
with col2:
    if Path("poppins.png").exists():
        st.image("poppins.png", use_container_width=True)
    st.markdown("<div style='padding: 0 20px;'><p><b>Poppins Bold</b><br>Fonte secundária</p></div>", unsafe_allow_html=True)
with col3:
    if Path("montserrat.png").exists():
        st.image("montserrat.png", use_container_width=True)
    st.markdown("<div style='padding: 0 20px;'><p><b>Montserrat Regular</b><br>Fonte de apoio</p></div>", unsafe_allow_html=True)

# ==================================================
# 04 • PALETA DE CORES
# ==================================================
banner(FUNDO_PALETA)

st.markdown('<div class="conteudo-texto"><h2>04 • Paleta de Cores</h2></div>', unsafe_allow_html=True)

cores = [
    ("Roxo Açaí", "#5B2A8C"),
    ("Verde Energia", "#D2D914"),
    ("Amarelo Tropical", "#F2CB05"),
    ("Branco Neve", "#FDFBFE"),
    ("Roxo Profundo", "#2D0B48"),
]

# Grid de cores sem margens agressivas
cols_cores = st.columns(5)
for i, (nome, cor) in enumerate(cores):
    with cols_cores[i]:
        text_color = "black" if cor.upper() == "#FDFBFE" else "white"
        st.markdown(f"""
        <div style="background:{cor}; padding:40px 20px; text-align:center; font-weight:bold; color:{text_color};">
            {nome}<br>{cor}
        </div>
        """, unsafe_allow_html=True)

# ==================================================
# 05 • APLICAÇÃO DA MARCA
# ==================================================
banner(FUNDO_APLICACOES)

st.markdown('<div class="conteudo-texto"><h2>05 • Aplicação da Marca</h2></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("<div style='padding:20px;'><h3>🥤 Copo Comercial</h3></div>", unsafe_allow_html=True)
    if Path("acai_01.png").exists(): st.image("acai_01.png", use_container_width=True)
    if Path("acai_02.png").exists(): st.image("acai_02.png", use_container_width=True)
with col2:
    st.markdown("<div style='padding:20px;'><h3>🍨 Taça Premium</h3></div>", unsafe_allow_html=True)
    if Path("sorvete_02.png").exists(): st.image("sorvete_02.png", use_container_width=True)
    if Path("banner_01.png").exists(): st.image("banner_01.png", use_container_width=True)

# ==================================================
# 06 • MOCKUPS
# ==================================================
banner(FUNDO_MOCKUPS)

st.markdown('<div class="conteudo-texto"><h2>06 • Mockups</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    if Path("out_01.png").exists(): st.image("out_01.png", caption="Outdoor", use_container_width=True)
with col2:
    if Path("uniforme_01.png").exists(): st.image("uniforme_01.png", caption="Uniforme", use_container_width=True)
with col3:
    if Path("insta_01.png").exists(): st.image("insta_01.png", caption="Instagram", use_container_width=True)

# ==================================================
# 07 • COMENTÁRIOS E AVALIAÇÕES (SISTEMA DE ENVIO)
# ==================================================
st.markdown('<div class="secao-interativa"><h2>07 • Feedback & Avaliações</h2>', unsafe_allow_html=True)

# Layout de colunas para o formulário de envio
col_form, col_lista = st.columns([1, 1])

with col_form:
    st.subheader("Deixe seu Comentário")
    nome_usuario = st.text_input("Seu Nome", placeholder="Ex: Professor Silva", key="input_nome")
    comentario_texto = st.text_area("Observações ou sugestões do projeto...", height=120, key="input_texto")
    
    col_sub1, col_sub2 = st.columns(2)
    with col_sub1:
        nota = st.slider("Avaliação Geral", 1, 10, 10)
    with col_sub2:
        st.write("") # Espaçador
        botao_enviar = st.button("Enviar Avaliação")

    if botao_enviar:
        if nome_usuario and comentario_texto:
            # Salva no Session State para não perder os dados na recarga do Streamlit
            st.session_state.historico_comentarios.append({
                "nome": nome_usuario,
                "texto": comentario_texto,
                "nota": nota
            })
            st.success("Avaliação enviada com sucesso!")
        else:
            st.error("Por favor, preencha o seu nome e o comentário.")

with col_lista:
    st.subheader("Comentários Recentes")
    if not st.session_state.historico_comentarios:
        st.info("Nenhum comentário enviado ainda. Seja o primeiro!")
    else:
        for c in reversed(st.session_state.historico_comentarios):
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-bottom: 10px;">
                <span style="font-weight: bold; color: #D2D914;">★ {c['nota']}/10 - {c['nome']}</span>
                <p style="margin-top: 5px; margin-bottom: 0px; color: #FDFBFE;">{c['texto']}</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# 08 • EXPORTAÇÃO
# ==================================================
st.markdown('<div class="conteudo-texto"><h2>08 • Exportação</h2></div>', unsafe_allow_html=True)

def gerar_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Brandbook Açaí Vida")
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(160, 760, "AÇAÍ VIDA")
    pdf.setFont("Helvetica", 14)
    pdf.drawString(150, 735, "Brandbook Acadêmico")
    if Path("logo_01.png").exists():
        pdf.drawImage("logo_01.png", 220, 520, width=160, height=160, preserveAspectRatio=True)
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer

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

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.download_button("📄 Baixar PDF", gerar_pdf(), "brandbook.pdf", "application/pdf", use_container_width=True)
with col_btn2:
    st.download_button("📦 Baixar KIT (.zip)", gerar_zip(), "kit_acai.zip", "application/zip", use_container_width=True)

# ==================================================
# RODAPÉ
# ==================================================
st.markdown("""
<div style="text-align: center; padding: 40px; background-color: #1A1A1A; color: #666666; font-size: 14px;">
    Açaí Vida • Brandbook Acadêmico • 2026
</div>
""", unsafe_allow_html=True)

import streamlit as st
from pathlib import Path
import io
import zipfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import qrcode

st.page_link("pages/cardapio.py", label="🍕 Ir para o Cardápio (Fazer Pedido)", icon="🥤")

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================
st.set_page_config(
    page_title="Açaí Vida | Brandbook",
    page_icon="logo_01.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 📥 INICIALIZAÇÃO DA LISTA DE PEDIDOS COMPARTILHADA
if 'pedidos_realizados' not in st.session_state:
    st.session_state.pedidos_realizados = []

# ==================================================
# 🛠️ FUNÇÕES DE SUPORTE
# ==================================================
def gerar_qr_instagram():
    qr = qrcode.make("https://www.instagram.com/acai_vida")
    qr.save("qr_instagram.png")
    return "qr_instagram.png"

@st.cache_data
def gerar_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Brandbook Açaí Vida")

    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(160, 760, "AÇAÍ VIDA")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(150, 735, "Brandbook Acadêmico")

    if Path("logo_final_01.png").exists():
        pdf.drawImage(
            "logo_final_01.png",
            80,
            650,
            width=450,
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
            "sorvete_01.png", "sorvete_02.png", "uniforme_01.png", "acai_fundo_amarelo_01.png",
            "acai_fundo_amarelo_02.png", "acai_fundo_amarelo_03.png", "acai_fundo_preto_01.png",
            "acai_fundo_roxo_01.png", "acais_fundo_amarelo_01.png", "soverte_verde_01.png",
            "sovertes_fundo_amarelo_01.png"
        ]
        for f in arquivos:
            if Path(f).exists():
                z.write(f)
    buffer.seek(0)
    return buffer

# ==================================================
# 🎨 CSS CUSTOMIZADO
# ==================================================
st.markdown('<link rel="stylesheet" href="https://fonts.cdnfonts.com/css/armonioso">', unsafe_allow_html=True)

css_behance = (
    "<style>"
    ".main .block-container {max-width: 100% !important; padding-top: 0rem !important; padding-bottom: 0rem !important; padding-left: 0rem !important; padding-right: 0rem !important;}"
    "[data-testid='stHorizontalBlock'] {gap: 0rem !important;}"
    ".conteudo-texto {padding: 60px 80px; background-color: transparent;}"
    ".title {font-family: 'Armonioso', cursive; font-size: 72px; color: white;text-shadow: 0px 2px 12px rgba(0,0,0,0.35);}"
    ".subtitle {font-size: 22px; color: #666;}"
    ".secao-interativa {background-color: #f7f7f7; padding: 60px 80px; border-radius: 16px; margin-bottom: 20px; color: #333333;}"
    ".aplicacao-container [data-testid='stImage'] img {height: 400px !important; width: 100% !important; object-fit: cover !important; border-radius: 12px !important; margin-bottom: 15px !important;}"
    ".mockup-container [data-testid='stImage'] img {height: 400px !important; width: 100% !important; object-fit: cover !important; border-radius: 12px !important; margin-bottom: 10px !important;}"
    "</style>"
)

st.markdown(css_behance, unsafe_allow_html=True)

# ==================================================
# CAPA
# ==================================================
col1, col2, col3 = st.columns([0.5, 3, 0.5]) # Ajustado o espaçamento para centralizar a logo maior

with col2:
    if Path("logo_02.png").exists():
        st.image("logo_02.png", width=700) # Logo ampliada de 500 para 700

st.markdown("""
<div style="text-align:center; color:white; font-size:20px; line-height:1.8;">
    <strong>Brandbook Acadêmico • Identidade Visual</strong>
    <br><br>
    Cliente: Açaí Vida<br>
    Ano: 2026<br>
    Projeto de Extensão: Brandbook
</div>
""", unsafe_allow_html=True)
    
# ==================================================
# 01 • IDENTIDADE VISUAL
# ==================================================
st.markdown("---")

st.markdown("""
<div class='conteudo-texto'>
    <h2>01 • Identidade Visual</h2>
    <p>A identidade visual da Açaí Vida foi desenvolvida para transmitir energia, naturalidade e conexão com a cultura amazônica.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Logo Principal")
    if Path("logo_01.png").exists():
        st.image("logo_01.png", use_container_width=True)

with col2:
    st.subheader("Versões da Marca")
    if Path("Logos_01.png").exists():
        st.image("Logos_01.png", use_container_width=True)

# ==================================================
# 02 • CONCEITO DA MARCA
# ==================================================
st.markdown("---")

st.markdown("""
<div class='conteudo-texto'>
    <h2>02 • Conceito da Marca</h2>
    <p>A Açaí Vida representa energia, bem-estar e vitalidade. Sua identidade busca unir elements da cultura amazônica com uma linguagem contemporânea, criando uma marca jovem, forte e memorável.</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# 03 • TIPOGRAFIA
# ==================================================
st.markdown("---")

st.markdown("""
<div class='conteudo-texto'>
    <h2>03 • Tipografia</h2>
    <p>A seleção tipográfica busca equilibrar personalidade, modernidade e excelente legibilidade em ambientes digitais e impressos.</p>
    <ul>
        <li><strong>Gelato Luxe:</strong> utilizada como tipografia principal por transmitir exclusividade, movimento e personalidade.</li>
        <li><strong>Poppins Bold:</strong> empregada em títulos e chamadas por sua alta legibilidade.</li>
        <li><strong>Montserrat Regular:</strong> aplicada em textos corridos devido à sua clareza e conforto de leitura.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Gelato Luxe")
    if Path("gelato.png").exists():
        st.image("gelato.png", use_container_width=True)
    st.caption("Tipografia principal da marca")

with col2:
    st.subheader("Poppins Bold")
    if Path("poppins.png").exists():
        st.image("poppins.png", use_container_width=True)
    st.caption("Tipografia complementar")

with col3:
    st.subheader("Montserrat Regular")
    if Path("montserrat.png").exists():
        st.image("montserrat.png", use_container_width=True)
    st.caption("Tipografia de apoio")
    
# ==================================================
# 04 • PALETA DE CORES & REFERÊNCIA DE MARCA
# ==================================================
st.markdown("---")

st.markdown("""
<div class='conteudo-texto'>
    <h2>04 • Paleta de Cores</h2>
    <p>A paleta cromática da Açaí Vida foi construída para transmitir energia, vitalidade, natureza e conexão com a Amazônia. Cada cor possui uma função estratégica dentro della identidade visual.</p>
    <ul>
        <li><strong>Roxo Açaí:</strong> representa o fruto principal da marca, autenticidade e personalidade.</li>
        <li><strong>Verde Energia:</strong> transmite saúde, frescor e ingredientes naturais.</li>
        <li><strong>Amarelo Tropical:</strong> remete ao clima brasileiro, alegria e energia.</li>
        <li><strong>Branco:</strong> proporciona equilíbrio visual e legibilidade.</li>
        <li><strong>Roxo Profundo:</strong> reforça sofisticação e contraste.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Bloco de Cores em 5 colunas
cores = [
    ("Roxo Açaí", "#5B2A8C"),
    ("Verde Energia", "#D2D914"),
    ("Amarelo Tropical", "#F2CB05"),
    ("Branco Neve", "#FDFBFE"),
    ("Roxo Profundo", "#2D0B48"),
]

cols_cores = st.columns(5)

for i, (nome, cor) in enumerate(cores):
    with cols_cores[i]:
        text_color = "black" if cor.upper() == "#FDFBFE" else "white"
        st.markdown(
            f"""
            <div style="background:{cor}; padding:35px 10px; border-radius:12px; text-align:center; font-weight:bold; color:{text_color}; margin-bottom:20px;">
                {nome}<br>{cor}
            </div>
            """,
            unsafe_allow_html=True
        )

# INCLUSÃO SOLICITADA: Logo Principal integrada às seções de Tipografia e Cores para melhor referência conceitual
st.markdown("<br>", unsafe_allow_html=True)
col_ref1, col_ref2 = st.columns([1.2, 2])

with col_ref1:
    st.markdown("""
    <div style="padding-top: 20px;">
        <h4>Aplicação Cromática e Tipográfica Integrada</h4>
        <p style="color: #666; font-size: 14px;">
            Ao lado, observa-se como o <strong>Roxo Açaí</strong> e o <strong>Verde Energia</strong> interagem diretamente com os contornos fluidos desenhados a partir da tipografia institucional. Esta combinação garante consistência e contraste tanto em fundos claros quanto escuros.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_ref2:
    if Path("logo_01.png").exists():
        st.image("logo_01.png", caption="Referência Visual: Logo Principal aplicada sobre fundo neutro", width=450)

st.markdown("---")

# ==================================================
# 05 • APLICAÇÃO DA MARCA
# ==================================================
st.markdown("<div class='conteudo-texto'><h2>05 • Aplicação da Marca</h2></div>", unsafe_allow_html=True)

st.markdown('<div class="aplicacao-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🥤 Copo Comercial")
    if Path("acai_01.png").exists():
        st.image("acai_01.png", use_container_width=True)
    if Path("acai_02.png").exists():
        st.image("acai_02.png", use_container_width=True)
    if Path("acai_fundo_amarelo_01.png").exists():
        st.image("acai_fundo_amarelo_01.png", use_container_width=True)
    if Path("acai_fundo_amarelo_02.png").exists():
        st.image("acai_fundo_amarelo_02.png", use_container_width=True)
    if Path("acai_fundo_amarelo_03.png").exists():
        st.image("acai_fundo_amarelo_03.png", use_container_width=True)

with col2:
    st.subheader("🍨 Taça Premium")
    if Path("sorvete_02.png").exists():
        st.image("sorvete_02.png", use_container_width=True)
    if Path("banner_01.png").exists():
        st.image("banner_01.png", use_container_width=True)
    if Path("sorvete_01.png").exists():
        st.image("sorvete_01.png", use_container_width=True)
    if Path("sorvete_02.png").exists():
        st.image("sorvete_02.png", use_container_width=True)
    if Path("sovertes_fundo_amarelo_01.png").exists():
        st.image("sovertes_fundo_amarelo_01.png", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ==================================================
# 06 • MOCKUPS
# ==================================================
st.markdown("<div class='conteudo-texto'><h2>06 • Mockups</h2></div>", unsafe_allow_html=True)

st.markdown('<div class="mockup-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if Path("out_01.png").exists():
        st.image("out_01.png", caption="Outdoor", use_container_width=True)

with col2:
    if Path("uniforme_01.png").exists():
        st.image("uniforme_01.png", caption="Uniforme", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    if Path("insta_01.png").exists():
        st.image("insta_01.png", caption="Instagram", use_container_width=True)

with col4:
    if Path("cardapio_01.png").exists():
        st.image("cardapio_01.png", caption="Cardápio", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

st.subheader("📱 Instagram")

arquivo_qr = gerar_qr_instagram()

col1_qr, col2_qr = st.columns([1,2])

with col1_qr:
    st.image(arquivo_qr)

with col2_qr:
    st.markdown("Escaneie o QR Code para acessar o perfil oficial da Açaí Vida.")
        
# ==================================================
# 📥 PAINEL DE PEDIDOS EM TEMPO REAL
# ==================================================
st.markdown("<div class='secao-interativa'><h2>📥 Pedidos Recebidos (Painel Geral)</h2></div>", unsafe_allow_html=True)

if not st.session_state.pedidos_realizados:
    st.info("Nenhum pedido recebido até o momento. Aguardando clientes realizarem pedidos na página do Cardápio...")
else:
    for idx, pedido in enumerate(reversed(st.session_state.pedidos_realizados)):
        st.markdown(f"""
        <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #D2D914; color: #333333; box-shadow: 0px 2px 4px rgba(0,0,0,0.05);">
            <h4 style="margin:0; color:#5B2A8C;">🛒 Pedido #{len(st.session_state.pedidos_realizados) - idx} - Cliente: {pedido['cliente']}</h4>
            <p style="margin: 5px 0;"><strong>Itens:</strong> {pedido['item']}</p>
            <p style="margin: 5px 0;"><strong>Observações:</strong> {pedido['obs']}</p>
            <span style="font-size:12px; color:#666;">Status: 🟡 Recebido pela Cozinha</span>
        </div>
        """, unsafe_allow_html=True)

# ==================================================
# 07 • COMENTÁRIOS E AVALIAÇÕES
# ==================================================
st.markdown("<div class='secao-interativa'><h2>07 • Feedback & Comentários</h2></div>", unsafe_allow_html=True)

if 'lista_comentarios' not in st.session_state:
    st.session_state.lista_comentarios = []

col_input, col_nota = st.columns([2, 1])

with col_input:
    comentario_texto = st.text_area(
        "Deixe suas observações",
        height=120,
        placeholder="Digite observações, sugestões ou avaliações do projeto...",
        key="campo_comentario"
    )
    botao_enviar = st.button("Enviar Comentário")

with col_nota:
    avaliacao_nota = st.slider(
        "Avaliação Geral",
        min_value=1,
        max_value=10,
        value=10,
        step=1,
        key="campo_avaliacao"
    )
    st.metric("Sua Nota", f"{avaliacao_nota}/10")

if botao_enviar:
    if st.session_state.campo_comentario.strip():
        st.session_state.lista_comentarios.append({
            'texto': st.session_state.campo_comentario.strip(),
            'nota': st.session_state.campo_avaliacao
        })
        st.rerun()
    else:
        st.warning("O campo de comentário não pode estar vazio.")

if st.session_state.lista_comentarios:
    st.markdown("<div style='padding: 0 20px;'><h3>Comentários Recentes:</h3></div>", unsafe_allow_html=True)
    for comentario in reversed(st.session_state.lista_comentarios):
        st.markdown(f"""
        <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; margin: 10px 20px 15px 20px; border-left: 5px solid #4B1E2F; color: #333333; box-shadow: 0px 2px 4px rgba(0,0,0,0.05);">
            <strong>Nota: {comentario['nota']}/10</strong><br>
            {comentario['texto']}
        </div>
        """, unsafe_allow_html=True)

# ==================================================
# 08 • EXPORTAÇÃO
# ==================================================
st.markdown("<div class='conteudo-texto'><h2>08 • Exportação</h2></div>", unsafe_allow_html=True)

col_dl1, col_dl2 = st.columns(2)
with col_dl1:
    st.download_button("📄 Baixar PDF", gerar_pdf(), "brandbook.pdf", "application/pdf", use_container_width=True)
with col_dl2:
    st.download_button("📦 Baixar KIT (.zip)", gerar_zip(), "kit_acai.zip", "application/zip", use_container_width=True)

# ==================================================
# RODAPÉ
# ==================================================
st.markdown("""
<div style="text-align: center; color: #666; font-size: 14px; padding: 40px 0px 20px 0px;">
    Açaí Vida • Brandbook Acadêmico • 2026
</div>
""", unsafe_allow_html=True)

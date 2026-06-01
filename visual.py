# python
import streamlit as st
from pathlib import Path

# ==================================================
# CONFIGURAÇÃO
# ==================================================

st.set_page_config(
    page_title="Açaí Vida | Brandbook",
    page_icon="editaveis/logo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
    <style>
        .header {
            text-align: center;
            padding: 30px 0 10px 0;
        }

        .logo {
            width: 150px;
            margin-bottom: 10px;
        }

        .title {
            font-size: 50px;
            font-weight: 900;
            color: #4B1E2F;
            margin: 0;
        }

        .subtitle {
            font-size: 16px;
            color: #777;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA (LOGO + NOME CENTRALIZADOS)
# ==================================================

logo = Path("editaveis/logo.png")

st.markdown("<div class='header'>", unsafe_allow_html=True)

if logo.exists():
    st.image(str(logo), width=150)

st.markdown("""
<div class="title">AÇAÍ VIDA</div>
<div class="subtitle">Projeto Acadêmico de Branding e Identidade Visual</div>
</div>
""", unsafe_allow_html=True)

st.caption("Instituto Federal de Roraima • Projeto Acadêmico • 2026")

st.markdown("""
### Brandbook Acadêmico

Desenvolvimento da identidade visual da marca Açaí Vida,
incluindo conceito, tipografia, paleta cromática e aplicações visuais.
""")

st.divider()

# ==================================================
# FUNÇÃO TÍTULO
# ==================================================

def titulo(numero, texto):
    st.markdown(f"### {numero}")
    st.header(texto)

# ==================================================
# SISTEMA DE LOGOS + CORES LADO A LADO
# ==================================================

st.markdown("## Identidade Visual da Marca")

logo_principal = Path("editaveis/logo.png")
logos_diversas = Path("editaveis/logos_diversas.png")

col1, col2 = st.columns([2, 2])

# -------------------------
# LOGO PRINCIPAL
# -------------------------
with col1:

    st.subheader("Logo Principal")

    if logo_principal.exists():
        st.image(str(logo_principal), width=250)
    else:
        st.warning("Insira a logo principal em: editaveis/logo.png")

# -------------------------
# CORES (AO LADO DA LOGO)
# -------------------------
with col2:

    st.subheader("Identificação das Cores")

    cores = [
        ("Roxo Açaí", "#5B2A8C"),
        ("Verde Energia", "#D2D914"),
        ("Amarelo Tropical", "#F2CB05"),
        ("Branco Neve", "#FDFBFE")
    ]

    for nome, cor in cores:
        st.color_picker(nome, cor, disabled=True)
        st.caption(cor)

st.divider()

# ==================================================
# LOGOS DIVERSAS (1 IMAGEM SÓ)
# ==================================================

titulo("02", "Logos diversas")

st.write("""
Esta seção reúne as variações da marca em diferentes aplicações.
""")

if logos_diversas.exists():
    st.image(str(logos_diversas), width=600)
else:
    st.warning("Crie a imagem: editaveis/logos.png (negativa + horizontal + ícone)")

st.divider()

# ==================================================
# CONCEITO
# ==================================================

titulo("03", "Conceito da Marca")

st.write("""
A Açaí Vida foi criada para proporcionar uma experiência
gastronômica marcante, unindo a energia do açaí à refrescância
dos sorvetes.

Sua identidade visual foi construída para transmitir vitalidade,
alegria, acolhimento e conexão com a cultura amazônica.
""")

st.divider()

# ==================================================
# PALETA DE CORES (DETALHADA)
# ==================================================

titulo("04", "Paleta de Cores")

cores = [

    ("Roxo Açaí", "#5B2A8C"),
    ("Roxo Noturno", "#4B2F73"),
    ("Lavanda Suave", "#A999BF"),
    ("Verde Energia", "#D2D914"),
    ("Amarelo Tropical", "#F2CB05"),
    ("Branco Neve", "#FDFBFE"),
    ("Verde Vitalidade", "#B7CE0E"),
    ("Roxo Profundo", "#2D0B48"),
    ("Lilás Premium", "#BC7CD2")
]

cols = st.columns(3)

for i, (nome, cor) in enumerate(cores):

    with cols[i % 3]:
        st.color_picker(nome, cor, disabled=True)
        st.caption(cor)

st.divider()

# ==================================================
# TIPOGRAFIA
# ==================================================

titulo("05", "Tipografia")

tipografia_logo = Path("editaveis/gelato.png")
tipografia_poppins = Path("editaveis/poppins.png")
tipografia_montserrat = Path("editaveis/montserrat.png")

st.subheader("Fonte Principal — Gelato Luxe")

col1, col2 = st.columns([2,1])

with col1:
    if tipografia_logo.exists():
        st.image(str(tipografia_logo))
    else:
        st.warning("editaveis/gelato.png não encontrada")

with col2:
    st.write("Uso principal da marca e identidade visual.")

st.divider()

st.subheader("Fonte Secundária — Poppins")

col1, col2 = st.columns([2,1])

with col1:
    if tipografia_poppins.exists():
        st.image(str(tipografia_poppins))
    else:
        st.warning("editaveis/poppins.png não encontrada")

with col2:
    st.write("Títulos e comunicação visual.")

st.divider()

st.subheader("Fonte de Apoio — Montserrat")

col1, col2 = st.columns([2,1])

with col1:
    if tipografia_montserrat.exists():
        st.image(str(tipografia_montserrat))
    else:
        st.warning("editaveis/montserrat.png não encontrada")

with col2:
    st.write("Textos e informações gerais.")

st.divider()

# ==================================================
# APLICAÇÃO DA MARCA
# ==================================================

titulo("06", "Aplicação da Marca")

imagem_copo = Path("editaveis/açai.01.png")
imagem_taca = Path("editaveis/açai.02.png")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🥤 Copo Comercial")
    if imagem_copo.exists():
        st.image(str(imagem_copo))

with col2:
    st.subheader("🍨 Taça Premium")
    if imagem_taca.exists():
        st.image(str(imagem_taca))

st.divider()

# ==================================================
# MOCKUPS
# ==================================================

titulo("07", "Mockups")

mockup = Path("editaveis/acai.03.png")

if mockup.exists():
    st.image(str(mockup))
else:
    st.info("Adicione mockups em editaveis/")

st.divider()

# ==================================================
# RESULTADO FINAL
# ==================================================

titulo("08", "Resultado Final")

st.success("""
A identidade visual da Açaí Vida foi construída para
transmitir energia, cultura e autenticidade amazônica.
""")

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("""
Açaí Vida • Brandbook Acadêmico • 2026
Bruno Freitas
""")

# python
import streamlit as st
from pathlib import Path

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
# CSS (APENAS VISUAL, SEM QUEBRAR LAYOUT)
# ==================================================

st.markdown("""
    <style>
        .title {
            font-size: 52px;
            font-weight: 900;
            color: #4B1E2F;
            text-align: center;
            margin-top: 10px;
        }

        .subtitle {
            font-size: 16px;
            color: #777;
            text-align: center;
            margin-bottom: 20px;
        }

        .centered {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# ==================================================
# CAPA (LOGO + NOME CENTRALIZADO CORRETAMENTE)
# ==================================================

logo = Path("editaveis/logo.png")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if logo.exists():
        st.image(str(logo), width=160)

st.markdown('<div class="title">AÇAÍ VIDA</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Projeto Acadêmico de Branding e Identidade Visual</div>', unsafe_allow_html=True)

st.caption("Instituto Federal de Roraima • Projeto Acadêmico • 2026")

st.divider()

# ==================================================
# FUNÇÃO TÍTULO
# ==================================================

def titulo(numero, texto):
    st.markdown(f"### {numero}")
    st.header(texto)

# ==================================================
# IDENTIDADE VISUAL (LOGO + CORES LADO A LADO)
# ==================================================

st.markdown("## Identidade Visual da Marca")

logo_principal = Path("editaveis/logo.png")

col1, col2 = st.columns([2, 2])

with col1:

    st.subheader("Logo Principal")

    if logo_principal.exists():
        st.image(str(logo_principal), width=250)
    else:
        st.warning("Insira: editaveis/logo.png")

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
# LOGOS DIVERSAS
# ==================================================

titulo("02", "Logos diversas")

logos_diversas = Path("editaveis/logos_diversas.png")

st.write("Variações da identidade visual da marca.")

if logos_diversas.exists():
    st.image(str(logos_diversas), width=600)
else:
    st.warning("Crie: editaveis/logos_diversas.png")

st.divider()

# ==================================================
# CONCEITO
# ==================================================

titulo("03", "Conceito da Marca")

st.write("""
A Açaí Vida foi criada para proporcionar uma experiência
gastronômica marcante, unindo a energia do açaí à refrescância
dos sorvetes.
""")

st.divider()

# ==================================================
# PALETA DE CORES
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

st.write("Identidade tipográfica da marca.")

st.divider()

# ==================================================
# APLICAÇÃO
# ==================================================

titulo("06", "Aplicação da Marca")

st.write("Aplicações da identidade visual em produtos e materiais.")

st.divider()

# ==================================================
# MOCKUPS
# ==================================================

titulo("07", "Mockups")

st.write("Visualização da marca em contextos reais.")

st.divider()

# ==================================================
# RESULTADO FINAL
# ==================================================

titulo("08", "Resultado Final")

st.success("""
A identidade visual da Açaí Vida transmite energia,
cultura e autenticidade amazônica.
""")

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("""
Açaí Vida • Brandbook Acadêmico • 2026
Bruno Freitas
""")

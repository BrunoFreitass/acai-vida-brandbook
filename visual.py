#python
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
# FUNÇÃO DE TÍTULO
# ==================================================

def titulo(numero, texto):
    st.markdown(f"### {numero}")
    st.header(texto)

# ==================================================
# LOGO
# ==================================================

logo = Path("mirtilo.png")

col1, col2, col3 = st.columns([2,1,2])

with col2:
    if logo.exists():
        st.image(str(logo), width=180)

# ==================================================
# CAPA
# ==================================================

st.markdown(
    """
    <div style='text-align:center;'>

    <h1>AÇAÍ VIDA</h1>

    <h3>
    Projeto Acadêmico de Branding e Identidade Visual
    </h3>

    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "Instituto Federal de Roraima • Projeto Acadêmico • 2026"
)

st.markdown("""
### Brandbook Acadêmico

Desenvolvimento da identidade visual da marca Açaí Vida,
incluindo conceito, tipografia, paleta cromática e aplicações visuais.
""")

st.divider()

# ==================================================
# MÉTRICAS
# ==================================================

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Cores da Marca", "9")

with m2:
    st.metric("Aplicações", "4")

with m3:
    st.metric("Ano", "2026")

st.divider()

# ==================================================
# CONCEITO
# ==================================================

titulo("01", "Conceito da Marca")

st.write("""
A Açaí Vida foi criada para proporcionar uma experiência
gastronômica marcante, unindo a energia do açaí à refrescância
dos sorvetes.

Sua identidade visual foi construída para transmitir vitalidade,
alegria, acolhimento e conexão com a cultura amazônica.
""")

st.divider()

# ==================================================
# PALETA DE CORES
# ==================================================

titulo("02", "Paleta de Cores")

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

        st.color_picker(
            nome,
            cor,
            disabled=True
        )

        st.caption(cor)

st.divider()

# ==================================================
# TIPOGRAFIA
# ==================================================

titulo("03", "Tipografia")

st.write("""
A identidade visual da Açaí Vida utiliza uma combinação
de tipografias que reforçam a personalidade da marca,
equilibrando criatividade, legibilidade e modernidade.
""")

tipografia_logo = Path("editaveis/gelato.png")
tipografia_poppins = Path("editaveis/poppins.png")
tipografia_montserrat = Path("editaveis/montserrat.png")

# GELATO

st.subheader("Fonte Principal — Gelato Luxe")

col1, col2 = st.columns([2,1])

with col1:

    if tipografia_logo.exists():
        st.image(str(tipografia_logo))

    else:
        st.warning("Imagem não encontrada: editaveis/gelato.png")

with col2:

    st.markdown("""
**Aplicação**

- Logo principal
- Destaques visuais
- Elementos de identidade

**Características**

- Criativa
- Orgânica
- Artesanal
- Memorável
""")

st.divider()

# POPPINS

st.subheader("Fonte Secundária — Poppins Bold")

col1, col2 = st.columns([2,1])

with col1:

    if tipografia_poppins.exists():
        st.image(str(tipografia_poppins))

    else:
        st.warning("Imagem não encontrada: editaveis/poppins.png")

with col2:

    st.markdown("""
**Aplicação**

- Títulos
- Chamadas
- Destaques

**Características**

- Moderna
- Limpa
- Forte
- Legível
""")

st.divider()

# MONTSERRAT

st.subheader("Fonte de Apoio — Montserrat Regular")

col1, col2 = st.columns([2,1])

with col1:

    if tipografia_montserrat.exists():
        st.image(str(tipografia_montserrat))

    else:
        st.warning("Imagem não encontrada: montserrat.png")

with col2:

    st.markdown("""
**Aplicação**

- Textos corridos
- Descrições
- Informações complementares

**Características**

- Elegante
- Neutra
- Profissional
- Versátil
""")

st.divider()

# ==================================================
# APLICAÇÃO DA MARCA
# ==================================================

imagem_copo = Path("editaveis/acai.02.png")
imagem_taca = Path("editaveis/açai.02.png")

titulo("04", "Aplicação da Marca")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🥤 Copo Comercial")

    if imagem_copo.exists():
        st.image(str(imagem_copo))

    else:
        st.warning("Imagem não encontrada: editaveis/acai.02.png")

with col2:

    st.subheader("🍨 Taça Premium")

    if imagem_taca.exists():
        st.image(str(imagem_taca))

    else:
        st.warning("Imagem não encontrada: editaveis/açai.02.png")

st.divider()

# ==================================================
# MOCKUPS
# ==================================================

titulo("05", "Galeria de Mockups")

aba1, aba2, aba3 = st.tabs(
    [
        "🥤 Copo",
        "👕 Uniforme",
        "📱 Instagram"
    ]
)

with aba1:

    mockup_copo = Path("editaveis/acai.03.png")

    if mockup_copo.exists():
        st.image(str(mockup_copo))

    else:
        st.info("Imagem não encontrada: editaveis/acai.03.png")

with aba2:

    uniforme = Path("editaveis/uniforme.png")

    if uniforme.exists():
        st.image(str(uniforme))

    else:
        st.info("Imagem não encontrada: editaveis/uniforme.png")

with aba3:

    instagram = Path("editaveis/insta.jpg")

    if instagram.exists():
        st.image(str(instagram))

    else:
        st.info("Imagem não encontrada: editaveis/insta.jpg")

st.divider()

# ==================================================
# SIGNIFICADO DAS CORES
# ==================================================

titulo("06", "Significado das Cores")

st.markdown("""
🟣 **Roxo Açaí**
Representa o produto principal da marca.

🟢 **Verde Energia**
Representa vitalidade, natureza e origem amazônica.

🟡 **Amarelo Tropical**
Representa alegria, calor e energia.

⚪ **Branco Neve**
Representa leveza e limpeza visual.
""")

st.divider()

# ==================================================
# RESULTADO FINAL
# ==================================================

titulo("07", "Resultado Final")

st.success("""
A identidade visual desenvolvida para a Açaí Vida
busca transmitir energia, sabor, acolhimento e
conexão com a cultura amazônica.

O sistema visual foi aplicado em embalagens,
mockups e peças digitais, criando uma marca
coerente e memorável.
""")

st.divider()

# ==================================================
# RODAPÉ
# ==================================================

st.caption("""
Açaí Vida • Projeto Acadêmico de Branding

Instituto Federal de Roraima

Bruno Freitas • 2026
""")

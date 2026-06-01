import streamlit as st

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Açaí Vida - Brandbook",
    page_icon="🍇",
    layout="centered"
)

# =========================
# CSS PERSONALIZADO
# =========================
st.markdown("""
    <style>
        .header {
            text-align: center;
            padding: 30px 0 10px 0;
        }

        .logo {
            width: 140px;
            height: auto;
            margin-bottom: 10px;
        }

        .title {
            font-size: 42px;
            font-weight: 700;
            color: #4B1E2F; /* ajuste conforme identidade visual */
            margin-top: 0;
        }

        .subtitle {
            font-size: 16px;
            color: #777;
            margin-top: -10px;
        }
    </style>
""", unsafe_allow_html=True)

# =========================
# HEADER (LOGO + NOME)
# =========================
st.markdown("""
<div class="header">
    <img src="editaveis/logo.png" class="logo">
    <div class="title">Açaí Vida</div>
    <div class="subtitle">Brandbook institucional</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CONTEÚDO DO BRAND BOOK
# =========================
st.divider()

st.header("Identidade Visual")

st.write("""
Aqui você pode inserir:
- Paleta de cores
- Tipografia
- Aplicações da marca
- Regras de uso da logo
""")

# =========================
# EXEMPLO DE CORES
# =========================
st.subheader("Cores principais")

col1, col2, col3 = st.columns(3)

with col1:
    st.color_picker("Cor primária", "#4B1E2F")

with col2:
    st.color_picker("Cor secundária", "#F4C542")

with col3:
    st.color_picker("Cor de apoio", "#FFFFFF")

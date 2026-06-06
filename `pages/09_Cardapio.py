python
import streamlit as st
from pathlib import Path

# Configuração da página do cliente
st.set_page_config(
    page_title="Açaí Vida | Faça seu Pedido", 
    page_icon="🥤", 
    layout="wide"
)

# Garante a conexão com a mesma lista de pedidos global da página principal
if 'pedidos_realizados' not in st.session_state:
    st.session_state.pedidos_realizados = []

# CSS Customizado para estilizar o Cardápio
st.markdown("""
<style>
    .cardapio-header { text-align: center; padding: 40px; background-color: #5B2A8C; color: white; border-radius: 12px; margin-bottom: 30px; }
    .produto-card { background-color: #ffffff; padding: 20px; border-radius: 12px; margin-bottom: 20px; border-left: 5px solid #D2D914; color: #333333; box-shadow: 0px 2px 5px rgba(0,0,0,0.05); }
    .preco { color: #5B2A8C; font-weight: bold; font-size: 18px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='cardapio-header'>
    <h1>🥤 Cardápio Digital • Açaí Vida</h1>
    <p>Faça seu pedido acadêmico simulado e veja-o aparecer em tempo real no Brandbook principal!</p>
</div>
""", unsafe_allow_html=True)

# Layout visual das opções do cardápio para o cliente ver antes de pedir
st.subheader("📋 Nossas Opções Disponíveis")
col_c1, col_c2 = st.columns(2)

with col_c1:
    st.markdown("""
    <div class='produto-card'>
        <h3>🥤 Copo Comercial Tradicional</h3>
        <p>Açaí cremoso batido na hora com direito a 3 acompanhamentos tradicionais à sua escolha.</p>
        <span class='preco'>R$ 15,00 (300ml) / R$ 22,00 (500ml)</span>
    </div>
    """, unsafe_allow_html=True)

with col_c2:
    st.markdown("""
    <div class='produto-card'>
        <h3>🍨 Taça Premium Sensação</h3>
        <p>Camadas estruturadas de creme de mirtilo artesanal, sorvete artesanal de creme e calda de açaí concentrada.</p>
        <span class='preco'>R$ 28,00</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Formulário para o envio dos pedidos
with st.form("formulario_pedido", clear_on_submit=True):
    st.subheader("📝 Formulário de Pedido")
    
    nome_cliente = st.text_input("Seu Nome Completo:", placeholder="Ex: João Silva")
    
    item_escolhido = st.selectbox(
        "Selecione o produto desejado:",
        [
            "Copo Comercial Tradicional (300ml) - R$ 15,00",
            "Copo Comercial Grande (500ml) - R$ 22,00",
            "Taça Premium Sensação (Mirtilo e Sorvete) - R$ 28,00",
            "Taça Tropical Completa (Açaí e Sorvete Verde/Amarelo) - R$ 32,00"
        ]
    )
    
    observacoes = st.text_area(
        "Observações ou Modificações:", 
        placeholder="Ex: Sem granola, leite em pó extra, adicionar banana..."
    )
    
    botao_enviar = st.form_submit_button("🚀 Enviar Pedido para o Painel")

if botao_enviar:
    if nome_cliente.strip() == "":
        st.error("Por favor, preencha o seu nome para realizar o pedido.")
    else:
        # Monta a estrutura do dicionário de pedido
        novo_pedido = {
            "cliente": nome_cliente,
            "item": item_escolhido,
            "obs": observacoes if observacoes.strip() else "Nenhuma alteração"
        }
        # Adiciona na lista compartilhada
        st.session_state.pedidos_realizados.append(novo_pedido)
        st.success(f"🎉 Pedido enviado com sucesso, {nome_cliente}! Volte para a página inicial (Brandbook) no menu lateral para visualizar no Painel Geral.")

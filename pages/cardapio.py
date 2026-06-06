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

# ==================================================
# INCLUSÃO 1: LOGO DA EMPRESA NO TOPO
# ==================================================
col_logo1, col_logo2, col_logo3 = st.columns([1, 1, 1])
with col_logo2:
    if Path("logo_01.png").exists():
        st.image("logo_02.png", width=450)

# Layout visual das opções do cardápio para o cliente ver antes de pedir
st.subheader("📋 Nossas Opções Disponíveis")
col_c1, col_c2 = st.columns(2)

with col_c1:
    st.markdown("""
    <div class='produto-card'>
        <h3>🥤 Copo Comercial Tradicional</h3>
        <p>Açaí cremoso batido na hora com direito até 3 Frutas, 3 Acompanhamento e 3 Caldas, à depender do tamanho do copo.</p>
        <span class='preco'>R$ 13,00 (250ml) / R$ 15,00 (300ml)</span>
        <span class='preco'>R$ 18,00 (400ml) / R$ 22,00 (500ml)</span>
        <span class='preco'>R$ 28,00 (700ml)</span>
    </div>
    """, unsafe_allow_html=True)

with col_c2:
    st.markdown("""
    <div class='produto-card'>
        <h3>🍨 Taça Premium Sensação</h3>
        <p>Sorvete artesanal de creme e calda de Açaí, Chocolate, Morango. Consulte Disponibilidade e Valores</p>
        <span class='preco'>R$ 00,00</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Formulário para o envio dos pedidos
with st.form("formulario_pedido", clear_on_submit=True):
    st.subheader("📝 Formulário de Pedido")
    
    nome_cliente = st.text_input("Seu Nome Completo:", placeholder="Ex: Bruno Freitas")
    
    item_escolhido = st.selectbox(
        "Selecione o produto desejado:",
        [
            "Copo Açaí (250ml) - R$ 13,00",
            "Copo Açaí (300ml) - R$ 15,00",
            "Copo Açaí (400ml) - R$ 18,00",
            "Copo Açaí (500ml) - R$ 22,00",
            "Copo Açaí (700ml) - R$ 28,00",
            "Taça Premium Sensação (Sorvete) - R$ 00,00",
        ]
    )
    
    # ==================================================
    # INCLUSÃO 2: ADICIONAIS E MONTANTE DO AÇAÍ
    # ==================================================
    st.write("✨ **Personalize seu Açaí (Monte do seu jeito):**")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        caldas_escolhidas = st.multiselect(
            "Escolha as Caldas (Inclusas):",
            ["Leite Condensado", "Calda de Chocolate", "Calda de Morango", "Mel", "Banana", "Sem Calda"]
        )
        frutas_escolhidas = st.multiselect(
            "Escolha as Frutas (Adicional R$: 2,00 cada se exceder o limite):",
            ["Banana", "Abacaxi", "Abacate", "Mamão", "Manga", "Maçã", "Uva"]
        )
        
    with col_f2:
        acompanhamentos_escolhidos = st.multiselect(
            "Acompanhamentos Tradicionais (Adicional R$: 3,00 cada se exceder o limite):",
            ["Leite em Pó", "Granola", "Paçoca", "Flocos de Arroz", "Granulado"]
        )
        adicionais_especiais = st.multiselect(
            "Adicionais Especiais (Consultar valores):",
            ["Ovo Maltine", "Doce de Leite", "M&Ms", "Kiwi"]
        )
    
    observacoes = st.text_area(
        "Observações ou Modificações Extras:", 
        placeholder="Ex: Sem granola, enviar colher extra, etc..."
    )
    
    botao_enviar = st.form_submit_button("🚀 Enviar Pedido para o Painel")

if botao_enviar:
    if nome_cliente.strip() == "":
        st.error("Por favor, preencha o seu nome para realizar o pedido.")
    else:
        # ==================================================
        # INCLUSÃO 3: REUNIR AS ESCOLHAS EM TEXTO PARA O PAINEL
        # ==================================================
        # Formata as listas selecionadas para virarem um texto bonito
        txt_caldas = ", ".join(caldas_escolhidas) if caldas_escolhidas else "Nenhuma"
        txt_frutas = ", ".join(frutas_escolhidas) if frutas_escolhidas else "Nenhuma"
        txt_acomp = ", ".join(acompanhamentos_escolhidos) if acompanhamentos_escolhidos else "Nenhum"
        txt_especiais = ", ".join(adicionais_especiais) if adicionais_especiais else "Nenhum"
        
        # Consolida tudo na string de observação que o visual.py já lê nativamente
        resumo_montagem = (
            f"🍧 Caldas: {"Leite Condesado", "Chocolate", "Morango", "Banana", "Mel"} | "
            f"🍓 Frutas: {"Banana", "Abacaxi", "Abacate", "Mamão", "Manga", "Maçã", "Uva"} | "
            f"🥜 Acompanhamentos: {"Farinha de Tapioca", "Flocos de Arroz", "Farinha Lactea", "Leite em Pó", "Amendoim", "Granola", "Neston"} | "
            f"⭐ Especiais: {"Ovo Maltini", "Doce de Leite", "M&Ms", "Kiwi"} | "
            f"💡 Obs: {observacoes.strip() if observacoes.strip() else 'Nenhuma'}"
        )

        novo_pedido = {
            "cliente": nome_cliente,
            "item": item_escolhido,
            "obs": resumo_montagem
        }
        
        # Adiciona na lista compartilhada
        st.session_state.pedidos_realizados.append(novo_pedido)
        st.success(f"🎉 Pedido enviado com sucesso, {nome_cliente}! Volte para a página inicial (Brandbook) no menu lateral para visualizar no Painel Geral.")

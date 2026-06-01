import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap

# ========================================
# CONFIGURAÇÃO DA PÁGINA
# ========================================
st.set_page_config(
    page_title="Dashboard Operacional",
    layout="wide"
)

st.title("⚡ Dashboard Operacional de Leituras")
st.markdown("Análise operacional de leituras de consumo de energia")

# ========================================
# UPLOAD
# ========================================
arquivo = st.file_uploader(
    "Envie a planilha CSV",
    type=["csv", "xlsx"]
)

# ========================================
# LEITURA
# ========================================
if arquivo:

    try:

        # CSV
        if arquivo.name.endswith(".csv"):
            try:
                df = pd.read_csv(
                    arquivo,
                    sep=';',
                    encoding='latin1'
                )
            except:
                df = pd.read_csv(arquivo)

        # EXCEL
        else:
            df = pd.read_excel(arquivo)

        # ========================================
        # LIMPEZA
        # ========================================
        df.columns = df.columns.str.strip()

        st.success("Planilha carregada com sucesso!")

        # ========================================
        # CONVERTER COLUNAS
        # ========================================

        # Consumo
        if 'Consumo' in df.columns:
            df['Consumo'] = pd.to_numeric(
                df['Consumo'],
                errors='coerce'
            )

        # Total Fatura
        if 'Total Fatura' in df.columns:
            df['Total Fatura'] = pd.to_numeric(
                df['Total Fatura'],
                errors='coerce'
            )

        # Latitude
        if 'Latitude' in df.columns:
            df['Latitude'] = pd.to_numeric(
                df['Latitude'],
                errors='coerce'
            )

        # Longitude
        if 'Longitude' in df.columns:
            df['Longitude'] = pd.to_numeric(
                df['Longitude'],
                errors='coerce'
            )

        # ========================================
        # FILTROS
        # ========================================
        st.sidebar.title("🔎 Filtros")

        # AGENTE
        if 'Agente' in df.columns:

            agentes = st.sidebar.multiselect(
                'Leiturista',
                options=sorted(df['Agente'].dropna().unique()),
                default=sorted(df['Agente'].dropna().unique())
            )

            df = df[df['Agente'].isin(agentes)]

        # BAIRRO
        if 'Bairro' in df.columns:

            bairros = st.sidebar.multiselect(
                'Bairro',
                options=sorted(df['Bairro'].dropna().unique()),
                default=sorted(df['Bairro'].dropna().unique())
            )

            df = df[df['Bairro'].isin(bairros)]

        # OCORRÊNCIA
        if 'Oco' in df.columns:

            ocorrencias = st.sidebar.multiselect(
                'Ocorrência',
                options=sorted(df['Oco'].dropna().unique()),
                default=sorted(df['Oco'].dropna().unique())
            )

            df = df[df['Oco'].isin(ocorrencias)]

        # ========================================
        # KPIs
        # ========================================
        st.subheader("📌 Indicadores Gerais")

        total_leituras = len(df)

        total_consumo = 0
        if 'Consumo' in df.columns:
            total_consumo = df['Consumo'].sum()

        total_faturamento = 0
        if 'Total Fatura' in df.columns:
            total_faturamento = df['Total Fatura'].sum()

        total_bairros = 0
        if 'Bairro' in df.columns:
            total_bairros = df['Bairro'].nunique()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            'Total Leituras',
            f'{total_leituras:,}'
        )

        col2.metric(
            'Consumo Total',
            f'{total_consumo:,.0f}'
        )

        col3.metric(
            'Faturamento Total',
            f'R$ {total_faturamento:,.2f}'
        )

        col4.metric(
            'Bairros',
            total_bairros
        )

        # ========================================
        # RANKING LEITURISTAS
        # ========================================
        if 'Agente' in df.columns:

            st.subheader('🏆 Ranking de Leituristas')

            ranking = (
                df.groupby('Agente')
                .size()
                .reset_index(name='Quantidade')
                .sort_values('Quantidade', ascending=False)
            )

            fig_ranking = px.bar(
                ranking,
                x='Agente',
                y='Quantidade',
                text_auto=True
            )

            st.plotly_chart(
                fig_ranking,
                use_container_width=True
            )

        # ========================================
        # CONSUMO POR BAIRRO
        # ========================================
        if 'Bairro' in df.columns and 'Consumo' in df.columns:

            st.subheader('🏘️ Consumo por Bairro')

            bairro_consumo = (
                df.groupby('Bairro')['Consumo']
                .sum()
                .reset_index()
                .sort_values('Consumo', ascending=False)
                .head(15)
            )

            fig_bairro = px.bar(
                bairro_consumo,
                x='Bairro',
                y='Consumo',
                text_auto=True
            )

            st.plotly_chart(
                fig_bairro,
                use_container_width=True
            )

        # ========================================
        # OCORRÊNCIAS
        # ========================================
        if 'Oco' in df.columns:

            st.subheader('⚠️ Ocorrências Operacionais')

            ocorrencia = (
                df.groupby('Oco')
                .size()
                .reset_index(name='Quantidade')
                .sort_values('Quantidade', ascending=False)
                .head(15)
            )

            fig_ocorrencia = px.pie(
                ocorrencia,
                names='Oco',
                values='Quantidade'
            )

            st.plotly_chart(
                fig_ocorrencia,
                use_container_width=True
            )

        # ========================================
        # FATURAMENTO POR LEITURISTA
        # ========================================
        if 'Agente' in df.columns and 'Total Fatura' in df.columns:

            st.subheader('💰 Faturamento por Leiturista')

            faturamento = (
                df.groupby('Agente')['Total Fatura']
                .sum()
                .reset_index()
                .sort_values('Total Fatura', ascending=False)
            )

            fig_faturamento = px.line(
                faturamento,
                x='Agente',
                y='Total Fatura',
                markers=True
            )

            st.plotly_chart(
                fig_faturamento,
                use_container_width=True
            )

        # ========================================
        # MAPA
        # ========================================
        if 'Latitude' in df.columns and 'Longitude' in df.columns:

            st.subheader('🗺️ Mapa de Leituras')

            mapa_df = df.dropna(subset=['Latitude', 'Longitude'])

            if len(mapa_df) > 0:

                centro_lat = mapa_df['Latitude'].mean()
                centro_lon = mapa_df['Longitude'].mean()

                mapa = folium.Map(
                    location=[centro_lat, centro_lon],
                    zoom_start=11
                )

                heat_data = [
                    [row['Latitude'], row['Longitude']]
                    for index, row in mapa_df.iterrows()
                ]

                HeatMap(heat_data).add_to(mapa)

                st_folium(
                    mapa,
                    width=1200,
                    height=500
                )

        # ========================================
        # TABELA RESUMO
        # ========================================
        st.subheader('📋 Resumo Operacional')

        colunas_resumo = []

        for coluna in [
            'Agente',
            'Bairro',
            'Consumo',
            'Total Fatura',
            'Oco'
        ]:
            if coluna in df.columns:
                colunas_resumo.append(coluna)

        st.dataframe(
            df[colunas_resumo],
            use_container_width=True
        )

        # ========================================
        # EXPORTAÇÃO
        # ========================================
        st.subheader('⬇️ Exportar Relatório')

        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label='Baixar CSV',
            data=csv,
            file_name='relatorio_operacional.csv',
            mime='text/csv'
        )

    except Exception as erro:
        st.error(f'Erro ao processar planilha: {erro}')

else:
    st.info('Envie sua planilha para iniciar a análise.')

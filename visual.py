for i, (nome, cor) in enumerate(cores):

    with cols[i % 3]:

        text_color = "black" if cor.upper() == "#FDFBFE" else "white"

        st.markdown(f"""
        <div style="
            background:{cor};
            padding:22px;
            border-radius:12px;
            text-align:center;
            font-weight:bold;
            color:{text_color};
        ">
        {nome}<br>{cor}
        </div>
        """, unsafe_allow_html=True)

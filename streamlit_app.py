import streamlit as st
from pbixray import PBIXRay

def app():
    st.title("PBIX info")

    uploaded_file = st.file_uploader("Choose a PBIX file", type="pbix")
    if uploaded_file:
        # Unpack the PBIX file to get the schema_df
        model = PBIXRay(uploaded_file)


        st.write(model.metadata)


        # Let the user select a table name
        table_name_input = st.selectbox("Select a table name:", model.tables)

        st.dataframe(model.get_table(table_name_input), use_container_width=True)


if __name__ == '__main__':
    app()

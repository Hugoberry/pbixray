import streamlit as st
from pbixray.core import PBIXRay

def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def app():
    st.title("PBIX info")

    uploaded_file = st.file_uploader("Choose a PBIX file", type="pbix")
    if uploaded_file:
        # Unpack the PBIX file to get the schema_df
        model = PBIXRay(uploaded_file)


        st.write(model.metadata)
        
        met1, met2 = st.columns(2)
        
        met1.metric(label='Model size', value = sizeof_fmt(model.size))
        met2.metric(label='# Tables', value = model.tables.size)

        st.write("Schema:")
        st.write(model.schema)

        st.write("Statistics:")
        st.dataframe(model.statistics)

        if model.relationships.size:
            st.write("Relationships:")
            st.write(model.relationships)

        if model.power_query.size:
            st.write("Power Query code:")
            st.dataframe(model.power_query)

        if model.m_parameters.size:
            st.write("M parameters:")
            st.dataframe(model.m_parameters)

        if model.dax_tables.size:
            st.write("DAX tables:")
            st.dataframe(model.dax_tables)
        
        if model.dax_measures.size:
            st.write("DAX measures:")
            st.dataframe(model.dax_measures)

        if model.dax_columns.size:
            st.write("Calculated columns:")
            st.dataframe(model.dax_columns)
            
        # Let the user select a table name
        table_name_input = st.selectbox("Select a table to peek at its contents:", model.tables)

        if st.button("Un-VertiPaq"):
            st.dataframe(model.get_table(table_name_input), use_container_width=True)


if __name__ == '__main__':
    app()

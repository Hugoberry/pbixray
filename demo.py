from pbixray import PBIXRay

# PBIX_FILE_PATH = r"C:\git\hub\pbixray\test-data\Excalidraw.pbix"
PBIX_FILE_PATH = r"C:\git\hub\pbixray\test-data\Sales & Returns Sample v201912.pbix"
model = PBIXRay(PBIX_FILE_PATH)
print(model.tables)
print(model.metadata)
print(model.power_query)
print(model.statistics)
print(model.dax_tables)
print(model.dax_measures)
print(model.size)
print(model.schema)
print(model.get_table("Age"))
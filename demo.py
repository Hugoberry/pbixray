from pbixray import PBIXRay
from icecream import ic

model = PBIXRay("data/Sales & Returns Sample v201912.pbix")

# Metadata & schema
ic(model.tables)
ic(model.metadata)
ic(model.power_query)
ic(model.m_parameters)
ic(model.statistics)
ic(model.dax_tables)
ic(model.dax_measures)
ic(model.dax_columns)
ic(model.size)
ic(model.schema)
ic(model.relationships)
ic(model.rls)

# Data extraction
ic(model.get_table("Age"))

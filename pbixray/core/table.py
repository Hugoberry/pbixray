class Table:

    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.columns = []

    def to_arrow_table(self):
        # Logic to convert this specific table to an Arrow table
        pass

    def to_dataframe(self):
        # Logic to convert this specific table to a DataFrame
        pass
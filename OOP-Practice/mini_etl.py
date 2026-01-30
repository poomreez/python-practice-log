# Mini ETL Pipeline

class DataSource:
    def read_data(self):
        pass

class CSVFile(DataSource):
    def read_data(self):
        print("Reading data from CSV file...")
        return ["row1,100", "row2,200"]

class DatabaseConnection(DataSource):
    def read_data(self):
        print("Connecting to DB & Running Query...")
        return [{"id":1, 'val':100}, {"id":2, "val":200}]

my_sources = [CSVFile(), DatabaseConnection()]

print("------- Starting ETL Pipeline -------")

for source in my_sources:
    data = source.read_data()
    print(f"Get data: {data}")
    print("-" * 37)
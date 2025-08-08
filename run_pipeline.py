# Main script to run the data pipeline

from pipeline.extract import extract
from pipeline.transform import transform
from pipeline.load import load
from pipeline.check import check_result
from pipeline.db import test_db_connection
from config import DB_URL

# Test database connection
test_db_connection(DB_URL)

# Run the data pipeline
df = extract("data/test_data.csv")
transformed = transform(df)
load(transformed)

# Check the ETL result in the database 
check_result()  

# Creaete a summary table in the database
#TODO: Implement summary data and table creation logic
#TODO: check the results stored in the summary table
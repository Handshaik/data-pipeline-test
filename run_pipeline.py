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
load(transformed, "user_actions")

# Check the ETL result in the database 
check_result("user_actions")  
 
# TODO: Implement a meterialised view(s) or summary table(s) in the database to support the 
# customer sucess and finance teams queries of user activity and credits over days, weeks and months.

# TODO: check the results stored in the new db schema
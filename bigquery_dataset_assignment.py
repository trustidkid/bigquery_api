
import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bq_service_account.json'

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
    SELECT *
    FROM `bigquery-public-data.flash-parity-384812.flights`
    LIMIT 20
"""
query_job = client.query(query)  # Make an API request.

for row in query_job.result():
    print(row)

import base64
import json
from google.cloud import bigquery

DATASET_ID = "tweets_dataset"
TABLE_ID = "tweets_table"

def insert_rows_to_bq(rows):
    client = bigquery.Client()
    dataset_ref = client.dataset(DATASET_ID)
    table_ref = dataset_ref.table(TABLE_ID)
    errors = client.insert_rows_json(table_ref, rows)
    if len(errors) == 0:
        print("New rows have been added")
    else:
        print("Encounterred errors while inserting rows: {}".format(errors))

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message[:100])
    # insert pubsub_message as a big query row
    json_obj = json.loads(pubsub_message)
    insert_rows_to_bq([json_obj]) # make a list
    
# Semi-annual Task

import warnings
from elasticsearch import Elasticsearch, ElasticsearchWarning
from datetime import datetime

# Suppress Elasticsearch warnings
warnings.filterwarnings('ignore', category=ElasticsearchWarning)

# Connection to Elasticsearch
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    basic_auth=("elastic", "XXXX")  # Use basic_auth instead of http_auth
)

# Verify the connection
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Connection error")

index_name = "log-index"

# Check if the index exists
if not es.indices.exists(index=index_name):
    print(f"Index '{index_name}' does not exist. Creating a new index...")
    es.indices.create(index=index_name)

    # Add sample data
    for i in range(5):  # Add 5 sample documents
        doc = {
            'author': f'Author {i}',
            'text': f'This is a sample text from Author {i}.',
            'timestamp': datetime.now(),
        }
        response = es.index(index=index_name, id=i + 1, body=doc)
        print(f"Added document: {response['_id']}")  # Information on added document
    print("Sample documents added.")
else:
    print(f"Index '{index_name}' already exists.")

# Pagination parameters
page = 1  # Page number
page_size = 10  # Number of results per page
from_result = (page - 1) * page_size  # Calculate offset

# Example query with pagination
try:
    response = es.search(index=index_name, body={
        "query": {
            "match_all": {}
        },
        "from": from_result,
        "size": page_size
    })

    total_results = response['hits']['total']['value']
    print(f"Total results: {total_results}")

    for hit in response['hits']['hits']:
        print(hit['_source'])

except Exception as e:
    print(f"An error occurred: {e}")

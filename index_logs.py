import warnings
from elasticsearch import Elasticsearch, ElasticsearchWarning
from datetime import datetime

# Disable Elasticsearch warnings
warnings.filterwarnings('ignore', category=ElasticsearchWarning)

# Connect to Elasticsearch
es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'http'}],
    basic_auth=("elastic", "XXXX")  # Use basic_auth instead of http_auth
)

# Check connection
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Connection error")

index_name = "log-index"

# Check if index exists
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
        print(f"Document added: {response['_id']}")  # Information about added document
    print("Sample documents added.")
else:
    print(f"Index '{index_name}' already exists.")

# Example of a filtered query
try:
    response = es.search(index=index_name, body={
        "query": {
            "match_all": {}
        },
        "size": 10
    })

    total_results = response['hits']['total']['value']
    print(f"Total number of results: {total_results}")

    for hit in response['hits']['hits']:
        print(hit['_source'])

except Exception as e:
    print(f"An error occurred: {e}")


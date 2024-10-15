import warnings
from elasticsearch import Elasticsearch, ElasticsearchWarning

# Disable Elasticsearch w
warnings.filterwarnings('ignore', category=ElasticsearchWarning)

# Connect to the Elasticsearch cluster running locally on port 9200
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Check if the connection to Elasticsearch is successful
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Connection failed")

# Example query: Fetch documents from the "log-index" index
# We use the match_all query to retrieve all documents, limiting the results to 10
response = es.search(index="log-index", body={
    "query": {
        "match_all": {}
    },
    "size": 10  # Limit the number of results to 10
})

# Loop through the results and print each document's source data
for hit in response['hits']['hits']:
    print(hit['_source'])

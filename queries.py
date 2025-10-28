from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents import SearchClient
from config import settings

credential = AzureKeyCredential(settings.search_api_key)
search_client = SearchClient(
    endpoint=settings.search_endpoint,
    index_name=settings.index_name,
    credential=credential
)

results =  search_client.search(
    query_type='simple',
    search_text="*" ,
    select='HotelName,Description,Tags',
    include_total_count=True
)

print ('Total Documents Matching Query:', results.get_count())
for result in results:
    print(result["@search.score"])
    print(result["HotelName"])
    print(result["Tags"])
    print(f"Description: {result['Description']}")
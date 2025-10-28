from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents import SearchClient
from config import settings
from documents import documents

credential = AzureKeyCredential(settings.search_api_key)
search_client = SearchClient(
    endpoint=settings.search_endpoint,
    index_name=settings.index_name,
    credential=credential
)

try:
    result = search_client.upload_documents(documents=documents)
    print("Upload of new document succeeded: {}".format(result[0].succeeded))
except Exception as ex:
    print (ex.message)

    index_client = SearchIndexClient(
    endpoint=settings.search_endpoint, credential=credential)


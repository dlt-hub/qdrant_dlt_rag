import qdrant_client
from qdrant_client import QdrantClient
from dotenv import load_dotenv
load_dotenv()

import os

QDRANT_KEY = os.getenv('QDRANT_KEY')
QDRANT_CLIENT = os.getenv('QDRANT_CLIENT')

qdrant_client = QdrantClient(QDRANT_CLIENT,
                             api_key=QDRANT_KEY,
                             )


import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def delete_all_collections(qdrant_client):
    """
    Deletes all collections from a Qdrant client.

    Parameters:
    - qdrant_client: An instance of a Qdrant client.

    This function will attempt to delete each collection retrieved from the Qdrant client.
    If an error occurs during the deletion of a collection, it logs the error.
    """
    try:
        collections = qdrant_client.get_collections()
        for collection_info in collections:
            collection_name = collection_info[1]
            logging.info(f"Deleting collection: {collection_name}")
            try:
                qdrant_client.delete_collection(collection_name)
            except Exception as e:
                logging.error(f"Error deleting collection {collection_name}: {e}")
    except Exception as e:
        logging.error(f"Error retrieving collections: {e}")

# Example usage
delete_all_collections(qdrant_client=qdrant_client)
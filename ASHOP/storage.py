from storages.backends.azure_storage import AzureStorage
from decouple import config


class AzureMediaStorage(AzureStorage):
    account_name = config('AZURE_ACCOUNT_NAME',default='afridi')
    account_key = config('AZURE_ACCOUNT_KEY',default='06611')
    azure_container = 'media'
    expiration_secs = None
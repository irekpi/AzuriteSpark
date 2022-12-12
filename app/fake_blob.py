from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import ContainerClient, BlobServiceClient


class FakeStorage:
    # basic azurite blob creds
    CONN_STR = "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"

    def create_blob(self, path, name, container_name='test1'):
        container = ContainerClient.from_connection_string(self.CONN_STR, container_name=container_name)
        try:
            with open(path, 'rb') as file:
                container.upload_blob(data=file, name=name)
        except ResourceExistsError:
            print('Blob already exists')

    def create_container(self, container_name='test1'):
        blob_service = BlobServiceClient.from_connection_string(self.CONN_STR)
        try:
            blob_service.create_container(container_name)
        except ResourceExistsError:
            print('Container  already exists')


if __name__ == '__main__':
    fake_storage = FakeStorage()
    fake_storage.create_container()
    fake_storage.create_blob('/app/app/fixtures/test_csv.csv', 'test_csv.csv')

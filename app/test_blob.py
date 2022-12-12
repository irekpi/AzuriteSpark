from spark import SparkBase

TEST_BLOB_PATH = "wasb://test1@devstoreaccount1/test_csv.csv"

if __name__ == "__main__":
    client = SparkBase()
    df = client.read_blob(TEST_BLOB_PATH)
    df.show()


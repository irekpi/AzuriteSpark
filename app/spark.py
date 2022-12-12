import pyspark


class SparkConfig:
    spark_cores_max = 2
    spark_exec_cores = 2
    spark_exec_memo = '2gb'


spark_cfg = SparkConfig()


class SparkBase:
    def __init__(self, app_name='test'):
        conf = pyspark.SparkConf().setAll(self.set_spark_cfg())
        self.spark = pyspark.sql.SparkSession.builder \
            .appName(app_name) \
            .config(conf=conf) \
            .getOrCreate()

    def read_blob(self, address):
        df = self.spark.read.format("csv").option("header", True).load(address)
        return df

    def set_spark_cfg(self):
        cfg = [
            ("spark.jars.ivy", "/spark_pcg"),
            ("spark.cores.max", spark_cfg.spark_cores_max),
            ('spark.executor.cores', spark_cfg.spark_exec_cores),
            ('spark.executor.memory', spark_cfg.spark_exec_memo),
            ("spark.hadoop.fs.azure.storage.emulator.account.name", 'devstoreaccount1'),
        ]
        return cfg
# spark-submit --packages org.apache.hadoop:hadoop-azure:3.3.1 /app/app/test_blob.py

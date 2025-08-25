# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7b8ee5c3-336c-4f67-84c2-b0db30f220a9",
# META       "default_lakehouse_name": "LHDeveloper",
# META       "default_lakehouse_workspace_id": "7ae470f7-df91-41dc-bb25-f17c2ed54575",
# META       "known_lakehouses": [
# META         {
# META           "id": "7b8ee5c3-336c-4f67-84c2-b0db30f220a9"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import sys
import os

# import Constant
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf


if __name__ == "__main__":

    # Spark session builder
    spark_session = (
        SparkSession.builder.appName("sjdsampleapp")
        .config("spark.some.config.option", "some-value")
        .getOrCreate()
    )

    spark_context = spark_session.sparkContext
    spark_context.setLogLevel("DEBUG")

    print(
        "spark.synapse.pool.name : " + spark_session.conf.get("spark.synapse.pool.name")
    )
    print()
    print("spark.driver.cores : " + spark_session.conf.get("spark.driver.cores"))
    print("spark.driver.memory : " + spark_session.conf.get("spark.driver.memory"))
    print("spark.executor.cores : " + spark_session.conf.get("spark.executor.cores"))
    print("spark.executor.memory : " + spark_session.conf.get("spark.executor.memory"))
    print(
        "spark.executor.instances: "
        + spark_session.conf.get("spark.executor.instances")
    )
    print()
    print(
        "spark.dynamicAllocation.enabled : "
        + spark_session.conf.get("spark.dynamicAllocation.enabled")
    )
    print(
        "spark.dynamicAllocation.maxExecutors : "
        + spark_session.conf.get("spark.dynamicAllocation.maxExecutors")
    )
    print(
        "spark.dynamicAllocation.minExecutors : "
        + spark_session.conf.get("spark.dynamicAllocation.minExecutors")
    )

    # tableName = "yellowtripdata"
    # You can download the sample Parquet file from this site "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page" and upload it to the files section of the lakehouse.
    csvFilePath = "Files/SalesDataset.csv"
    # deltaTablePath = SaveToLH + "/Tables/" + tableName
    deltaTablePath = "Tables/salesdataset"

    df = spark_session.read.format('csv').options(header='true', inferschema='true').load(csvFilePath)
    df.write.mode("overwrite").format("delta").save(deltaTablePath)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

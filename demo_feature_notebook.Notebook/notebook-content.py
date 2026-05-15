# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a27788df-a50f-432e-aa08-96dbb803cc32",
# META       "default_lakehouse_name": "lh_first_lakehouse",
# META       "default_lakehouse_workspace_id": "14b56594-e527-48ef-ae85-1d10f404caf3",
# META       "known_lakehouses": [
# META         {
# META           "id": "a27788df-a50f-432e-aa08-96dbb803cc32"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "default_warehouse": "85546431-b2df-47a1-ae3c-4b5cc339dddd",
# META       "known_warehouses": [
# META         {
# META           "id": "85546431-b2df-47a1-ae3c-4b5cc339dddd",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

env = "DEV"
env = env.upper()
CONFIG = {
    "DEV": {"multiplier": 1, "write_mode": "overwrite"},
    "TEST": {"multiplier": 2, "write_mode": "overwrite"},
    "PROD": {"multiplier": 5, "write_mode": "append"}
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# CONFIG = {
#     "DEV": {
#         "multiplier": 1,
#         "write_mode": "overwrite"
#     },
#     "TEST": {
#         "multiplier": 2,
#         "write_mode": "overwrite"
#     },
#     "PROD": {
#         "multiplier": 5,
#         "write_mode": "append"
#     }
# }

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import Row
from pyspark.sql.functions import col

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# import notebookutils
# env = notebookutils.runtime.get("environment", "DEV")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# from pyspark.sql import Row

# raw_data = [
#     Row(order_id=1, customer="Alice", amount=100, country="UK"),
#     Row(order_id=2, customer="Bob", amount=200, country="UK"),
#     Row(order_id=3, customer="Charlie", amount=150, country="US"),
#     Row(order_id=4, customer="Diana", amount=300, country="US"),
# ]

# df_raw = spark.createDataFrame(raw_data)

# df_raw.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

base_data = [
    Row(order_id=1, customer="Alice", amount=100, country="UK"),
    Row(order_id=2, customer="Bob", amount=200, country="UK"),
    Row(order_id=3, customer="Charlie", amount=150, country="US"),
    Row(order_id=4, customer="Diana", amount=300, country="US"),
]

# multiplier = CONFIG[env]["multiplier"]
# data = base_data * multiplier

# df_raw = spark.createDataFrame(data)

# df_raw.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def ingest_data(base_data, multiplier):
    data = base_data * multiplier
    return spark.createDataFrame(data)

def transform_data(df):
    from pyspark.sql.functions import col
    return df.withColumn("is_high_value", col("amount") > 150)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def write_data(df, env, write_mode):
    table_name = f"{env}_orders_gold"
    df.write.mode(write_mode).saveAsTable(table_name)
    return table_name

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def validate_data(table_name):
    return spark.read.table(table_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

env = env.strip().upper()

multiplier = CONFIG[env]["multiplier"]
write_mode = CONFIG[env]["write_mode"]

df_raw = ingest_data(base_data, multiplier)
df_silver = transform_data(df_raw)
table_name = write_data(df_silver, env, write_mode)
df_check = validate_data(table_name)

df_check.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# from pyspark.sql.functions import col

# df_silver = df_raw \
#     .withColumn("is_high_value", col("amount") > 150)

# df_silver.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_silver = df_raw.withColumn(
    "is_high_value",
    col("amount") > 150
)

df_silver.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# df_silver.write.mode("overwrite").saveAsTable("orders_gold")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

table_name = f"{env}_orders_gold"
write_mode = CONFIG[env]["write_mode"]

df_silver.write.mode(write_mode).saveAsTable(table_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# df_check = spark.read.table("orders_gold")
# df_check.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_check = spark.read.table(table_name)
df_check.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

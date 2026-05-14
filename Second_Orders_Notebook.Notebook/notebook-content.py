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
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

spark_df = spark.read.parquet("Files/First_Workstream/orders_second.parquet")

spark.sql("CREATE DATABASE IF NOT EXISTS Second_Schema")

spark_df.write.mode("overwrite").saveAsTable("Second_Schema.orders_second")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

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

# MAGIC %%sql
# MAGIC Create SCHEMA first_schema

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
# file_path = "/lakehouse/default/Files/Upload/products.xlsx"
import pandas as pd
file_path = '/lakehouse/default/Files/First_Workstream/Apocolypse Food Prep.xlsx'

df = pd.read_excel(file_path, engine="openpyxl")

spark_df = spark.createDataFrame(df)

spark_df.write.mode("overwrite").saveAsTable("First_Schema.Food_Prep")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
# file_path = "/lakehouse/default/Files/Upload/products.xlsx"
import pandas as pd
file_path = '/lakehouse/default/Files/First_Workstream/Apocolypse Food Prep.xlsx'

df = pd.read_excel(file_path, engine="openpyxl")

spark_df = spark.createDataFrame(df)

spark_df.write.mode("overwrite").saveAsTable("First_Schema.Food_Prep_2")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
# file_path = "/lakehouse/default/Files/Upload/products.xlsx"
import pandas as pd
file_path = '/lakehouse/default/Files/First_Workstream/orders_first.parquet'

df = pd.read_excel(file_path, engine="openpyxl")

spark_df = spark.createDataFrame(df)

spark_df.write.mode("overwrite").saveAsTable("First_Schema.orders_first")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
# file_path = "/lakehouse/default/Files/Upload/products.xlsx"
import pandas as pd
file_path = '/lakehouse/default/Files/First_Workstream/orders_second.parquet'

df = pd.read_excel(file_path, engine="openpyxl")

spark_df = spark.createDataFrame(df)

spark_df.write.mode("overwrite").saveAsTable("First_Schema.orders_second")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# %% Databricks notebook source
MAGIC %pip install -e ..
MAGIC %restart_python

# %% load the data using spark
print("Connect to the databricks!!")
# COMMAND ----------
df = spark.read.csv("laptop_clean_dataset.csv")


# COMMAND ----------
display(df)


# COMMAND ----------

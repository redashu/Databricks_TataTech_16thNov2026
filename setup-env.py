# lets define default things
CATALOG = "databricks_ukwest"
SCHEMA  = "default"
VOLUME  = "ashuvolume"
# create if not exist volume 
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME}")
# use default options 
spark.sql(f"USE CATALOG {CATALOG}")
spark.sql(f"USE SCHEMA {SCHEMA}")
# checking print volume path 
VOLUME_PATH = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"

# lets print all default settings
print(f"Catalog : {CATALOG}")
print(f"Schema :  {SCHEMA}")
print(f"Volume : {VOLUME_PATH}")
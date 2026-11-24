# lets define default things
CATALOG = "databricks_ukwest"
SCHEMA  = "default"
VOLUME1  = "ashuvolume_data"
VOLUME2  = "ashuvolume_schema"
VOLUME3  = "ashuvolume_checkpoint"

# create if not exist volume 
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME1}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME2}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME3}")

# use default options 
spark.sql(f"USE CATALOG {CATALOG}")
spark.sql(f"USE SCHEMA {SCHEMA}")
# checking print volume path 
VOLUME_PATH1 = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME1}"
VOLUME_PATH2 = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME2}"
VOLUME_PATH3 = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME3}"


# lets print all default settings
print(f"Catalog : {CATALOG}")
print(f"Schema :  {SCHEMA}")
print(f"Volume Data : {VOLUME_PATH1}")
print(f"Volume Schema : {VOLUME_PATH2}")
print(f"Volume Checkpoint : {VOLUME_PATH3}")


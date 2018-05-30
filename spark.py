#-*-encoding=utf-8
from pyspark.sql.types import Row,StructField,StructType,StringType,IntegerType
cols='id name age score'

schema=StructType([StructField('person_name',StringType(),False),StructField('person_age',IntegerType(),False)])
another_df=sqlContext.createDataFrame(another_rdd,schema)
another_df.printSchema()



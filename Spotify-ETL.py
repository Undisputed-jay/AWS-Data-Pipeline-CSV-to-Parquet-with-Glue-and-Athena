import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node albums
albums_node1729530667547 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://etljobpipeline/staging/albums.csv"], "recurse": True}, transformation_ctx="albums_node1729530667547")

# Script generated for node tracks
tracks_node1729530670027 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://etljobpipeline/staging/track.csv"], "recurse": True}, transformation_ctx="tracks_node1729530670027")

# Script generated for node artist
artist_node1729530663817 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://etljobpipeline/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1729530663817")

# Script generated for node Join
Join_node1729531480629 = Join.apply(frame1=albums_node1729530667547, frame2=artist_node1729530663817, keys1=["artist_id"], keys2=["id"], transformation_ctx="Join_node1729531480629")

# Script generated for node Join
Join_node1729533439013 = Join.apply(frame1=Join_node1729531480629, frame2=tracks_node1729530670027, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Join_node1729533439013")

# Script generated for node Drop Fields
DropFields_node1729534686930 = DropFields.apply(frame=Join_node1729533439013, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1729534686930")

# Script generated for node Amazon S3
AmazonS3_node1729535463836 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1729534686930, connection_type="s3", format="glueparquet", connection_options={"path": "s3://etljobpipeline/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1729535463836")

job.commit()
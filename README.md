<div>
    <h2>Project Overview</h2>
    <p>This project automates the process of extracting data from CSV files stored in an S3 bucket, transforming the data through AWS Glue, and writing the transformed data back to S3 in Parquet format. Finally, it uses AWS Glue Crawler to update the metadata in the AWS Glue Data Catalog for querying via Amazon Athena. This enables you to perform powerful SQL queries on large datasets efficiently.</p>
</div>   
    <h3>Workflow Summary</h3>
    <ul>
        <li><strong>Data Ingestion (S3 to Glue):</strong> CSV files are stored in the staging directory in S3. AWS Glue extracts these files, represented as dynamic frames in the ETL script.</li>
        <li><strong>ETL Job:</strong>
            <ul>
                <li>The data from albums, tracks, and artists CSV files is loaded into AWS Glue dynamic frames.</li>
                <li>The Join transformations combine data from the three tables based on relevant foreign keys (<code>artist_id</code>, <code>track_id</code>).</li>
                <li>Irrelevant or duplicate fields are dropped from the final dataset.</li>
            </ul>
        </li>
        <li><strong>Data Transformation (Glue to Parquet):</strong> The final, transformed data is written back to a designated S3 location in Parquet format with Snappy compression for optimized storage and faster query performance.</li>
        <li><strong>Cataloging with Glue Crawler:</strong> The AWS Glue Crawler automatically updates the Glue Data Catalog with the schema and metadata of the Parquet files, making the data queryable using Amazon Athena.</li>
        <li><strong>Querying with Athena:</strong> Athena is used to perform SQL queries on the transformed data stored in S3, offering seamless analytics and reporting capabilities.</li>
    </ul>
    
  <h3>Steps for Execution</h3>
    <ol>
        <li><strong>Set Up AWS Resources:</strong>
            <ul>
                <li>Create an S3 bucket for storing raw CSV files (staging folder) and transformed data (datawarehouse folder).</li>
                <li>Upload your CSV files (e.g., <code>albums.csv</code>, <code>tracks.csv</code>, <code>artists.csv</code>) to the S3 staging folder.</li>
            </ul>
        </li>
        <li><strong>Create an AWS Glue Job:</strong>
            <ul>
                <li>Use the provided code as the script for an AWS Glue Job.</li>
                <li>Ensure the Glue job is configured to access your S3 bucket and has permissions to read/write data.</li>
            </ul>
        </li>
        <li><strong>Run the Glue Job:</strong> Execute the Glue job to perform the ETL process, which will transform the data and write it back to the S3 datawarehouse folder in Parquet format.</li>
        <li><strong>Use AWS Glue Crawler:</strong> Configure a Glue Crawler to scan the datawarehouse folder and update the Glue Data Catalog with the schema of the Parquet files.</li>
        <li><strong>Query Data with Athena:</strong> Once the data is cataloged, use Athena to perform SQL queries on the transformed data for analysis or reporting.</li>
    </ol>

  <h3>Features</h3>
    <ul>
        <li><strong>CSV to Parquet Transformation:</strong> Converts raw CSV files to an optimized Parquet format for efficient querying.</li>
        <li><strong>Data Cleaning and Joining:</strong> Joins multiple datasets and removes unnecessary fields before saving.</li>
        <li><strong>S3 Integration:</strong> Seamless integration with S3 for both input (CSV) and output (Parquet) storage.</li>
        <li><strong>AWS Glue Crawler:</strong> Automatically updates the data catalog for Athena queries.</li>
        <li><strong>Scalability:</strong> Can easily be expanded to handle additional transformations or datasets.</li>
    </ul>

  <h3>Requirements</h3>
    <ul>
        <li>AWS Glue (Job and Crawler)</li>
        <li>S3 Bucket for storage</li>
        <li>Amazon Athena for querying</li>
    </ul>

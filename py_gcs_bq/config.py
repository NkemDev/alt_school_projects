from google.cloud import bigquery
def fetch_job_config(file_format, schema, create_disposition='CREATE_IF_NEEDED', write_disposition='WRITE_APPEND'):
    # write_disposition='WRITE_TRUNCATE'
    config_dict = {
    "json" : bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            schema=schema,
            create_disposition=create_disposition,
            write_disposition = write_disposition
        ),
    
    "avro" : bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.AVRO,
            schema = schema,
            use_avro_logical_types=True,
            create_disposition=create_disposition,
            write_disposition = write_disposition
        ),
    
    "csv" : bigquery.LoadJobConfig(
       source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        field_delimiter=",",
        quote_character="",
        schema=schema,
        autodetect=False,
        write_disposition = write_disposition
    ),

    "parquet": bigquery.LoadJobConfig(
       source_format=bigquery.SourceFormat.PARQUET,
       create_disposition = create_disposition,
       schema=schema,
       write_disposition = write_disposition
    )
    }
    return config_dict[file_format]
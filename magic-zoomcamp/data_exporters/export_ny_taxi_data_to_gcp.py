import os
import pyarrow as pa
from pandas import DataFrame


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/src/keys/keys.json'

bucket_name = 'mage-demo-bucket-andreev'
# project_id = 'terraform-demo-412521'
file_name = 'ny_taxi_data'
root_path = f'{bucket_name}/{file_name}'


@data_exporter
def export_data_to_gcs_as_partitioned_parquets(df: DataFrame, *args, **kwargs) -> None:
    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pa.parquet.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )

import boto3
import datetime

def run():
    client = boto3.client("kinesis")
    streams = client.list_streams()

    test_stream = client.describe_stream(StreamName='test',)

    shards = test_stream["StreamDescription"]["Shards"]

    for shard in shards:
        iterator = client.get_shard_iterator(
            StreamName='test',
            ShardId=shard["ShardId"],
            ShardIteratorType='AT_SEQUENCE_NUMBER',
            StartingSequenceNumber=shard["SequenceNumberRange"]["StartingSequenceNumber"],
            Timestamp=datetime.datetime(2017, 8, 2)
        )
        records = client.get_records(
            ShardIterator=iterator["ShardIterator"],
        )
        print records
        

if __name__ == "__main__":
    run()
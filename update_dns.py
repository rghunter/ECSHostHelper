import requests
import boto3
import os
import requests

zone_id = os.environ['ZONE_ID']
record = os.environ['RECORD']
ttl = os.environ.get('TTL', 180)

client = boto3.client('route53')


def get_local_ip():
    return requests.get('http://169.254.169.254/latest/meta-data/local-ipv4'


response = client.change_resource_record_sets(
    HostedZoneId=zone_id,
    ChangeBatch={
        "Comment": "Automatic DNS update",
        "Changes": [
            {
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": record,
                    "Type": "A",
                    "TTL": ttl,
                    "ResourceRecords": [
                        {
                            "Value": get_local_ip()
                        },
                    ],
                }
            },
        ]
    }
)

import requests
import boto3

client = boto3.client('route53')
hosted_zone = "ZYIQ07YV68SXE"



response = client.change_resource_record_sets(
    HostedZoneId=hosted_zone,
    ChangeBatch={
        "Comment": "Automatic DNS update",
        "Changes": [
            {
                "Action": "UPSERT",
                "ResourceRecordSet": {
                    "Name": "statsd.ryanhunter.co",
                    "Type": "CNAME",
                    "TTL": 180,
                    "ResourceRecords": [
                        {
                            "Value": "test.cens.io"
                        },
                    ],
                }
            },
        ]
    }
)

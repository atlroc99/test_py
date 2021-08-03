import json
import datetime
from dateutil.tz import tzutc


def lambda_handler(event, context):
    # TODO implement

    my_dictionary = {
        'Contents': [
            {
                'Key': 'filename-1.pdf',
                'LastModified': datetime.datetime(2018, 12, 19, 15, 32, 54, tzinfo=tzutc()),
                'Size': 1545033
            },
            {
                'Key': 'filename-2.pdf',
                'LastModified': datetime.datetime(2018, 12, 19, 15, 32, 54, tzinfo=tzutc()),
                'Size': 4222827
            },
            {
                'Key': 'filename-3.pdf',
                'LastModified': datetime.datetime(2018, 12, 19, 15, 32, 54, tzinfo=tzutc()),
                'Size': 640925
            },
            {
                'Key': 'filename-4.pdf',
                'LastModified': datetime.datetime(2018, 12, 19, 15, 32, 54, tzinfo=tzutc()),
                'Size': 1617724
            },
        ]
    }

    def convert_datetime(item):
        if isinstance(item, (datetime.datetime, datetime.date)):
            return item.timestamp()

    response = {
        'statusCode': 200,
        # 'body': json.dumps('Hello from Lambda!')
        'body': json.dumps({'dictionary': my_dictionary},default=convert_datetime)
    }

    print(response)
    return response


lambda_handler(None, None)

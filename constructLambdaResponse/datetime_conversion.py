import json
import datetime
from dateutil.tz import tzutc

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


def convert_datetime(datetime_item):
    if isinstance(datetime_item, (datetime.date, datetime.datetime)):
        return datetime_item.timestamp()


my_json_data = json.dumps(my_dictionary, indent=2, default=convert_datetime)

print('my_json_data')
print(my_json_data)

import os
import requests
import json
from dotenv import load_dotenv


def read_file():
    aql_query_file = '../json_files/aql_query'
    with open(file=aql_query_file, mode='r') as f:
        payload = f.read()

    print(payload)
    load_dotenv()
    token = os.environ.get('bearer-token')
    print('token::: ', token)

    response = requests.post(
        url=os.environ.get('url'),
        headers={'Authorization': 'Bearer ' + os.environ.get('bearer-token'), 'Content-Type': 'text/plain'},
        data=payload
    )

    content = response.text
    print(f'content type: {type(content)}')
    print(content)

    response_dict = json.loads(content)
    pretty_json = json.dumps(response_dict, indent=1)
    print(pretty_json)

read_file()

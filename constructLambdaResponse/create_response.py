import json


def create_response():
    people_dict = {
        "object": {
            "key": "serverless-presigned/03820/WO-070721-002/WO-070721-002-SurveyForm.json",
            "size": 2043,
            "eTag": "6c701420edadccff03e44a9c10657867",
            "sequencer": "006102A36CB8F90AA4"
        }
    }

    print('Type of people {}'.format(type(people_dict)))

    return {
        'statusCode': 200,
        'headers': {
            "Content-Type": 'application/json'
        },
        'body': json.dumps({'people': people_dict})
    }


response = create_response()
print('type of response {}'.format(type(response)))
print(response)
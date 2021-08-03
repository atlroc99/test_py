import json


def test_dictionary():
    print('test')
    string_params = {
        'object_name': 'resposne.json'
    }

    if string_params is None:
        print('string param is null')

    if 'object_name' not in string_params or not string_params['object_name']:
        print('string_param dictionary does NOT have object_name')
    else:
        print('string_params {}'.format(string_params))
        print('everything okay and object_name:  {}'.format(string_params['object_name']))


# test_dictionary()


def dict_keys_to_list():
    keeping_five = []
    with open(file='../json_files/keep5PredefinedImagesPath.json', mode='r') as f:
        for path in json.load(f)["paths"]:
            keeping_five.append(path['name'])

    print(f'type of keeping five: {type(keeping_five)}')
    print(keeping_five)


dict_keys_to_list()

people_list = []


def add_dictionary():
    data_str = {
        "bas/instanceportal": 8,
        "ivupro/addons": 5,
        "ivupro/content": 6,
        "ivupro/drivers": 3,
        "ivupro/factoryapplications": 18,
        "ivupro/sals": 30
    }

    template = {
        "names": [
            {
                "name": "",
                "age": 0,
                "gender": ""
            }
        ]
    }

    # keys = data_str.keys()
    name_dict = template["names"][0]
    print(name_dict)
    for key in data_str.keys():
        print('processing key: {}'.format(key))
        name_dict["name"] = key
        name_dict_copy = name_dict.copy()
        people_list.append(name_dict_copy)
    print('People list :', people_list)


'''
     items = [
         {
             "name": "Jon",
             "age": 20,
             "gender": "Male"
         },
         {
             "name": "David",
             "age": 32,
             "gender": "Male"
         },
         {
             "name": "Sheela",
             "age": 34,
             "gender": "Female"
         }
     ]
'''
add_dictionary()

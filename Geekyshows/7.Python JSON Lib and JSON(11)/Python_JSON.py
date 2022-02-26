import json

dict_data = {"a": 1, "b": 2, "c": 3}
print(dict_data)  # {'a': 1, 'b': 2, 'c': 3}
print(type(dict_data))  # <class 'dict'>

json_data = json.dumps(dict_data)
print(json_data)  # {"a": 1, "b": 2, "c": 3}
print(type(json_data))  # <class 'str'>

some_data = json.loads(json_data)
print(some_data)  # {'a': 1, 'b': 2, 'c': 3}
print(type(some_data))  # <class 'dict'>

list_data = ['hello', 'bye']
print(list_data)  # ['hello', 'bye']
print(type(list_data))  # <class 'list'>

another_data = json.dumps(list_data)
print(another_data)  # ["hello", "bye"]
print(type(another_data))  # <class 'str'>

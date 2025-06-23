import json


json_data = '{"1": {"name": "Rabin", "Age": 20}}'

print(type(json_data))

data = json.loads(json_data)

print(type(data))

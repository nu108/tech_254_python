import json
parsed_json = json.loads(open("example.json").read())
print(type(parsed_json))
value = parsed_json["website"]
print(value)


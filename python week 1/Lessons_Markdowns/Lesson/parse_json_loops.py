import json
parsed_json = json.loads(open("example.json").read())

for key in parsed_json:
    print(f"This is the key; {key}"This is the value:){parsed_json[key]}")"
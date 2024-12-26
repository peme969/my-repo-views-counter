import requests,json
repos = []
saved_data = []
try:
    with requests.get("https://api.github.com/users/peme969/repos") as r:
        for d in r.json():
          repos.append(d['name'])
        saved_data.append(r.status_code)
        saved_data.append(r.reason)
        saved_data.append(r.json())
except Exception as e:
    print('\033[31;1mRequest ERROR! Responses (order in - status code, error reason, response in json format): \033[0m')
    for i in saved_data:
        print(f' • {i}')
    print(f'Exception: {e}')
old_data = None
new_data = None
try:
    with open('config.json','r') as f:
        data = json.load(file)
    old_data = data
    data['repository'] = repos
    new_data = data
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
except Exception as e:
    print('\033[31;1mRequest ERROR! Responses (order in - data before edited, data after edits): \033[0m')
    print(old_data)
    print(new_data)
    print(f'Exception: {e}')
print("\033[1;32mConfig Updated! ✅\033[0m")

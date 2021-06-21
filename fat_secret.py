import requests
import json
import pandas as pd

responses = {}
food_items = []
file = open('food.txt', 'r')
for line in file:
    food_items.append(line.strip())

for food_item in food_items:
    try:
        urlId = "https://platform.fatsecret.com/rest/server.api"
        parametersId = {}
        parametersId["method"] = "foods.search"
        parametersId["format"] = "json"
        parametersId["search_expression"] = food_item
        headers = {}
        headers["Authorization"] = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEzRTFGRDgwMTQ0Q0IwQTI4NDRFMzI4REZCNUU4NTQyRDE0QUI2RUYiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJFLUg5Z0JSTXNLS0VUaktOLTE2RlF0Rkt0dTgifQ.eyJuYmYiOjE2MjM5OTE4NTIsImV4cCI6MTYyNDA3ODI1MiwiaXNzIjoiaHR0cHM6Ly9vYXV0aC5mYXRzZWNyZXQuY29tIiwiYXVkIjoiYmFzaWMiLCJjbGllbnRfaWQiOiI3ZGVhMzM3YTQzOTY0NzVjOTQ0OWUyMjc1NmMyZmU0OSIsInNjb3BlIjpbImJhc2ljIl19.LnUclOgB5R_w3JvmGr0fvsTw7vAFFkI6k7SQf7pSI_30m9ZByuRSBIfaJgg-ldDqZCe_TxXOa1FjDYHA-RPLN3fKqbqUeTxZhmAOpuaFdZleqX2LdrWPAn1-PnUsGg_cM4BHVbvv13SHOcsoEoYyx82eMdIloQjyDuG2a8H7L1rJy4GXYfMFyytS4WAkSDTK1UNCuT6XXsZ9RYqBXVFbYq3D2atAx81URLeKOXS9kUBTrbbEcu4AitnenQgcszJnwZkLNVoDcbyoUXUdmLThjLwQ-pl183R1bvneEaauewlzTan_FKqj1aleHv-UOXcGHbmG5cg10ZQyoWPLBusR1Q"
        res = requests.post(url=urlId, params=parametersId, headers=headers).json()
        food_list = []
        for each_item in res["foods"]["food"]:
            try:
                id = (int)(each_item["food_id"])
                parameters = {}
                parameters["method"] = "food.get.v2"
                parameters["format"] = "json"
                parameters["food_id"] = id
                res_food = requests.post(url=urlId, params=parameters, headers=headers).json()
                food_list.append(res_food["food"])
            except Exception as e:
                pass
        responses[food_item] = food_list
        print(food_item)
    except Exception as e:
        pass


import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(responses, f, ensure_ascii=False, indent=4)
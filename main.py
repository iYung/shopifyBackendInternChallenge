import requests as r

menus = []
validMenus = []
invalidMenus = []

page = 1

while True:
    response = r.get('https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2&page=' + str(page)).json()
    
    nodes = response["menus"]
    
    for node in nodes:
        if 'parent_id' not in node:
            menu = {"root_id": node["id"], "children": node["child_ids"]}
            menus.append(menu)
        else:
            for menu in menus:
                if node["parent_id"] == menu["root_id"] or node["parent_id"] in menu["children"]:
                    for child in  node["child_ids"]:
                        menu["children"].append(child)
    
    page += 1
    if response["pagination"]["per_page"] * response["pagination"]["current_page"] > response["pagination"]["total"]:
        break

for menu in menus:
    if menu["root_id"] in menu["children"]:
        invalidMenus.append(menu)
    else:
        validMenus.append(menu)

answer = {"valid_menus": validMenus, "invalid_menus": invalidMenus}

print answer
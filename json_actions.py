import json


def find_item(dictionnary, name, file):
    with open(file, encoding='utf-8') as data:
        dictionaries = json.load(data)

        for item in dictionaries[dictionnary]:
            if item["name"] == name:
                return item


def get_allitems(dictionnary, file):
    with open(file, encoding='utf-8') as data:
        dictionaries = json.load(data)
        try:
            return dictionaries[dictionnary]
        except Exception as e:
            print(
                f"exception occurred \"{e}\" (propably dictionnary doesn't exist)")


def add_item(dictionnary, item, file):
    with open(file, mode='r', encoding='utf-8') as data:
        dictionaries = json.load(data)
        dictionaries[dictionnary].append(item)

    with open(file, mode='w', encoding='utf-8') as data:
        json.dump(dictionaries, data)

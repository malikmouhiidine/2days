from json_actions import find_item
from helpers import dictionaries_path
import webbrowser


def execute(command, exp=False):
    item = find_item("commands", command, dictionaries_path)

    if item["type"] == "direct_link":
        webbrowser.open(item["link"])

    elif item["type"] == "search_page":
        webbrowser.open(item["query_url"] + exp)

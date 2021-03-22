from json_actions import find_item
from helpers import dictionaries_path
import os
import platform
import webbrowser


def execute(command, exp=False):
    item = find_item("commands", command, dictionaries_path)

    if item["type"] == "direct_link":
        webbrowser.open(item["link"])

    elif item["type"] == "search_page":
        webbrowser.open(item["query_url"] + exp)

    elif item["type"] == "local_forder/file":
        if platform.system() == "Linux":
            os.system(fr'xdg-open "{item["path"]}"')
        elif platform.system() == "Darwin":
            os.system(fr'open "{item["path"]}"')
        elif platform.system() == "Windows":
            os.system(fr'start "" "{item["path"]}"')

from web_actions import execute
from json_actions import get_allitems, add_item
from helpers import dictionaries_path


def commander(expression):
    for index, command in enumerate(expression):
        if command == "-add-command":
            add_command()
        elif command == "-list":
            list_commands()
        elif command == "-help":
            print_help()
        elif command in commands():
            try:
                command_exp = expression[index + 1]
                execute(command, expression[index + 1])
            except IndexError:
                execute(command)


def add_command():
    command_type = input(
        "type of the command (direct_link, search_page, local_forder/file): ")
    name = input("name of the command: ")
    if command_type == "direct_link":
        link = input("what's the link: ")
        add_item("commands", {"type": command_type,
                 "name": name, "link": link}, dictionaries_path)
    elif command_type == "search_page":
        query_url = input(
            "what's the query url e.g (http://www.google.com/search?q=): ")
        add_item("commands", {"type": command_type,
                 "name": name, "query_url": query_url}, dictionaries_path)
    elif command_type == "local_forder/file":
        path = input(
            "what's the path to the folder or path: ")
        add_item("commands", {"type": command_type,
                 "name": name, "path": path}, dictionaries_path)


def commands():
    commands = []
    for command in get_allitems("commands", dictionaries_path):
        commands.append(command["name"])
    return commands


def list_commands():
    commands = []
    for command in get_allitems("commands", dictionaries_path):
        commands.append(command["name"])
    for command in commands:
        print(command)
    print("if you want to list all commands with more information use -help")


def print_help():
    commands = []
    for command in get_allitems("commands", dictionaries_path):
        commands.append(command)
    for command in commands:
        if command["type"] == "direct_link":
            print(
                f'name is: {command["name"]} type is: {command["type"]} and open: {command["link"]}')
        if command["type"] == "search_page":
            print(
                f'name is: {command["name"]} type is: {command["type"]} and open: {command["query_url"]} + a search term provided')
        if command["type"] == "local_forder/file":
            print(
                f'name is: {command["name"]} type is: {command["type"]} and open: {command["path"]}')

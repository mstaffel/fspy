"""Console script for fspy."""
# import argparse
import sys
from fspy import FileSystem


def main():
    """Console script for fspy."""
    # parser = argparse.ArgumentParser()
    # parser.add_argument('_', nargs='*')
    # args = parser.parse_args()

    user_response = input("Create an in memory FileSystem? <y> ")

    if user_response != "y":
        return 0
    else:
        print_help()
        user_interactive_shell()

    return 0


def user_interactive_shell() -> int:
    file_system = FileSystem()

    while(True):
        user_response = input("$ ")

        if user_response in ["exit", "q"]:
            return 0

        if user_response in ["help", ""]:
            print_help()
            continue

        split_response = user_response.split(" ")
        if len(split_response) > 1:
            if split_response[0] in ["make", "get", "change", "delete"]:
                handle_crud(split_response, file_system)
                continue
            else:
                print_error_help()
                continue
        else:
            print_error_help()

    return 0


def handle_crud(split_response: list, file_system: FileSystem) -> None:
    if len(split_response) not in [3, 4]:
        print_error_help()
        return

    # change directory to <child directory name>
    if (split_response[0:2] == "change directory to" and
            len(split_response) == 4):
        file_system.move_up_one_directory(split_response[3])
        return

    # change directory to parent
    if " ".join(split_response) == "change directory to parent":
        file_system.move_to_parent()
        return

    # make <directory name> directory
    if split_response[0] == "make" and split_response[2] == "directory":
        file_system.make_directory(split_response[1])
        return

    # get working directory
    if " ".join(split_response) == "get working directory":
        working_directory = file_system.current_directory.path
        print(working_directory)
        return

    # get working directory contents
    if " ".join(split_response) == "get working directory contents":
        contents = file_system.current_directory.children
        print("\n".join(contents.keys()))
        return

    print_error_help()
    return


def print_help() -> None:
    for command in commands:
        print(command + " : " + commands[command])
    return


def print_error_help() -> None:
    print("Syntax error, the possible commands are: \n")
    print_help()
    return


global commands
commands = {
    "make <filename> file": "Create a new file",
    "make <directory> directory": "Create a new directory",
    "get working directory": "Print current directory path",
    "get working directory contents": "Print current directory's contents",
    "change directory to <directory>": "Change directory to given directory",
    "change directory to parent": "Change directory to parent directory",
    "delete <directory> directory": "Delete given directory"
    "if directory in current directory",
    "exit or q": "Close the program"
}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

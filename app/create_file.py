import sys
import os
import datetime


def define_path() -> dict:
    current_flag = ""
    file_name = ""
    directories = []

    for arg in sys.argv[1:]:
        if arg == "-f":
            current_flag = "-f"
            continue
        elif arg == "-d":
            current_flag = "-d"
            continue

        if current_flag == "-f":
            file_name = arg
        else:
            directories.append(arg)

    return {
        "dir": "/".join(directories),
        "file": file_name
    }


def create_file() -> None:
    path_dict = define_path()
    if path_dict["dir"]:
        os.makedirs(path_dict["dir"], exist_ok=True)

    if path_dict["file"]:
        file_path_base = os.path.join(path_dict["dir"], path_dict["file"])
        file_path = os.path.normpath(file_path_base)
        mode = "w"
        if os.path.isfile(file_path):
            mode = "a"

        with open(file_path, mode) as file:
            if mode == "a":
                file.write("\n\n")
            file.write(
                f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            )
            line_counter = 1
            input_text = input("Enter content line: ")
            while input_text != "stop":
                file.write(f"\n{line_counter} ")
                file.write(input_text)
                line_counter += 1
                input_text = input("Enter content line: ")


create_file()

import sys
import os
import datetime

def create_file() -> None:
    sys_args_len = len(sys.argv)
    flags = [sys_args_len, sys_args_len]
    if "-d" in sys.argv:
        flags[0] = sys.argv.index("-d")
    if "-f" in sys.argv:
        flags[1] = sys.argv.index("-f")
    
    directories = ""
    if "-d" in sys.argv:
        directories = "/".join(sys.argv[flags[0] + 1: flags[1]])
        directories += "/"
        os.makedirs(directories, exist_ok=True)

    if "-f" in sys.argv:
        file_name = directories + sys.argv[flags[1] + 1]
        mode = "w"
        if os.path.isfile(file_name):
            mode = "a"

        with open(file_name, mode) as file:
            if mode == "a":
                file.write("\n\n")
            file.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            line_counter = 1
            input_text = input("Enter content line: ")
            while input_text != "stop":
                file.write(f"\n{line_counter} ")
                file.write(input_text)
                line_counter += 1
                input_text = input("Enter content line: ")


create_file()
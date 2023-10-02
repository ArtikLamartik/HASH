from tkinter import *
import time
global inp
with open("hash_input.txt", "r") as file:
    a = file.read()
    file.close()
    pass
with open('hash_output.txt', 'w') as file:
    file.truncate(0)
words = a.split()
if not words:
    with open("hash_output.txt", "a") as file:
        file.write("Error: Input file is empty.")
        file.close()
    exit()
first_word = words[0]
last_word = words[-1]
if first_word.lower() == "!go!":
    if last_word.lower() == "!end!":
        commands = words[1:-1]
        for command in commands:
            if "var=" in command:
                var = command.split("var=")[1].split()[0]
            elif "show=" in command:
                show = command.split("show=")[1].split()[0]
                if show == "var":
                    if not var:
                        with open("hash_output.txt", "a") as file:
                            file.write("Error: You forgot about the var.")
                            file.close()
                        exit()
                    with open("hash_output.txt", "a") as file:
                        file.write(var)
                        file.close()
                        pass
                if show == "input":
                    if not input_a:
                        with open("hash_output.txt", "a") as file:
                            file.write("Error: You forgot about the input.")
                            file.close()
                        exit()
                    with open("hash_output.txt", "a") as file:
                        file.write(input_a)
                        file.close()
                        pass
                if show == "rand":
                    if not w or not x or not y or not z:
                        with open("hash_output.txt", "a") as file:
                            file.write("Error: You forgot about the random.")
                            file.close()
                        exit()
                    with open("hash_output.txt", "a") as file:
                        file.write(w)
                        file.close()
                        pass
                    with open("hash_output.txt", "a") as file:
                        file.write(x)
                        file.close()
                        pass
                    with open("hash_output.txt", "a") as file:
                        file.write(y)
                        file.close()
                        pass
                    with open("hash_output.txt", "a") as file:
                        file.write(z)
                        file.close()
                        pass
            elif "print=" in command:
                print_v = command.split("print=")[1].split()[0]
                with open("hash_output.txt", "a") as file:
                    file.write(print_v)
                    file.close()
                    pass
            elif "input=" in command:
                input_v = command.split("input=")[1].split()[0]
                input_a = input(input_v)
            elif "rendom_num" in command:
                w = "3 random numbers"
                import random
                x = random.getrandbits(5)
                y = random.getrandbits(7)
                z = random.getrandbits(10)
            elif "open_window=" in command:
                open_wd = command.split("open_window=")[1].split()[0]
                if "in_window=" in open_wd:
                    in_wd = open_wd.split("in_window=")[1].split()[0]
                    title_v, size, bg_clr = map(str, in_wd.split(","))
                    width, height = map(str, size.split("x"))
                    new_window = Tk()
                    new_window.title(title_v)
                    new_window["background"] = f"{bg_clr}"
                    new_window.geometry(f"{width}x{height}")
                    new_window.mainloop()
                with open("hash_output.txt", "a") as file:
                    file.write("Invalid Syntax.")
                    file.close()
                    pass
            elif "wait=" in command:
                wait = float(command.split("wait=")[1].split()[0])
                time.sleep(wait)
            elif "if=" in command:
                if_v = command.split("if=")[1].split()[0]
                what_v, what_with_what_v, a_nr_txt, trueness, what_to_do = map(str, if_v.split(","))
                result = False
                if what_v == "var":
                    if not var:
                        with open("hash_output.txt", "a") as file:
                            file.write("Error: You forgot about the var.")
                            exit()
                    else:
                        if trueness == "true":
                            if what_with_what_v == "=":
                                result = var == a_nr_txt
                            elif what_with_what_v == ">":
                                result = var > a_nr_txt
                            elif what_with_what_v == "<":
                                result = var < a_nr_txt
                            elif what_with_what_v == "!=":
                                result = var != a_nr_txt
                        if trueness == "false":
                            if what_with_what_v == "=":
                                result = var != a_nr_txt
                            elif what_with_what_v == ">":
                                result = var < a_nr_txt
                            elif what_with_what_v == "<":
                                result = var > a_nr_txt
                            elif what_with_what_v == "!=":
                                result = var == a_nr_txt
                        if "put.out=" in what_to_do:
                            put_out_v = what_to_do.split("put.out=")[1].split()[0]
                            with open("hash_output.txt", "a") as file:
                                if result == True:
                                    file.write(put_out_v)
                                if result == False:
                                    file.write("false")
                                file.close()
                            pass
                if what_v == "input":
                    if not input_v:
                        with open("hash_output.txt", "a") as file:
                            file.write("Error: You forgot about the input.")
                            exit()
                    else:
                        if trueness == "true":
                            if what_with_what_v == "=":
                                result = input_a == a_nr_txt
                            elif what_with_what_v == "!=":
                                result = input_a != a_nr_txt
                        if trueness == "false":
                            if what_with_what_v == "=":
                                result = input_a != a_nr_txt
                            elif what_with_what_v == "!=":
                                result = input_a == a_nr_txt
                        if "put.out=" in what_to_do:
                            put_out_v = what_to_do.split("put.out=")[1].split()[0]
                            with open("hash_output.txt", "a") as file:
                                if result == True:
                                    file.write(put_out_v)
                                file.close()
            elif "new.l" in command:
                with open("hash_output.txt", "a") as file:
                    file.write("\n")
                    file.close()
                    pass
            else:
                with open("hash_output.txt", "a") as file:
                    file.write("Invalid Syntax.")
                    file.close()
                    pass
    else:
        with open("hash_output.txt", "a") as file:
            file.write("Error: '!end!' is the ending word.")
            file.close()
            pass
else:
    with open("hash_output.txt", "a") as file:
        file.write("Error: '!go!' is the starting word.")
        file.close()
        pass

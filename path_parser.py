import re


# простой вариант если нет точек в пути и расширение не пустое
def path_parser(user_line : str) -> ():
    *path, name, extension = re.split(r"[\\.]", user_line)
    path = "\\".join(path)
    return (path, name, extension)


# вариант если есть точки и/или нет расширения файла
def path_parser_1(user_line : str) -> ():
    *path, file = user_line.split("\\")
    path = str("\\".join(path) + "\\")
    if len(file.split(".")) == 1:
        name, extension = file, ""
    elif len(file.split(".")) == 2:
        name, extension = file.split(".")
    else:
        *name, extension = file.split(".")
        name = str(".".join(name))
    return (path, name, extension)


path = r"C:\%USERPROFILE%\Saved Games\CD Projekt Red\Cyberpunk 2077\sa.ve.sav"
# path = r"C:\%USER.PROFILE%\Saved Games\CD Projekt Red\Cyberpunk 2077\save"
print(path_parser_1(path))

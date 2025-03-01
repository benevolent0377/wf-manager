import re


# a python file to check input syntax and limit erroneous inputs

def basic(text, isLoop=False):
    if isLoop:

        out = []
        count = 0
        while len(text) > count:
            out.append(text[count].strip())
            count += 1
        return out

    else:
        return text.strip()


def adv(text, chk="", isLoop=False, isCustom=False, toLower=False, title=False, regex=False, regexStr=""):
    if isCustom or regex or chk == "custom":

        if regex and regexStr != "":

            if isLoop:
                count = 0
                err = 0

                if isLoop:
                    while len(text) > count:

                        if re.search(regexStr, text) is None:
                            err = 1
                else:
                    if re.search(regexStr, text) is None:
                        err = 1

                if err == 0:

                    return True

                else:

                    return False

            else:
                if re.search(regexStr, text) is not None:
                    return basic(text)
        else:

            if toLower:
                text = text.lower()
            if title:
                text = text.title()

            return basic(text)

    else:

        match chk:

            case "internal":

                if isLoop:

                    out = []
                    count = 0
                    while len(text) > count:
                        out.append(text[count].lower().strip())
                        count += 1

                    return out
                else:
                    return text.lower().strip()

            case "filename":

                invChars = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '{', '[', '}', '}',
                            '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '?', '/']

                if isLoop:

                    out = []
                    count = 0

                    while len(text) > count:
                        letters = list(text[count].replace(" ", "_"))
                        for letter in letters:
                            for char in invChars:
                                if char.__eq__(letter):
                                    text[count] = text[count].replace(letter, "")

                        out.append(text[count])
                        count += 1

                    return out

                else:

                    letters = list(text.replace(" ", "_"))

                    for letter in letters:
                        for char in invChars:
                            if char.__eq__(letter):
                                text = text.replace(letter, "")

                    return text

            case "nosymb":

                invChars = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[',
                            '}', '}', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/']

                if isLoop:

                    out = []
                    count = 0

                    while len(text) > count:
                        letters = list(text[count])
                        for letter in letters:
                            for char in invChars:
                                if char.__eq__(letter):
                                    text[count] = text[count].replace(letter, "")

                        out.append(text[count])
                        count += 1
                    return out

                else:

                    letters = list(text)
                    for letter in letters:
                        for char in invChars:
                            if char.__eq__(letter):
                                text = text.replace(letter, "")

                    return text

            case "dir":
                invChars = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[',
                            '}', '}', '|', ':', ';', '"', '\'', '<', ',', '>', '.', '?']

                if isLoop:

                    out = []
                    count = 0

                    while len(text) > count:
                        letters = list(text[count])
                        for letter in letters:
                            for char in invChars:
                                if char.__eq__(letter):
                                    text[count] = text[count].replace(letter, "")

                        out.append(text[count])
                        count += 1
                    return out

                else:

                    letters = list(text)
                    for letter in letters:
                        for char in invChars:
                            if char.__eq__(letter):
                                text = text.replace(letter, "")

                    return text

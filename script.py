###--- IMPORTS ---###
import re

###--- FUNCTIONS ---###


def check_url_validity_(userinput):
    # regular expression to check if URL is valid
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([a-zA-Z0-9@:%._\\+~#?&//=]*)")

    compiled = re.compile(regex)

    if userinput == None or userinput == '':
        return False

    else:
        if re.search(compiled, userinput):
            return True
        else:
            return False


###--- DRIVER CODE ---###
if __name__ == "__main__":
    userinput = input("Please enter a URL and hit Enter: ")
    if check_url_validity_(userinput) == True:
        print("Valid.")
    else:
        print("Not valid.")

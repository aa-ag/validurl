###--- IMPORTS ---###
import re
import requests


###--- FUNCTIONS ---###

# [!] This approached is flawed as many thins can be considered valid URLs
# It also requires more work to try to catch all posissibilities via regex

# def check_url_validity(userinput):
#     # regular expression to check if URL is valid
#     regex = ("((http|https)://)(www.)?" +
#              "[a-zA-Z0-9@:%._\\+~#?&//=]" +
#              "{2,256}\\.[a-z]" +
#              "{2,6}\\b([a-zA-Z0-9@:%._\\+~#?&//=]*)")

#     compiled = re.compile(regex)

#     if userinput == None or userinput == '':
#         return False

#     else:
#         if re.search(compiled, userinput):
#             return True
#         else:
#             return False


def check_url_validity(userinput):
    response = requests.get(userinput)
    if response.status_code < 400:
        print("Valid.")
    else:
        print("Not valid.")


###--- DRIVER CODE ---###
if __name__ == "__main__":
    userinput = input("Please enter a URL and hit Enter: ")
    check_url_validity(userinput)
    # if check_url_validity(userinput) == True:
    #     print("Valid.")
    # else:
    #     print("Not valid.")

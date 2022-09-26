import re

print("Path not defined. Which file do you want to evaluate?")
print("README.md = 1, Other = 2")
answer = input()
if answer == "1":
    path = "C:/Vault/README.md"
elif answer == "2":
    print("What's the file's path?")
    path = input()
    print(path)

with open(path, "r") as f1:    
    file = f1.read()
    nox = file.count("- [ ]")
    x = file.count("[x]")
    max = nox + x
    xstring = ["id=\"progress-bar\" value=\"", x, "\" max=\"", max, "\""]
    xstring = str(xstring)
    xstring = "".join(xstring)
    xstring = xstring.replace("', ", "")
    xstring = xstring.replace(", '", "")
    xstring = xstring.replace("['", "")
    xstring = xstring.replace("']", "")

with open(path, "r") as f1:
    lines = f1.readlines()
    with open(path,'w') as f2:
        for x in range(len(lines)):
            lines[x] = re.sub("id=\"progress-bar\" value=\"\d+\" max=\"\d+\"", xstring, lines[x])
        f2.writelines(lines)

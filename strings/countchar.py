s="Fgh^f#89"
spaces=0
def countspchar(s):
    spchar=0
    regex="[^a-zA-Z0-9]+"
    for char in s:
        if char in regex:
            spchar+=1
    return spchar
def countspaces(s):
    spaces=0
    if s.find(' '):
        spaces+=1
    return spaces

print(s)
schar=countspchar(s)
spa=countspaces(s)
print("no. of special charcters:",schar)
print("no. of spaces:",spa)

import re

infile = open('nodisc.txt', 'r', encoding="utf8")   # input file
outfile = open('texts.txt', 'w', encoding="utf8")   # file with texts only will be saved here
members = open('groupMembers.txt', 'w', encoding="utf8")             # group members will be saved in this file
timeStamp = open('timezone.txt', 'w', encoding="utf8")


regex = r"(\d{1,2}\/\d{1,2}\/\d{2,4}), (\d{1,2}\:\d{2}\s\w\.?\w\.?) - ([a-z0-9 \S]+?): ((?:[^\/]+(?:\n|$))+)"

test_str = infile.read()    # the entire text file in string
groupMembers = []           # list for group members

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    if match.group(3) not in groupMembers:      # if username doesn't already exit in groupMembers
        groupMembers.append(match.group(3))     # add username to groupMembers list
    outfile.writelines(match.group(4))          # saving all texts in a file
    timeStamp.write(match.group(1) + ' ' + match.group(2) + '\n')


outfile.close()

texts = open('texts.txt', 'r', encoding="utf8")

for x in range(len(groupMembers)):      # to remove any repeating names and false sentences
    counter = groupMembers[x].count(' ')
    if counter > 3:
        groupMembers[x] = ''               # replaces the false indexes with blank space

while '' in groupMembers:               # to remove the empty indexes in the string
    groupMembers.remove('')

groupMembers.sort()                     # sorting before storing

for x in range(len(groupMembers)):      # storing group members names in file.
    members.write(groupMembers[x])
    members.write("\n")

print("Group Members: ")
for x in range(len(groupMembers)):
    print(groupMembers[x])

infile.close()
texts.close()
members.close()
timeStamp.close()

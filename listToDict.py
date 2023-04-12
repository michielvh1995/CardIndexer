import re

card_regex = re.compile('(?!(#* ))((\d\d?\d?)x )?(.*)')

cardDict = {}
with open('./cardlist.txt') as cardfile:
    for l in cardfile:
        match = card_regex.match(l.lower())

        # If we have a match in the regex
        if match: 
            matchGroups = match.groups()

            # Count how many cards we have
            count = int(matchGroups[-2]) if matchGroups[-2] is not None else 1

            # Update the card dict:
            if matchGroups[-1] in cardDict:
                cardDict[matchGroups[-1]] += count
            else:
                cardDict[matchGroups[-1]] = count
            
num = 0
for k in cardDict.keys():
    print('{' + f" id: {num}, name: \"{k}\", count: {cardDict[k]}"  + '},')
    num += 1

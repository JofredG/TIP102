print("_____________________Problem 1:")
# Understand: Given dictionary. Return total value of dictionary values
# Plan: 
def total_treasures(treasure_map):
    total = 0
    #for treasure in treasure_map.values():
    #    total += treasure
    total = sum(treasure_map.values())
    return total



treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2))


print("_____________________Problem 2:")
#Understand: given message check for every letter in alphabet
#Plan: Use a for loop to iterate through ea char in string and check if it's in the set. Check size of set at the end == 26
#Time and space: O(n) O(1) bc O(26) 
def can_trust_message(message):
    alpha = set()
    for char in message:
        if char != ' ':
            alpha.add(char)
    #print(alpha)
    return len(alpha) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))




print("_____________________Problem 3:")
#understand: if not in set add, if in set add to results list
#Time and space: O(n) O(n) where n is the length of chests
def find_duplicate_chests(chests):
    track = set()
    res = []
    for val in chests:
        if val in track:
            res.append(val)
        else:
            track.add(val)
    return res


chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))


print("Problem 4: Booby Trap")
#Understand
#Plan: Use two dictionaries. Iterate through the the message tracking
def is_balanced(code):
    d1 = dict()
    d2 = dict()
    for char in code:
        


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

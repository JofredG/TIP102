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
print(treasure_map1["Cove"]) 


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
#1) Create a frequency dictionary (`freq_dict`) to count how often each character appears in the code.
#2) Create a frequency of frequencies dictionary (`frequency_count`) to count how often each frequency appears in `freq_dict`.
#3) Determine the number of unique frequencies.

#4) If there are three or more unique frequencies, it's impossible to balance the code by removing just one letter, so return `False`.
#5) If there's only one unique frequency:
#    - If all characters are the same or have a frequency of 1, return `True`.
#6) If there are exactly two unique frequencies, check if removing one letter can balance the remaining letters:
#    - If one frequency is 1 and it occurs exactly once, return `True`.
#    - If the difference between the two frequencies is 1 and the higher frequency occurs exactly once, return `True`.
#7) If none of the conditions are met, return `False`.

def is_balanced(code):
    freq_dict = {}
    frequency_count = {}
    for char in code:
        if char not in freq_dict:
            freq_dict[char] = 1
        elif char in freq_dict:
            freq_dict[char] = freq_dict[char] + 1
    for _, value in freq_dict.items():
        if value not in frequency_count: 
            frequency_count[value] = 1
        elif value in frequency_count:
            frequency_count[value] = frequency_count[value] + 1
    if len(frequency_count) > 2:
        return False

    if len(frequency_count) == 2:
        a, b = frequency_count.items()
        if abs(a.value - b.value) == 1:
            return True

    if len(frequency_count) == 1:
        return True

        


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

'''
Understand
    Inputs: int list
    Output: int describing longest balanced subsequence
    Constriants: Balanced means the diff between max and min is exactly 1
    Edge cases:

    Given a list of ints find a subsequence that 

    Loop through array adding it to dict
'''

def find_balanced_subsequence(art_pieces):
    pass


art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

def find_balanced_subsequence(art_pieces):
    freq = {}
    for item in art_pieces:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    max = 0
    for i in freq:
        if i + 1 in freq:
            if freq[i] + freq[i + 1] > max:
                max = freq[i] + freq[i + 1]
    return max


art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]
print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))



def is_authentic_collection(art_pieces):
    freq = {}
    #add to dictionary
    for item in art_pieces:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    #find max key to check frequency of 2 later
    max_key = max(art_pieces)
    #for every key,
    for key in freq:
        #if it isn't the max key, if the frequncy isn't 1, return False
        if key != max_key:
            if freq[key] != 1:
                return False
        #if it IS the max key, if the frequncy isn't 2, return False         
        elif key == max_key:
            if freq[key] != 2:
                return False
    return True

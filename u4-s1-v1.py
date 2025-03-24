'''
Input - List of dictionaries with 'name' and other keys
Output - List of all the names given by the dictionaries found in the input list.
Constrains - No Time or Space constraints
Edge Cases - Empty input list (no dictionaries)
Match - Lists, and Dictionaries
Plan - Iterate through the input list looking at the 'name' keys and appending them
to the resulting list.
Implementation: Seen below

Evaluation - Time: O(n) Space: O(n) since we store the answers in a new list
'''

print('______________________________________Problem 1')
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))



'''
Input - List of dictionaries with 3 Key Value Pairs
Output - List of dictionary element names
'''
print('______________________________________Problem 2')
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        print(nft["name"])
        nft_names += [nft["name"]] #for some reason we need to use [] around the value to be returned so that it can be properly appended to a list.
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))



print('______________________________________Problem 3')
'''
Input - List of dictionaries
Output - The name value of the dictionary element who's 'creator' value appears the most.
'''
def identify_popular_creators(nft_collection):
    d = {}
    for nft in nft_collection:
        if nft['creator'] not in d:
            d[nft['creator']] = 1
        elif nft['creator'] in d:
            d[nft['creator']] += 1
    tupel = zip(d.keys(), d.values())
    print(list(tupel))

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))

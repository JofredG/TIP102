print('')
'''
for every brand in the list we look at it's criteria and check if it matches our input criterion. If the criterion matches we append the name to our 'ans' list.

Time: O(n^2) Space: O(n)
'''
def filter_sustainable_brands(brands, criterion):
    ans = []
    #sustainable = set(['eco-friendly', 'ehtical labor', 'carbon-neutral'])
    for brand in brands:
        for criteria in brand['criteria']:
            if criteria == criterion:
                ans.append(brand['name'])
                break
    return ans

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

print(filter_sustainable_brands(brands, "eco-friendly"))
print(filter_sustainable_brands(brands_2, "ethical labor"))
print(filter_sustainable_brands(brands_3, "carbon-neutral"))

print("_________________________Problem 2")
'''
Input - List of dictionaries
Output - Dictionary containing the frequency of ea material
Constraints - 
Edge Cases - Empty input list, No key for materials in given dictionary

Match - Using a dictionary to measure frequency of materials we want to return the fre of each material
Plan - Look through ea dictionary in input list and look through materials list using a dictionary to track the frequency of ea material.
Time: O(n^2) Space: O(n)
'''
def count_material_usage(brands):
    freq = {}
    for brand in brands:
        for mat in brand['materials']:
            freq[mat] = freq.get(mat, 0) + 1
    return freq

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))

print()


print()
"""
Input: list of dictionaries
Output: list (of string) of materials
Edge cases: empty input list or dictionaries does not have correct keys

Plan: build frequency list of materials. While we are building this,
check if the frequency > 1. If yes, we can append the brand name
immediately to result
Time: O(N^2), space: O(N)
"""

def find_trending_materials(brands):
    result = set()
    freq = {}
    for brand in brands:
        for mat in brand["materials"]:
            freq[mat] = freq.get(mat, 0) + 1
            # Check if frequency is > 1
            if freq[mat] > 1:
                result.add(mat)

    return list(result)

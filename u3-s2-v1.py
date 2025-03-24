'''
Understanding - given a list of ints return a sorted list using a queue
Plan - 
'''


from collections import deque
def blueprint_approval(blueprints):
    return blueprints.sort()

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 


'''
Understand: 

Plan: Using two pointers we check the current 

Time: O(n) + O(n) = O(n)
Space: O(n)
'''
print('Problem 2')
def build_skyscrapers(floors):
    s = []
    res = 0
    for floor in floors:
        if s:
            if s[-1] <= floor:
                s.append(floor)
            else:
                res = res + 1
                while s:
                    s.pop()
                s.append(floor)

        else:
            s.append(floor)
    #if s:
    #    res += 1
    return res + 1
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))


print('Problem 3')
def max_corridor_area(segments):
    pass




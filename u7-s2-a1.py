def check_stock(inventory, part_id):
    l, r, m = 0, len(inventory)-1, len(inventory)//2
    while l <= r:
        m = (l+r) // 2
        #m = l + (r - l) // 2
        if inventory[m] == part_id:
            return True
        elif inventory[m] < part_id:
            l = m + 1
        elif inventory[m] > part_id:
            r = m - 1
    return False

print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))


def check_stock(inventory, part_id):
    return helper(inventory, part_id, 0, len(inventory) - 1, len(inventory) // 2) 

def helper(inventory, part_id, l, r, m):
  if inventory[m] == part_id:
    return True
  elif l >= r:
    return False
  elif inventory[m] < part_id:
    return helper(inventory, part_id, m + 1, r, ((m + 1) + r) // 2)
  elif inventory[m] > part_id:
    return helper(inventory, part_id, l, m - 1, (l + (m-1)) // 2)

print(check_stock([1, 2, 5, 20, 12], 20))
print(check_stock([1, 2, 5, 20, 12], 100))


print('----------------------------')
def find_frequency_positions(transmissions, target_code):
    l, r = 0, len(transmissions) - 1
    while l <= r:
        m = (l + r) // 2
        if transmissions[m] == target_code:
            start, end = m, m
            # Expand to the left
            while start > 0 and transmissions[start - 1] == target_code:
                start -= 1
            # Expand to the right
            while end < len(transmissions) - 1 and transmissions[end + 1] == target_code:
                end += 1
            return (start, end)
        elif transmissions[m] < target_code:
            l = m + 1
        else:
            r = m - 1
    return (-1, -1)

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,8,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))

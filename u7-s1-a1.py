

# p1
def count_layers(sandwich):
    if len(sandwich) == 1:
        return 1
    
    return 1 + count_layers(sandwich[1])


sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))


# p2
def reverse_orders(orders):
    result = ""
    food_list = orders.split(" ")
    new_orders = help_reverse(food_list, result)

    final_result = new_orders[1:]
    return final_result

def help_reverse(orders, result):
    if not orders:
        return result
    result += " " + orders.pop()
    
    return help_reverse(orders, result)
    

print(reverse_orders("Bagel Sandwich Coffee"))
    
def reverse_orders_2(orders):
    if orders.find(" ") == -1:
        return orders + " "
    # print(orders)
    return reverse_orders_2(orders[(orders.index(" "))+1:]) + orders[:orders.index(" ")] + " "

print(reverse_orders_2("Bagel Sandwich Coffee"))


# p3
def can_split_coffee(coffee, n):
    if not coffee:
        return True
    if coffee[0] % n == 0:
        coffee.pop(0)
        return can_split_coffee(coffee, n)
    else:
        return False
    else:
        return False


print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))


# p4
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    merge_helper(sandwich_a, sandwich_b)
    return sandwich_a

def merge_helper(sandwich_a, sandwich_b):
    if not sandwich_a and not sandwich_b:
        return

    hold_a_next = sandwich_a.next
    hold_b_next = sandwich_b.next
    sandwich_a.next = sandwich_b
    
    sandwich_b.next = hold_a_next
    sandwich_a = sandwich_a.next
    if not sandwich_a:
        sandwich_b 
        merge_helper(sandwich_a, hold_b_next)



sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_c = Node('Bread')
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))

print_linked_list(merge_orders(sandwich_a, sandwich_b)) # Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
print_linked_list(merge_orders(sandwich_a, sandwich_c)) # Bacon -> Bread -> Lettuce -> Tomato


def merge_orders(sandwich_a, sandwich_b):
    merge_helper(sandwich_a, sandwich_b)
    return sandwich_a
def merge_helper(sandwich_a, sandwich_b):
    if not sandwich_a and not sandwich_b:
        return
    if not sandwich_b:
        return
    hold_a_next = sandwich_a.next
    hold_b_next = sandwich_b.next
    sandwich_a.next = sandwich_b
    if hold_a_next == None:
        return
    sandwich_b.next = hold_a_next
    sandwich_a = sandwich_b.next
    # if not sandwich_a:
    #     sandwich_b 
    merge_helper(sandwich_a, hold_b_next)


sandwich_a1 = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_a2 = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')
print_linked_list(merge_orders(sandwich_a1, sandwich_b))
print_linked_list(merge_orders(sandwich_a2, sandwich_c))

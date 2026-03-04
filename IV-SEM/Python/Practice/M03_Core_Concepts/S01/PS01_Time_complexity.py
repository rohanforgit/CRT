#linear search 
def linear_search(elements,target):
    for i in range(len(elements)):
        if target == elements[i]:
            return i
    return -1

print(linear_search([12,45,78,69,32],12))#o(1) time complextiy best case
print(linear_search([12,45,78,69,32],78))#o(5) time complexity average case
print(linear_search([12,45,78,69,32],68))#o(n) time complexity worst case

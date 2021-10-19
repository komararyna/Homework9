def search(num_list, num):
    for item in num_list:
        if item == num:
            return item
    else:
        return -1
print(search([1, 2, 3, 4, 5, 6, 78, 9, 0], 78))

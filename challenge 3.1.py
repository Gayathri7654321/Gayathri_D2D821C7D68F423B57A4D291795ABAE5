def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices
product_list = ["apple", "banana", "orange", "mango", "grape"]
target = "orange"
result = linear_search_product(product_list, target)
print("Product List:", product_list)
print("Target Product:", target)
print("Indices of '{}' in the Product List: {}".format(target, result))
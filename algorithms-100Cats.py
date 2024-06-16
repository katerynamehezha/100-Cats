def cats_with_hats(num_cats, num_rounds):
    hats = [False] * num_cats
    
    for round_num in range(1, num_rounds + 1):
        for cat in range(1, num_rounds + 1):
            if cat % round_num == 0:
                hats[cat - 1] = not hats[cat - 1]
                
    cats_with_hats = [cat + 1 for cat in range(num_cats) if hats[cat]]
    
    return cats_with_hats


num_cats = 100
num_rounds = 100
cats_with_hats_list = cats_with_hats(num_cats, num_rounds)
print("Cats with hats at the end:", cats_with_hats_list)


# Временная сложность: O(num_сats * num_rounds) 
# Пространственная сложность: O(num_cats) 
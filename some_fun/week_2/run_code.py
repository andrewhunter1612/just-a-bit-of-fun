from change_tuple import*

dict_test = {
        "name": ("Andrew",),
        "age": 29,
        "height": 194
    }

test_tuple = ("item", "thing", "this")
tuple_test_one = ChangeTuple(test_tuple)

print(tuple_test_one.add_item_to_tuple("new"))

# tuple_test = ("andrew", "steve")

# # dict_test["name"][0] = "James"
# print(tuple_test)

# tuple_replacement = []
# for item in tuple_test:
#     tuple_replacement+=item

# word_length = len(tuple_test[0])
# print(word_length)

# print("".join(tuple_replacement))

# tuple_test[1] = "James"

# tuple_test = "James"

# tuple_test = "James"
# print(type(tuple_test))
# print(tuple_test)


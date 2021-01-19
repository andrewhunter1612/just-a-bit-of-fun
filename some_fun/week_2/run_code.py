from change_tuple import*

dict_test = {
        "name": ("Andrew",),
        "age": 29,
        "height": 194
    }

test_tuple = ("item", "thing", "this")
tuple_test_one = ChangeTuple(test_tuple)

print(tuple_test_one.tuple)

tuple_test_one.add_item_to_tuple("new")

print(tuple_test_one.tuple)
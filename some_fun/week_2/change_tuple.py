

class ChangeTuple:
    def __init__(self, tuple):
        self.tuple = tuple
        

    def add_item_to_tuple(self, new_item):
        new_tuple = []
        word_number = 0
        while word_number < self.get_tuple_length():
            new_tuple.append(self.tuple[word_number])
            word_number += 1

        new_tuple.append(new_item)
        return tuple(new_tuple)


    def get_tuple_length(self):
        return len(self.tuple)
    

    
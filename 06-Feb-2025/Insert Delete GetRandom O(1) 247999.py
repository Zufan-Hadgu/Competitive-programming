# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/


class RandomizedSet:

    def __init__(self):
        self.set_dict = {}
        self.list_element = list()

    def insert(self, val: int) -> bool:
        if not (val in self.set_dict):   
            self.set_dict[val] = len(self.list_element)
            self.list_element.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set_dict:
            remove_index = self.set_dict[val]
            self.list_element[remove_index], self.list_element[-1] = self.list_element[-1], self.list_element[remove_index]
            self.set_dict[self.list_element[remove_index]] = remove_index
            self.list_element.pop()
            del self.set_dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list_element)

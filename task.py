class FindDuplicates:
    def __init__(self, arr):
        self.arr = arr

    def find(self):
        seen = set()
        duplicates = set()

        for num in self.arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)

        return duplicates


# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 5, 8, 9, 10, 2, 11]
finder = FindDuplicates(arr)
print(finder.find())

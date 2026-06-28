import math


# ============================================================
# Daily Challenge : Pagination System
# ============================================================

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = items

        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number is out of range")

        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1

        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1

        return self

    def __str__(self):
        visible_items = self.get_visible_items()
        return "\n".join(visible_items)


# ============================================================
# Test your code
# ============================================================

alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabet_list, 4)

print("===== First page =====")
print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

print()

print("===== Next page =====")
p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

print()

print("===== Last page =====")
p.last_page()
print(p.get_visible_items())
# ['y', 'z']

print()

print("===== Go to page 10 =====")
try:
    p.go_to_page(10)
    print(p.current_idx + 1)
except ValueError as error:
    print(error)

print()

print("===== Go to page 0 =====")
try:
    p.go_to_page(0)
except ValueError as error:
    print(error)

print()

print("===== String display =====")
p.first_page()
print(str(p))
# a
# b
# c
# d

print()

print("===== Bonus chaining =====")
print(p.next_page().next_page().next_page().get_visible_items())
# ['m', 'n', 'o', 'p']

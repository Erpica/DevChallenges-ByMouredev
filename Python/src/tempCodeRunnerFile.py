class My_Queue:
    items = []

    def __init__(self, items: list):
        self.items = items

    def add_item(self, item: str):
        self.items.append(item)

    def add_item(self, item: int):
        self.items.append(item)

    def del_item(self):
        if (len(self.items) > 0):
            del(self.items[0])

    def del_item(self):
        if (len(self.items) > 0):
            del(self.items[0])

    def show_items(self):
        print(self.items)

one_queue = My_Queue(["file1", "file2"])
one_queue.show_items()
one_queue.add_item(3)
one_queue.show_items()
one_queue.del_item()
one_queue.show_items()
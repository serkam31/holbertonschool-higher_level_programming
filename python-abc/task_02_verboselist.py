class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Appended {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {iterable}.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item

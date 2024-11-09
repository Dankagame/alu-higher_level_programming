# 1-my_list.py

class MyList(list):
    """A subclass of list that adds a print_sorted method to print the list in sorted order."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))

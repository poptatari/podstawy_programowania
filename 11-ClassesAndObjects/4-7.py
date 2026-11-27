class Statistics:
    def __init__(self):
        self.collection = []

    def add_to_collection(self):
        try:
            number = float(input("Enter a number: "))
            self.collection.append(number)
        except ValueError:
            print("Must be a valid number.")

    def display_numbers(self):
        if len(self.collection) > 0:
            print(" ".join(str(x) for x in self.collection))
        else:
            print("Collection of numbers is empty")

    def greatest_num(self):
        if len(self.collection) > 0:
            return max(self.collection)
        return None

    def smallest_num(self):
        if len(self.collection) > 0:
            return min(self.collection)
        return None

    def mean(self):
        if len(self.collection) > 0:
            return sum(self.collection) / len(self.collection)
        return None

    def median(self):
        if len(self.collection) == 0:
            return None

        sorted_numbers = sorted(self.collection)
        n = len(sorted_numbers)

        if n % 2 == 0:
            return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        else:
            return sorted_numbers[n // 2]

    def print_calculated(self):
        if len(self.collection) == 0:
            print("Collection of numbers is empty")
            return

        print(
            f"Minimum: {self.smallest_num()}\n"
            f"Maximum: {self.greatest_num()}\n"
            f"Arithmetic mean: {self.mean()}\n"
            f"Median: {self.median()}"
        )


def main():
    stats = Statistics()

    # Read 5 numbers from the keyboard: 12, 37, 6, 9, 17
    for _ in range(5):
        stats.add_to_collection()

    print("\nNumbers:")
    stats.display_numbers()

    print("\nStatistics:")
    stats.print_calculated()


if __name__ == "__main__":
    main()
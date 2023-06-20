class NumberStats:
    def __init__(self):
        self.record = []

    def add_number(self, nb):
        self.record.append(nb)

    def count_numbers(self) -> int:
        return len(self.record)

    def get_sum(self):
        return sum(self.record)

    def average(self):
        try:
            return self.get_sum() / self.count_numbers()
        except:
            return 0


stats = NumberStats()
even_nb = NumberStats()
odd_nb = NumberStats()
print("Please type in integer numbers:")
while True:
    number = int(input())
    if number == -1:
        break
    stats.add_number(number)
    if number % 2 == 0:
        even_nb.add_number(number)
    else:
        odd_nb.add_number(number)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even_nb.get_sum())
print("Sum of odd numbers:", odd_nb.get_sum())

from kata1 import Dictionary
from kata2 import cost_calculation
from kata3 import construct_word

def run_katas():
    print("Kata 1")
    my_dict = Dictionary()
    my_dict.newentry("Car", "Four-wheeled vehicle powered by an engine")
    print(my_dict.look("Car"))

    print("Kata 2")
    costs = {"laptop": 100, "mouse": 25, "speakers": 38, "USB-C hub": "20"}
    items = ["laptop", "speakers"]
    tax = 0.08
    print(cost_calculation(costs, items, tax))

    print("Kata 3")
    words = ["banana", "apple", "grapes", "watermelon"]
    print(construct_word(words))

if __name__ == "__main__":
    run_katas()




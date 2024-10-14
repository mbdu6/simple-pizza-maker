import os
import time

# Prices for additional toppings
pricem = {
    'Sweetcorn': 0.65,
    'Pepperoni': 0.39,
    'Chicken': 0.35,
    'Pineapple': 0.23,
    'Mushroom': 0.68
}

customized_pizzas = {
    'Margherita': (['Cheese', 'Tomato Sauce'], 8, 4.00),
    'Pepperoni Delight': (['Cheese', 'Tomato Sauce', 'Pepperoni'], 12, 5.75),
    'BBQ Chicken': (['Cheese', 'BBQ Sauce', 'Chicken'], 12, 5.75),
    'Veggie Supreme': (['Cheese', 'Tomato Sauce', 'Sweetcorn', 'Mushroom', 'Pineapple'], 16, 7.50),
    'Tropical': (['Cheese', 'Tomato Sauce', 'Pineapple', 'Chicken'], 16, 7.50)
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_receipt(order, total, change):
    clear_terminal()
    print("========== RECEIPT ==========")
    print(f"Pizza Type: {order[0].capitalize()}")
    print("\nToppings Selected:")
    for topping in order[1:]:
        print(f"  - {topping}")
    print("\n-----------------------------")
    print(f"Total: £{total:6.2f}")
    if change > 0:
        print(f"Change: £{change:6.2f}")
    print("==============================")
    print("Thank you for your order!")
    print("==============================")
    print("\n      🍕🍕🍕")
    print("\n       Enjoy your meal!\n")

def loading_animation(message="Cooking your pizza"):
    clear_terminal()
    print("MA's Pizza Place")
    print("-------------------")
    print(f"{message}", end="", flush=True)
    animation = ['[■□□□□]', '[■■□□□]', '[■■■□□]', '[■■■■□]', '[■■■■■]']
    for i in range(5):
        print(f"\r{message} {animation[i]}", end="", flush=True)
        time.sleep(0.6)
    print("\n\nYour pizza is ready! Enjoy!\n")

def get_money_input():
    while True:
        try:
            money = float(input("Enter the amount you are paying (Max £50): £"))
            if money > 50:
                print("Maximum denomination is £50!")
            else:
                return money
        except ValueError:
            print("Invalid input! Please enter a valid amount.")

def calculate_total(order_size, toppings):
    total = 0
    if order_size == 'small':
        total = 4.00
    elif order_size == 'medium':
        total = 5.75
    elif order_size == 'large':
        total = 7.50
    elif order_size == 'custom':
        diameter = int(input("Enter the diameter of your custom pizza in inches: "))
        total = diameter * 0.52

    for topping in toppings:
        total += pricem[topping]
    return total

def choose_customized_pizza():
    clear_terminal()
    print("========== Customized Pizzas ==========")
    print("Available Pre-Customized Pizzas:\n")
    
    for idx, (pizza, (toppings, size, price)) in enumerate(customized_pizzas.items(), start=1):
        print(f"[{idx}] {pizza} - Size: {size} inches - Price: £{price:.2f} - Toppings: {', '.join(toppings)}")
        print("-" * 50) 

    print("[6] Create Your Own Customized Pizza\n")

    while True:
        choice = input("Choose a pizza by number (1-6): ")
        if choice in [str(i) for i in range(1, 7)]:
            if choice == '6':
                return None 
            else:
                selected_pizza = list(customized_pizzas.keys())[int(choice) - 1]
                return selected_pizza, customized_pizzas[selected_pizza][0] 
        else:
            print("Invalid choice! Please select a valid number.")

def order_pizza():
    clear_terminal()
    money = get_money_input() 

    clear_terminal()
    print("========== MA's Pizza Place ==========")
    
    pizza_info = choose_customized_pizza()
    
    if pizza_info is None: 
        print("Select your pizza size:\n")
        print("[1] Small (8 inches) - £4.00")
        print("[2] Medium (12 inches) - £5.75")
        print("[3] Large (16 inches) - £7.50")
        print("[4] Custom Size (calculated by diameter)")
        
        order_size = input("\nEnter your choice (1-4): ").lower()
        size_map = {'1': 'small', '2': 'medium', '3': 'large', '4': 'custom'}
        order_size = size_map.get(order_size, 'custom')

        clear_terminal()
        print("You must pick three toppings.\n")
        print("Available Toppings:\n")
        print("  [1] Chicken - £0.35")
        print("  [2] Sweetcorn - £0.65")
        print("  [3] Pepperoni - £0.39")
        print("  [4] Pineapple - £0.23")
        print("  [5] Mushroom - £0.68")
        print("\nChoose your toppings by number:\n")

        toppings = []
        for i in range(3):
            topping_number = input(f"Select topping {i + 1} (1-5): ")
            topping_map = {
                '1': 'Chicken',
                '2': 'Sweetcorn',
                '3': 'Pepperoni',
                '4': 'Pineapple',
                '5': 'Mushroom'
            }
            topping = topping_map.get(topping_number)

            if topping is None:
                print("Invalid topping number. Please select again.")
                i -= 1 
            else:
                toppings.append(topping)

    else:
        selected_pizza, toppings = pizza_info
        order_size = 'custom'

    clear_terminal()
    total = calculate_total(order_size, toppings)

    print(f"Your total is £{total:.2f}!\n")

    if money < total:
        print(f"Insufficient funds! You still owe £{total - money:.2f}.")
        return
    elif money > total:
        change = money - total
        print(f"Change: £{change:.2f}")

    loading_animation()

    print_receipt([selected_pizza if pizza_info else order_size] + toppings, total, change)

while True:
    order_pizza()
    cont = input("\nWould you like to order another pizza? (yes/no): ").lower()
    if cont != 'yes':
        print("\nThank you for visiting MA's Pizza Place! See you next time!")
        break

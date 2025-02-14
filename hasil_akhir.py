import tkinter as tk
from tkinter import messagebox


def get_coin_combinations(amount, coins):
    if amount == 0:
        return [[]]
    if amount < 0:
        return []
    combinations = []
    for i, coin in enumerate(coins):
        remaining_coins = coins[i:]
        sub_combinations = get_coin_combinations(amount - coin, remaining_coins)
        for combination in sub_combinations:
            combination.append(coin)
            combinations.append(combination)
    return combinations


def greedy_algorithm(amount):
    coin_values = [1000, 500, 200, 100]
    coin_counts = [0, 0, 0, 0]
    for i, coin in enumerate(coin_values):
        while amount >= coin:
            amount -= coin
            coin_counts[i] += 1
    return coin_counts


def calculate():
    amount = int(entry_amount.get())
    if var.get() == 1:
        combinations = get_coin_combinations(amount, [100, 200, 500, 1000])
        if combinations:
            combinations = [
                " ".join(str(coin) for coin in combo) for combo in combinations
            ]
            combinations_str = "\n".join(combinations)
            messagebox.showinfo(
                "Coin Combinations", f"Minimum coin combinations:\n{combinations_str}"
            )
        else:
            messagebox.showinfo("Coin Combinations", "No possible combinations")
    else:
        coin_counts = greedy_algorithm(amount)
        coin_values = [1000, 500, 200, 100]
        result_str = "\n".join(
            f"{coin_values[i]} Rupiah: {coin_counts[i]}"
            for i in range(len(coin_values))
        )
        messagebox.showinfo("Coin Combinations", f"Minimum coin counts:\n{result_str}")


root = tk.Tk()
root.title("Coin Exchange Program")
root.geometry("400x250")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

label_amount = tk.Label(frame, text="Enter Rupiah amount:")
label_amount.pack()

entry_amount = tk.Entry(frame)
entry_amount.pack()

label_method = tk.Label(frame, text="Choose exchange method:")
label_method.pack()

var = tk.IntVar()
radio_brute = tk.Radiobutton(frame, text="Brute Force Method", variable=var, value=1)
radio_brute.pack()

radio_greedy = tk.Radiobutton(frame, text="Greedy Algorithm", variable=var, value=2)
radio_greedy.pack()

button_calculate = tk.Button(
    frame, text="Calculate", command=calculate, bg="blue", fg="white"
)
button_calculate.pack()

root.mainloop()

prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330}

portfolio = {}
print("Available stocks:", ", ".join(prices))

while True:
    name = input("Stock name (or 'done'): ").upper()
    if name == "DONE":
        break
    if name not in prices:
        print("Stock not available.")
        continue
    try:
        qty = int(input("Quantity: "))
    except ValueError:
        print("Enter a valid number.")
        continue
    portfolio[name] = portfolio.get(name, 0) + qty

total = 0
lines = []
for stock, qty in portfolio.items():
    value = prices[stock] * qty
    total += value
    lines.append(f"{stock}: {qty} x ${prices[stock]} = ${value}")

lines.append(f"Total Investment: ${total}")
print("\n".join(lines))

with open("portfolio.txt", "w") as f:
    f.write("\n".join(lines))
print("Saved to portfolio.txt")
products = (
    ("P101", "Notebook", 50, 12),
    ("P102", "Pen", 10, 3),
    ("P103", "Bag", 600, 2),
    ("P104", "Pencil", 5, 20)
)

total = 0

for product in products:
    product_id, name, price, stock = product

    value = price * stock
    total += value

    print("Product ID:", product_id)
    print("Product Name:", name)
    print("Price:", price)
    print("Stock:", stock)
    print("Inventory Value:", value)

    if stock < 5:
        print("Replenishment Required")

    print("------------------")

print("Total Inventory Value:", total)
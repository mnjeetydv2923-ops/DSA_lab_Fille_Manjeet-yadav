# Experiment 07: Inventory Stock Management System

inventory = []

def insert_product():
    sku = input("Enter SKU: ")
    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    inventory.append({"sku": sku, "name": name, "quantity": qty})
    print("Product Added!")

def search():
    key = input("Enter SKU or Name to Search: ")
    for item in inventory:
        if item["sku"] == key or item["name"] == key:
            print(item)
            return
    print("Not Found")

def delete():
    key = input("Enter SKU or Name to Delete: ")
    for item in inventory:
        if item["sku"] == key or item["name"] == key:
            inventory.remove(item)
            print("Deleted")
            return
    print("Not Found")

def sell():
    sku = input("Enter SKU: ")
    qty = int(input("Enter quantity to sell: "))
    for p in inventory:
        if p["sku"] == sku:
            if p["quantity"] == 0:
                print("Out of stock!")
            elif p["quantity"] < qty:
                print("Insufficient stock!")
            else:
                p["quantity"] -= qty
                print("Sale completed!")
            return
    print("SKU not found!")

def zero_stock():
    print("Zero Stock Items:")
    for p in inventory:
        if p["quantity"] == 0:
            print(p)

def max_stock():
    if not inventory:
        print("Empty Inventory")
        return
    m = max(p["quantity"] for p in inventory)
    print("Max Stock Items:")
    for p in inventory:
        if p["quantity"] == m:
            print(p)

def show():
    for p in inventory:
        print(p)

# menu()  # Uncomment to run

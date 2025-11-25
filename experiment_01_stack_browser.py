# Experiment 01: Browser History Navigation System using Stack

history = []
forward_history = []
total_history = []

def visit_page(page):
    history.append(page)
    forward_history.clear()
    total_history.append(page)
    print(f"Visited: {page}")

def go_back():
    if not history:
        print("No back history available.")
        return
    page = history.pop()
    forward_history.append(page)
    if history:
        total_history.append(history[-1])
        print(f"Moved back to: {history[-1]}")
    else:
        print("No more pages in history.")

def go_forward():
    if not forward_history:
        print("No forward history available.")
        return
    page = forward_history.pop()
    history.append(page)
    total_history.append(page)
    print(f"Moved forward to: {page}")

def view_history():
    print("Back History:", history)

def view_total_history():
    print("Total History:", total_history)

def visit_stats():
    print("Total Visits:", len(total_history))
    freq = {}
    for p in total_history:
        freq[p] = freq.get(p, 0) + 1
    print("Visit Frequency:", freq)

def menu():
    while True:
        print("\n--- Browser Menu ---")
        print("1. Visit Page\n2. Back\n3. Forward\n4. View History\n5. View Total History\n6. Stats\n7. Exit")
        ch = int(input("Enter choice: "))
        
        if ch == 1:
            page = input("Enter page URL: ")
            visit_page(page)
        elif ch == 2:
            go_back()
        elif ch == 3:
            go_forward()
        elif ch == 4:
            view_history()
        elif ch == 5:
            view_total_history()
        elif ch == 6:
            visit_stats()
        elif ch == 7:
            break
        else:
            print("Invalid choice!")

# menu()

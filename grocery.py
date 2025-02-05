def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().lower()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:  # Handle Ctrl+D to terminate input
            break
        except KeyboardInterrupt:
            break

    # Sort the grocery list alphabetically and print the items
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()

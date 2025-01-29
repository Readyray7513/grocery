# # Grocery List Program

## Overview
The Grocery List program allows users to input grocery items continuously, with each item being counted as it is entered. The program tracks how many times each item is input and displays the list in alphabetical order after the user finishes entering the items (via `Ctrl-D` or `Ctrl-C`).

## Features
- Continuously prompts the user to input grocery items.
- Automatically counts occurrences of each item, even if they are entered multiple times.
- Once input is terminated, the program displays the grocery list sorted alphabetically, showing the count for each item.

## Example Usage
```
$ python grocery_list.py
apple
banana
apple
orange
banana
grape
# Press Ctrl-D to finish input

1 APPLE
2 BANANA
1 GRAPE
1 ORANGE
```

## How to Run
1. Run the program by executing:
   ```
   python grocery_list.py
   ```
2. Input grocery items one by one. Each item should be entered on a new line.
3. To end input, press `Ctrl-D` (or `Ctrl-Z` on Windows) to finish and see the sorted list of items with counts.

## Notes
- The program treats items case-insensitively (e.g., "apple" and "Apple" will be considered the same item).
- After the input ends, the list of items will be displayed in alphabetical order, with the count next to each item name in uppercase letters.

<h1 align = "center"><b>First Class Functions Part I</b></h1>
This session was all about docstrings, annotations, lambda Expression, Functional Introspection, Callables, Map, filter and zip

## **Assignment**
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

suits = ['spades', 'clubs', 'hearts', 'diamonds']
![poker](https://i.pinimg.com/474x/6b/1f/f7/6b1ff73716c14139c951241f3c1d7c46.jpg)

1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck 
2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck 
3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker (Links to an external site.)

## **Functions**

### **1. create_deck_cards_single_expression** 
    This function creates all 52 cards from vals and suits using lambda and map function in a single line

```python
def create_deck_cards_single_expression():
    cards = []
    list(map(lambda x: list(map(lambda y: cards.append((x,y)), suits)),vals))
    return cards
```

### **2. create_deck_cards_normal_function**
This function creates all 52 cards from vals and suits without using lambda and map function
```python

def create_deck_cards_normal_function():
    cards = []

    for val in vals:
        for suit in suits:
            cards.append((val, suit))
    return cards
```
### **3. ____**



## **Tests**

1. test_readme_exists : Checks whether readme exists or not.
2. test_readme_contents : Checks if ther are more contents in readme or not
3. test_readme_proper_description :  test for appropriate documentation of readme
4. test_readme_file_for_formatting : checks for proper formating
5. test_indentations : check for source file indentation
6. test_function_name_had_cap_letter :  checks if function has cap letters or not
7. test_all_functions_implemented : checks if all given function included or not
8. test_create_deck_cards_single_expression_docstring : check for docstring exists or not
9. test_create_deck_cards_single_expression_docstring_content : check for  docstring length
10. test_create_deck_cards_single_expression_total_cards :  check for total no of cards
11. test_create_deck_cards_single_expression_compare_cards : compare the result with card combination
12. test_create_deck_cards_single_expression_invalid_input : checks for invalid input
13. test_create_deck_cards_normal_function_docstring : check for docstring exists or not
14. test_create_deck_cards_normal_function_docstring_content : check for  docstring length
15. test_create_deck_cards_normal_function_total_cards : check for total no of cards
16. test_create_deck_cards_normal_function_compare_cards : compare the result with card combination
17. test_create_deck_cards_normal_function_invalid_input :checks for invalid input
18.
19.
20.


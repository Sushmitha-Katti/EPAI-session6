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
### **3. play_poker_game**
This function evaluates which player has won poker game.

### **Rules**

   1. Royal Flush :

A, K, Q, J, 10, all the same suit for 5 cards. A, K, Q, J, all the same suit for 4 cards. A, K, Q, all the same suit for 3 cards.

   2. Straight flush :

Cards in a sequence, all in the same suit.

   3. Four Of A Kind:

Four cards of the same rank. This is not applicable to set of 3 cards.

   4. Full house :

Three of a kind with a pair. This is not applicable to set of 3 or 4 cards.

   5. Flush :

Any cards of the same suit, but not in a sequence.

   6. Straight :

Cards in a sequence, but not of the same suit.

   7. Three Of A Kind :

Three cards of the same rank.

   8. Two Pair :

Two different pairs. This is not applicable to set of 3 cards.

   9. One Pair :

Two cards of the same rank.

   10. High Card :

When you haven’t made any of the hands above, the highest card from both set is compared.

   11. deck_cards_using_single_expression :

function creates 52 cards in a deck with the help of lambda, zip and map functions

   12. deck_cards_using_normal_function :

function creates 52 cards in a deck with the normal function without using lambda, zip and map functions

   13. play_poker_game :

function evaluates which player has won poker game

   14. setValues :

stores number rank for each value of a card

   15. isRoyalFlush() :

checks if it a royal flush

   16. isStraightFlush() :

checks if it is a striaght flush

   17. isFourOfAKind():

checks if it is has four of a kind

   18. isFullHouse():

checks if it is a full house

   19. isFlush():

checks if it is a flush

   20. isStraight():

checks if it is a straight

   21. isThreeOfAKind():

checks if it has three of a kind

   22. isTwoPair():

checks if it has two pairs

   23. isOnePair():

checks if it has one pair

   24. check_hand_score():

checks which hand is applicable and returns score for that hand
    



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
18. test_map_used / test_lambda_used / test_zip_used : tests if map, lambda and zip have been used or not
19. test_play_poker_game_invalid_length_input : 
checks if invalid set of cards other than 3, 4 or 5 have been given as input
20. test_play_poker_game_length_mismatch : both set of cards given as input doesnt match length
21. test_play_poker_game_Royal_Flush / test_play_poker_game_Royal_Flush_4cards / test_play_poker_game_Royal_Flush_3cards : 
Checks if Royal Flush is identified by game for set of 5, 4, 3 cards
22. test_play_poker_game_Straight_Flush / test_play_poker_game_Straight_Flush_4cards / test_play_poker_game_Straight_Flush_3cards : 
Checks if Straight Flush is identified by game for set of 5, 4, 3 cards
23. test_play_poker_game_Four_Of_A_Kind / test_play_poker_game_Four_Of_A_Kind_4cards : 
Checks if Four of a Kind is indentified by game for set of 5, 4 cards
24. test_play_poker_game_Full_House : 
Checks if Full House is identified by game for set of 5 cards
25. test_play_poker_game_Flush / test_play_poker_game_Flush_4cards / test_play_poker_game_Flush_3cards : 
Checks if Flush is identified by game for a set of 5, 4, 3 cards
26. test_play_poker_game_Straight / test_play_poker_game_Straight_4cards / test_play_poker_game_Straight_3cards :
Checks if Straight is identified by game for a set of 5, 4, 3 cards
27. test_play_poker_game_Three_Of_A_Kind / test_play_poker_game_Three_Of_A_Kind_4cards / test_play_poker_game_Three_Of_A_Kind_3cards :
Checks if Three of a kind is identified by game for a set of 5, 4, 3 cards
28. test_play_poker_game_Two_Pair / test_play_poker_game_Two_Pair_4cards :
Checks if two pairs is identified by game for a set of 5, 4 cards
29. test_play_poker_game_One_Pair / test_play_poker_game_One_Pair_4cards / test_play_poker_game_One_Pair_3cards :
Checks if One pair is identified by game for a set of 5, 4, 3 cards
30. test_play_poker_game_High_Card / test_play_poker_game_High_Card_4cards / test_play_poker_game_High_Card_3cards : 
Checks if High Card is identified by game for a set of 5, 4, 3 cards
31. test_play_poker_game_Draw : 
Checks if both players have a draw in case both have same high card and no hand


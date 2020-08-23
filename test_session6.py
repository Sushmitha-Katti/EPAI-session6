import pytest
import random
import string
import session6
import os
import inspect
import re


CHECK_FOR_FUNCT_IMPL = [
    'vals',
    'create_deck_cards_normal_function',
    'create_deck_cards_single_expression',
    'vals',
    'suits',
    # '__eq__',
    # '__float__',
    # '__ge__',
    # '__gt__',
    # '__invertsign__',
    # '__le__',
    # '__lt__',
    # '__mul__',
    # '__sqrt__',
    # '__bool__', 
    ]

Cards_Combination = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'), ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'), ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]


README_CONTENT_CHECK_FOR = [
    'vals',
    'create_deck_cards_normal_function',
    'create_deck_cards_single_expression',
    'vals',
    'suits',
]

# Tests related to readme
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "Readme is not formatted properly"

# --------------------------------------------------------------------------------------
# Tests related Contents in session 4 file

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_implemented():
    code_lines = inspect.getsource(session6)
    FUNCS_IMPL = True
    for c in CHECK_FOR_FUNCT_IMPL:
        if c not in code_lines:
            print(c)
            FUNCS_IMPL = False
            pass
    assert FUNCS_IMPL == True, 'You forgot to implement all functions! Try again!'

# --------------------------------------------------------------------------------------
# test case for functions

def test_create_deck_cards_single_expression_docstring():
    docstring = session6.create_deck_cards_single_expression.__doc__
    assert docstring , "Beware, You have not written docstring for a function!"

def test_create_deck_cards_single_expression_docstring_content():
    docstring = session6.create_deck_cards_single_expression.__doc__
    assert len(docstring)>50 , "Beware, You have not written proper docstring for a function!"

def test_create_deck_cards_single_expression_total_cards():
    result = session6.create_deck_cards_single_expression()
    assert len(result) == 52, "There should be total of 52 cards"

def test_create_deck_cards_single_expression_compare_cards():
    result = session6.create_deck_cards_single_expression()
    for card in Cards_Combination:
        if card not in result:
            assert False, "Not all the combinations of cards present"

def test_create_deck_cards_single_expression_invalid_input():
    with pytest.raises(TypeError):
        session6.create_deck_cards_single_expression(2,3,5)



def test_create_deck_cards_normal_function_docstring():
    docstring = session6.create_deck_cards_normal_function.__doc__
    assert docstring , "Beware, You have not written docstring for a function!"

def test_create_deck_cards_normal_function_docstring_content():
    docstring = session6.create_deck_cards_normal_function.__doc__
    assert len(docstring)>50 , "Beware, You have not written proper docstring for a function!"

def test_create_deck_cards_normal_function_total_cards():
    result = session6.create_deck_cards_normal_function()
    assert len(result) == 52, "There should be total of 52 cards"

def test_create_deck_cards_normal_function_compare_cards():
    result = session6.create_deck_cards_normal_function()
    for card in Cards_Combination:
        if card not in result:
            assert False, "Not all the combinations of cards present"

def test_create_deck_cards_normal_function_invalid_input():
    with pytest.raises(TypeError):
        session6.create_deck_cards_normal_function(2,3,5)









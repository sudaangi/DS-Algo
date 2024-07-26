# Problem Statement:
# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.
import math

#Linear search function
def locate_card_linear_search(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

#Binary search function

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid_number >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card_binary_search(cards, query):
    lo, hi = 0, len(cards) - 1
    sorted_cards = sorted(cards, reverse=True)
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(sorted_cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# Test cases
tests = []
test = {
    'input': {
        'cards': [1, 0, 6, 2, 3, -9],
        'query': -9
    },
    'output': 5
}
tests.append(test)
tests.append({
    'input': {
        'cards': [2, 8, 12, 16, 1, 19, 13, 21],
        'query': 16
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [4],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 6
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [4, 2, 1, 1],
        'query': 2
    },
    'output': 1
})

tests.append({
    'input': {
        'cards': [9, 6, 4, 3, 3, 2, 1, -9],
        'query': 1
    },
    'output': 6
})

test_position = 0
while test_position < len(tests):
    result = locate_card_binary_search(**tests[test_position]['input']) == tests[test_position]['output']
    print(result)
    test_position += 1





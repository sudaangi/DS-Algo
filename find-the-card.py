def locate_card_linear_search(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

def locate_card_binary_search(cards, query):
    pass

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
        'cards': [4, 2, 1, 1, 3, 6, 9, 1, 0],
        'query': 1
    },
    'output': 2
})

test_position = 0
while test_position < len(tests):
    result = locate_card_linear_search(**tests[test_position]['input']) == tests[test_position]['output']
    print(result)
    test_position += 1
print(test_position)





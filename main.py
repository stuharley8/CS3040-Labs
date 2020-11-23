# Stuart Harley
# Assignment 4: Recursive Descent Parser

import re


def next_token(tokens) -> str:
    if len(tokens) > 0:
        return tokens[0]
    else:
        return ''


def advance(tokens) -> None:
    del tokens[0]


def consume_next_token(token, tokens) -> None:
    if next_token(tokens) != token:
        fail(token, next_token(tokens))
    else:
        advance(tokens)


def consume_next_token_plural(token1, token2, tokens) -> None:
    if next_token(tokens) != token1 and next_token(tokens) != token2:
        fail(token1 + ' or ' + token2, next_token(tokens))
    else:
        advance(tokens)


def fail(expected, given):
    raise ValueError('Expected: ' + expected + ' Given: ' + given)


def parse_plans(tokens) -> int:
    floors = {}
    parse_floor(tokens, floors)
    while next_token(tokens) == 'floor':
        parse_floor(tokens, floors)
    return parse_complex(tokens, floors)


def parse_complex(tokens, floors) -> int:
    consume_next_token('complex', tokens)
    sqft = parse_building(tokens, floors)
    while next_token(tokens) == 'building':
        sqft = sqft + parse_building(tokens, floors)
    return sqft


def parse_building(tokens, floors) -> int:
    consume_next_token('building', tokens)
    parse_name(tokens)
    consume_next_token('with', tokens)
    consume_next_token_plural('floor', 'floors', tokens)
    return parse_floor_list(tokens, floors)


def parse_floor_list(tokens, floors) -> int:
    consume_next_token('{', tokens)
    name = parse_floor_reference(tokens)
    sqft = floors[name]
    while next_token(tokens) == ',':
        consume_next_token(',', tokens)
        name = parse_floor_reference(tokens)
        sqft = sqft + floors[name]
    consume_next_token('}', tokens)
    return sqft


def parse_floor_reference(tokens) -> str:
    return parse_name(tokens)


def parse_floor(tokens, floors) -> None:
    consume_next_token('floor', tokens)
    name = parse_name(tokens)
    floors[name] = 0
    consume_next_token('has', tokens)
    consume_next_token_plural('room', 'rooms', tokens)
    parse_room_list(tokens, floors, name)


def parse_room_list(tokens, floors, name) -> None:
    consume_next_token('[', tokens)
    parse_room(tokens, floors, name)
    while next_token(tokens) == ',':
        consume_next_token(',', tokens)
        parse_room(tokens, floors, name)
    consume_next_token(']', tokens)


def parse_room(tokens, floors, name) -> None:
    length = parse_number(tokens)
    consume_next_token('by', tokens)
    width = parse_number(tokens)
    floors[name] = floors[name] + (length * width)


def parse_name(tokens) -> str:
    if re.match("^[A-Z_]*$", next_token(tokens)):
        name = next_token(tokens)
        advance(tokens)
        return name
    else:
        fail('[A-Z_]+', next_token(tokens))


def parse_number(tokens) -> int:
    if re.match("^[0-9]*$", next_token(tokens)):
        num = next_token(tokens)
        advance(tokens)
        return int(num)
    else:
        fail('[0-9]+', next_token(tokens))


def main():
    filename = input('Enter a text file: ')
    file = open(filename, "r")
    text = file.read()
    text = text.replace(',', ' ,')
    tokens = text.split()
    print('The total usable area is ' + str(parse_plans(tokens)) + ' square feet.')


main()

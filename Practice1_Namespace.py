calls = 0


def count_calls():
    """Counting calls of other functions"""
    global calls
    calls+=1


def string_info(string: str):
    """Takes an argument of str type
        Returns cortege of string_length string.upper string.lower"""
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list: list):
    """receives string and list arguments
        returns True if list contains such string
        Returns False, when is not
        register of string doesn't matter"""
    count_calls()
    flag = False
    for i in list:
        if i.casefold() == string.casefold():
            flag = True
    return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
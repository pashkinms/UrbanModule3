

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    """

    """
    result = 0

    for element in data:
        if isinstance(element, int):
            result += element
        elif isinstance(element, str):
            result += len(element)
        elif isinstance(element, tuple) or isinstance(element, list) or isinstance(element, set):
            result += calculate_structure_sum(element)
        elif isinstance(element, dict):
            key_list = list(element)
            for key in key_list:
                result += len(key)
                result += element.get(key)

    return result


result = calculate_structure_sum(data_structure)
print(result)
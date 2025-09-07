def word_count(string: str) -> int:
    num_of_words = len(string.split())
    return num_of_words


def char_count(text: str) -> dict[str, int]:
    results_dict = {}
    for char in text:
        char = char.lower()
        if char not in results_dict:
            results_dict[char] = 1
        else:
            results_dict[char] += 1 

    return results_dict


def char_dict_sorted(dict_to_sort: dict[str, int]) -> list[dict]:
    list_of_dicts = []

    for key in dict_to_sort:
        list_of_dicts.append({"char": key, "num":dict_to_sort[key]})

    list_of_dicts.sort(reverse=True, key=__sort_key)

    return list_of_dicts


def __sort_key(dictionary: dict) -> int:
    return dictionary["num"]

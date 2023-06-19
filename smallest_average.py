def get_av(person: dict) -> float:
    return (person["result1"] + person["result2"] + person["result2"]) / 3


def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    person_with_smallest_av = person1
    smallest_av = get_av(person1)
    if get_av(person2) < smallest_av:
        person_with_smallest_av = person2
        smallest_av = get_av(person2)
    if get_av(person3) < smallest_av:
        person_with_smallest_av = person3
    return person_with_smallest_av


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))

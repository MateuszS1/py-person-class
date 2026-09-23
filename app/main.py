class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]

    all_people = Person.people
    for person in people:
        if person.get("wife") is not None:
            all_people[person["name"]].wife = all_people[person["wife"]]

        if person.get("husband") is not None:
            all_people[person["name"]].husband = all_people[person["husband"]]

    return list(Person.people.values())

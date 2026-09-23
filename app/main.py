class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person.get("name"), person.get("age")) for person in people]

    all_people = Person.people
    for person in people:
        if person.get("wife") is not None:
            all_people[person.get("name")].wife = all_people[person.get("wife")]

        if person.get("husband") is not None:
            all_people[person.get("name")].husband = all_people[person.get("husband")]

    return list(Person.people.values())

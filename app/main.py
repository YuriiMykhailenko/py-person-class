class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    instances = [Person(p["name"], p["age"]) for p in people]
    for data, inst in zip(people, instances):
        spouse_name = data.get("wife")
        if spouse_name is not None:
            spouse = Person.people.get(spouse_name)
            if spouse is not None:
                inst.wife = spouse
        spouse_name = data.get("husband")
        if spouse_name is not None:
            spouse = Person.people.get(spouse_name)
            if spouse is not None:
                inst.husband = spouse
    return instances

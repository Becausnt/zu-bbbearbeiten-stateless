from dataclasses import dataclass

items = []


@dataclass
class Todo:
    title: str
    isCompleted: bool = False


def add(title):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Todo(title))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted

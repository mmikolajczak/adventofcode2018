INPUT_PATH = 'input.txt'


class Node:

    def __init__(self, children, entries):
        # Note: "private", Nodes should be created using construct classmethod
        self.children = children
        self.entries = entries

    @staticmethod
    def construct(numbers):
        nb_children, nb_entries = numbers[:2]
        numbers = numbers[2:]
        children = []
        for _ in range(nb_children):
            child, numbers = Node.construct(numbers)
            children.append(child)
        entries = numbers[:nb_entries]
        numbers = numbers[nb_entries:]
        return Node(children, entries), numbers

    def walk(self):
        yield self.entries
        for ch in self.children:
            for el in ch.walk():
                yield el

    @property
    def value(self):
        if self.children:
            val = 0
            for entry in self.entries:
                if entry - 1 < len(self.children):
                    val += self.children[entry - 1].value
            return val
        else:
            return sum(self.entries)


class Tree:

    def __init__(self, f_content):
        numbers = [int(nb) for nb in f_content.split(' ')]
        self.root = Node.construct(numbers)[0]

    def walk(self):
        # traverse through tree values, in parent first, children from left to right later manner. return generator
        return self.root.walk()


def is_iterable(arg):
    try:
        iter(arg)
        return True
    except TypeError:
        return False


def flatten(nested):
    res = []
    for el in nested:
        if is_iterable(el):
            res.extend(flatten(el))
        else:
            res.append(el)
    return res


def solution_8_2(input_path):
    with open(input_path) as f:
        content = f.read()
    tree = Tree(content)
    return tree.root.value


if __name__ == '__main__':
    res = solution_8_2(INPUT_PATH)
    print(res)

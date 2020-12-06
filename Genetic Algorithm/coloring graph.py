import csv
import genetic
import unittest
from datetime import datetime

def display(candidate, startTime):
    timeDiff = datetime.now() - startTime
    print("{}\t{}\t{}".format(
        ''.join(map(str, candidate.Genes)),
        candidate.Fitness,
        timeDiff))

def get_fitness(genes, rules, state_index_lookup):
    rules_that_pass = sum(1 for rule in rules
            if rule.is_valid(genes, state_index_lookup))
    return rules_that_pass

def load_data(data_file):
    """
        expects: A,B;C, where A - key city; B and C - its neighbours
    """
    with open(data_file, mode='r') as df:
        reader = csv.reader(df)
        lookup = {row[0]: row[1].split(';') for row in reader if row}
    return lookup

def build_rules(items):
    rules_added = {}

    for state, adjacent in items.items():
        for adjacent_state in adjacent:
            if adjacent_state == '':
                continue
            rule = Rule(state, adjacent_state)
            if rule in rules_added:
                rules_added[rule] += 1
            else:
                rules_added[rule] = 1

    for key, value in rules_added.items():
        if value != 2:
            print("rule {0} is not bidirectional".format(key))

    return rules_added.keys()

class Rule:
    def __init__(self, node, adjacent):
        if node < adjacent:
            node, adjacent = adjacent, node
        self.Node = node
        self.Adjacent = adjacent

    def __eq__(self, other):
        return self.Node == other.Node and \
               self.Adjacent == other.Adjacent

    def __hash__(self):
        """
            unique value, cause using prime number
        """
        return hash(self.Node) * 397 ^ hash(self.Adjacent)

    def __str__(self):
        return self.Node + '->' + self.Adjacent

    def is_valid(self, genes, node_index_lookup):
        index = node_index_lookup[self.Node]
        adjacent_state_index = node_index_lookup[self.Adjacent]
        return genes[index] != genes[adjacent_state_index]


class GraphColoringTest(unittest.TestCase):

    def invoke(self, colors_cnt, input_file):
        states = load_data(input_file)
        rules = build_rules(states)
        optimal_value = len(rules)
        state_index_lookup = {key: index
                              for index, key in enumerate(sorted(states))}

        default_colors = ['Orange', 'Green', 'Yellow', 'Blue', 'Red', 'White', 'Black', 'Grey']
        colors = default_colors[:colors_cnt]
        color_lookup = {color[0]: color for color in colors}
        geneset = list(color_lookup.keys())

        start_time = datetime.now()

        def fn_display(candidate):
            display(candidate, start_time)

        def fn_get_fitness(genes):
            return get_fitness(genes, rules, state_index_lookup)

        best = genetic.get_best(fn_get_fitness, len(states),
                                optimal_value, geneset, fn_display)
        self.assertTrue(not optimal_value > best.Fitness)

        keys = sorted(states.keys())

        for i in range(len(states)):
            print('{0} is {1}'.format(keys[i], color_lookup[best.Genes[i]]))


if __name__ == '__main__':
    test = GraphColoringTest()
    test.invoke(4, 'USA states.txt')
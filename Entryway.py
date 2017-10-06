import numpy as np


class Option:

    def __init__(self, name, prob, line):
        if not 0 < prob < 1:
            print('{} is not in range (0, 1). Fix yourself!'.format(prob))
            return
        self.name = name
        self.p = prob
        self.line = line

    def __str__(self):
        return '[OPTION OBJ:[ name: {name}, p: {p}, line: {line} ]]'.format(name=self.name, p=self.p, line=self.line)


class Entryway:

    def __init__(self, options):
        """
        :param options: [Option] -- a list of Option instances
        """
        if round(sum([o.p for o in options]) != 1):
            print('probabilities {} do not sum to 1. Fix yourself!'.format(str(options)))
            return

        self.options = options

    def choose(self, person):
        """
        :param person: Person object 
        """
        opt_indices = list(range(len(self.options)))
        dest = self.options[np.random.choice(opt_indices, p=[opt.p for opt in self.options])]
        dest.push(person)





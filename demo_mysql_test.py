class CodeCouple(object):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == 'Agnieszka':
            self.__name = 'beautiful'
        elif name == 'Krzysztof':
            self.__name = 'ugly'
        else:
            self.__name = 'CodeCouple'


agnieszka = CodeCouple('Agnieszka')
print(agnieszka.name)

krzysztof = CodeCouple('Krzysztof')
print(krzysztof.name)

code_couple = CodeCouple('UglyKrzysztof')
print(code_couple.name)

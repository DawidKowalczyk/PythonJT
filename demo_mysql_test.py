# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="dkw",
#     passwd="dkwd",
#     database="mydatabase"
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")
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

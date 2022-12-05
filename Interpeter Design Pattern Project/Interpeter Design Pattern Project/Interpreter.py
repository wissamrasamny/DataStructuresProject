class Expression:
    def interpreter(self, name):
        pass


class TerminalExpression(Expression):
    tutors = []
    ids = []

    def _init_(self, tutors):
        self.tutors = tutors

    def interpreter(self, name):
        id = ""
        count = 1
        arr = name.split(" ")
        for names in arr:
            id += names[0:1].upper()
        id += "01"
        if id in self.ids:
            if len(id) == 4:
                id = id[0:2] + "02"
            else:
                id = id[0:3] + "02"
        self.ids.append(id)
        print(id)
        return id


class check_name(Expression):
    expr1 = None

    def _init_(self, expr1):
        self.expr1 = expr1

    def interpreter(self, con):
        return self.expr1.interpreter(con)


class new_version:
    @staticmethod
    def main(args):
        tutors = ["Dani Chaddad", "Wajih Tayyar", "Makram Fares", "Chadi Chamoun", "Joanne Rizkallah",
                  "Mohammad Al Kammoun", "Charbel Khoury", "Christina Saliba", "Josee Rizkallah", "Christy Skaff",
                  "Georges Saab", "Charbel Hanna", "Cyril El Mendek"]
        ter = TerminalExpression(tutors)
        cn = check_name(ter)
        cn.interpreter(tutors[0])


if __name__ == "_main_":
    new_version.main([])
class Equation:


    def __init__(self, weight, power):
        self.weight = int(weight)
        self.power = int(power)
        self.dic = dict()
        self.tab = []


    def getWeight(self):
        return self.weight


    def setWeight(self, weight):
        self.weight = weight


    def getPower(self):
        return self.power


    def setPower(self, power):
        self.power = power


    def tostring(self):
        return(f"weight {self.weight} power {self.power}")


    def prepare_expression(self, str_val):
        """
        take the string expression
        return a well formatted 2 dimensional tab
        format expression [+|-|""][0-9*][*X[^[0-9*]]]
        """
        str_val = str_val.replace(" ", "").replace("\t", "").replace("\n", "").replace("+", " +").replace("-",
                " -").replace(
            "=", " = ")
        expres = str_val.split("=")
        index = 0
        while index < len(expres):
            expres[index] = expres[index].strip()
            index += 1
        return expres

    def get_elemt_expression(self, e):
        index = 0
        len_elem = len(e)
        if e[0] == "-":
            index = 1
        if e[0] == "+":
            index = 1
        while index < len_elem and ((e[index] == ".") or (e[index].isdigit())):
            index += 1
        if index == len_elem - 1 and e[index] == "X":
            q = e.replace("+", "").replace("-", "")
            if len(q) == 1 and q == "X":
                if e[0] == "-":
                    poid_x = -1
                else:
                    poid_x = 1
                power = 1
                elem = Equation(int(poid_x), int(power))
                return elem
        if index == len_elem and e[index - 1] == ".":
            print(f"Error format [{e}]")
            return None
        try:
            if (len(e) == 1):
                poid_x = float(e[:index])
            else:
                if (index == len(e)):
                    poid_x = float(e[:index])
                elif e[index] == "X":
                    if (e[0] == '+' or e[0] == '-') and e[1] == 'X':
                        poid_x = 1
                    elif e[0] == 'X':
                        poid_x = 1
                    else:
                        poid_x = float(e[:index])
                else:
                    poid_x = float(e[:index])
        except ValueError:
            print(f"Error format : [{e}]")
            return None
        power = 0
        if index < len_elem:
            if e[index] == "*" or e[index] == "X":
                if e[index] == "*":
                    index += 1
                if index < len_elem and e[index] == "X":
                    index += 1
                    if index < len_elem and (e[index] == "^" or e[index].isdigit()):
                        if not e[index].isdigit():
                            index += 1
                        if index == len_elem:
                            print(f"Error format : the power of the unknown element is not indicated : [{e}]")
                            return None
                        else:
                            power = e[index:]
                            if not power.isdigit():
                                print(
                                    f"Error format : the power of the unknown element is not well formatted: [{e}] int expected")
                                return None
                    elif index == len_elem:
                        power = 1
                    else:
                        print(f"Error format : the element [{e}] is not well formatted")
                        return None
                else:
                    print(f"Error format: The expression is not well formatted in element [{e}]")
                    return None
            else:
                print(f"Error format: The expression is not well formatted in element [{e}]")
                return None
        elem = Equation(int(poid_x), int(power))
        return elem


    def sort_equation(self, tab):
        i = 0
        while i < len(tab) - 1:
            if int(tab[i].getPower()) > int(tab[i + 1].getPower()):
                temp = tab[i]
                tab[i] = tab[i + 1]
                tab[i + 1] = temp
                i = 0
            else:
                i += 1
        return tab


    def leftPart(self, expression, dico):
        """
            extract the elements of the left expression
        """
        elem = expression.split(" ")
        for e in elem:
            el = self.get_elemt_expression(e)
            if el is not None:
                if el.getPower() in dico.keys():
                    dico[el.getPower()] += el.getWeight()
                else:
                    dico[el.getPower()] = el.getWeight()
            else:
                exit(-1)


    def rightPart(self, expression, dico):
        """
            extract the elements of the right expression
        """
        elem = expression.split(" ")
        for e in elem:
            el = self.get_elemt_expression(e)
            if el is not None:
                if el.getPower() in dico:
                    dico[el.getPower()] -= el.getWeight()
                else:
                    dico[el.getPower()] = -el.getWeight()
            else:
                exit(-1)


    def print_min_expression(self, tab):
        ret = ""
        i = 0
        l = len(tab)
        for e in tab:
            if not( i == l or i == 0):
                if (e.getWeight() > 0) :
                    ret += f" +"
                else:
                    ret += f" "
            if e.getWeight() != 1:
                ret += f"{e.getWeight()}"
            ret += f"X^{e.getPower()}"
            i += 1
        ret += f" = 0"
        print(ret)


    def minimize_expression(self, expression):
        """
            extract information in the expression and minimize it
        """
        ## tout mettre dans un tableux puis le triee et le mettre dans dico
        self.leftPart(expression[0], self.dic)
        self.rightPart(expression[1], self.dic)
        tab = []
        for clef, val in self.dic.items():
            c = int(clef)
            v = int(val)
            if v != 0:
                tab.append(Equation(v, c))
        self.tab = self.sort_equation(tab)
        self.print_min_expression(self.tab)

from math import *

class Equation:


    def __init__(self, weight, power):
        self.weight = float(weight)
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
        return("weight {0} power {1}".format(self.weaight, self.power))


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
                elem = Equation(float(poid_x), int(power))
                return elem
        if index == len_elem and e[index - 1] == ".":
            print("Error format [{0}]".format(e))
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
            print("Error format [{0}]".format(e))
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
                            print("Error format : the power of the unknown element is not indicated : [{0}]".format(e))
                            return None
                        else:
                            power = e[index:]
                            if not power.isdigit():
                                print(
                                    "Error format : the power of the unknown element is not well formatted: [{0}] int expected".format(e))
                                return None
                    elif index == len_elem:
                        power = 1
                    else:
                        print("Error format : the element [{0}] is not well formatted".format(e))
                        return None
                else:
                    print("Error format: The expression is not well formatted in element [{0}]".format(e))
                    return None
            else:
                print("Error format: The expression is not well formatted in element [{0}]".format(e))
                return None
        elem = Equation(float(poid_x), int(power))
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


    def get_min_expression(self, tab):
        ret = ""
        i = 0
        l = len(tab)
        for e in tab:
            if not( i == l or i == 0):
                if (e.getWeight() > 0) :
                    ret += " +"
                else:
                    ret += " "
            if e.getWeight() != 1:
                ret += "{0}".format(e.getWeight())
            ret += "X^{0}".format(e.getPower())
            i += 1
        ret += " = 0"
        return ret


    def minimize_expression(self, expression):
        """
            extract information in the expression and minimize it
        """
        self.leftPart(expression[0], self.dic)
        self.rightPart(expression[1], self.dic)
        for clef, val in self.dic.items():
            c = int(clef)
            v = float(val)
            if v != 0:
                self.tab.append(Equation(v, c))
        return self.sort_equation(self.tab)

    def get_max_power_equation(self, tab):
        l = len(tab)
        if l == 0:
            return (0)
        return (tab[l - 1].getPower())

    def solve_neg_delta(self, a, b, delta):
        r = sqrt(delta)
        if (r * r) == delta :
            print("x1 = (-{0} - i * {1})/ {2}  ".format(b, r, 2 * a))
            print("x2 = (-{0} + i * {1})/ {2}  ".format(b, r, 2 * a))
        else:
            print("x1 = (-{0} - i * √ {1})/ {2}  ".format(b, delta, 2 * a))
            print("x2 = (-{0} + i * √ {1})/ {2}  ".format(b, delta, 2 * a))
       
    def solve_second(self, tab):
        """ 
            aX2 + bX + c = 0
            faire attention quand b == 0 ou/et c == 0
        """
        b = 0
        c = 0
        for e in tab:
            if (e.getPower() == 2):
                a = e.getWeight()
            elif (e.getPower() == 1):
                b = e.getWeight()
            elif (e.getPower() == 0):
                c = e.getWeight()
        delta = (b * b) - (4 * a * c)
        print("[a == {0}]  [b == {1}]  [c == {2}]  [delta == {3}]".format(a, b, c, delta))
        if (delta > 0):
            print("Discriminant is strictly positive, the two solutions are:")
            val1 = (-b - sqrt(delta)) / (2 *a)
            val2 = (-b + sqrt(delta)) / (2 *a)
            print("x1 = {0}".format(val1))
            print("x2 = {0}".format(val2))
        elif delta == 0:
            print("Discriminant is Null, the solution is:")
            val1 = (-b - sqrt(delta)) / (2 *a)
            print("x = {0}".format(val1))
        else:
            print("Ther's no solution in ℝ")
            print("Do you want to solve it ?  Y/y to continue other to stop")
            if  input().upper() == "Y":
                self.solve_neg_delta(a, b, -delta)
            else:
                print("Ciao")
                exit(0)
                                                                                            


    def solve_first(self, tab):
        """ 
            faire gaffe aX + b = 0   a ce que quand b == 0
        """
        l = len(tab)
        if (l == 1):
            print("The solution is : 0")
        else:
            b = tab[0].getWeight()
            a = tab[1].getWeight()
            print("The solution is : {0}".format(-b / a))

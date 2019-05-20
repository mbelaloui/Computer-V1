from Equation import *

"""
    reste a tester la fonction get_elemt_expression  pour tout les cas possible 
"""

if __name__ == "__main__":
    #    str_test = " -115 * X^5  + 7 -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0  "
    #    str_test = " -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2  +1 * X^0  "
    #    str_test = "8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0 + 2 "
    #str_test = "+4.4X^5 +1X^2 +1X^2 +1X^2 -X  = 0 + 5 + X^2"
    #str_test = "  X = 2*X^2"
    #str_test = "X+X -X + 4 + 4. -4.4 +4.4X -4.4* +4.4*X - 4.4X^ + 4.4X^7 -4.4X^s -*X^5 +X  + 7 -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0  "
    #str_test = " -X + X^0  + 1*X^2 +4X^4  +X^3 +  0X^9 + 5 = -2 +X +X^7 -5"
    str_test = " -X + X^0  + 1*X^2 +4X^4  +X^3 +  0X^9 + 5  -2 +X +X^7 -5"

    temp = Equation(0, 0)
    if len(str_test .split("=")) != 2:
        print("no = in the expression continue ?? Y/y to continue other to stop")
        if input() == "Y":
            str_test  += " = 0"
        else:
            exit(0)
    expression = temp.prepare_expression(str_test)
    expression_minim = temp.minimize_expression(expression)
    print("------- voir si le degre de l'eqaution < 3 si oui resoudre l'equation si non exit---------------")

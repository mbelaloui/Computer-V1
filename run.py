from Equation import *
import sys


def run(str_test):
    """"
    for bonus degree 3  
print("------- voir si le degre de l'eqaution < 3 si oui resoudre l'equation si non exit---------------")
    """
    temp = Equation(0, 0)
    expression = temp.prepare_expression(str_test)
    if (len(expression[0]) and len(expression[1])):
        expression_minim_tab = temp.minimize_expression(expression)
        min_equation = temp.get_min_expression(expression_minim_tab)
        power_max = temp.get_max_power_equation(expression_minim_tab)
        print("Reduced form : {0}".format(min_equation))
        print("Polynomial degree : {0}".format(power_max))
        if (power_max > 2):
            print("The Polynomial degree is stricly greater than 2, I can't solve")
            exit(0)
        elif power_max == 2:
            temp.solve_second(expression_minim_tab)
        elif power_max == 1:
            temp.solve_first(expression_minim_tab)
        elif power_max == 0:
            if expression_minim_tab:
                print("There's no solution !!")
            else:
                print("All the X ∈ ℝ are the sollution !!") 
    else:
        print("Wrong format: Usage Python3 '[aX2 + bX + c = 0]' / a,b,c are double ")

if __name__ == "__main__":
    if len(sys.argv) is 2 :
        str_test = sys.argv[1]
        size = len(str_test.split("="))
        if size == 2:
            run(str_test)
        elif size == 1:
            print("Warning, no '=' in the expression continue !! Y/y to continue other to stop")
            if  input().upper() == "Y":
                str_test  += " = 0"
                run(str_test)
            else:
                print("Ciao")
                exit(0)
        else:
            print("Error, multiple '=' found in the expression please check the expression and retry\nCiao")
            exit(0)
    else:
        print("Wrong format: Usage Python3 '[aX2 + bX + c = 0]' / a,b,c are double ")


#Str for test : 
#str_test = "3X2 +5X + 7 = 0"
#str_test = "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
#str_test = "5 * X^0 + 4 * X^1 - 9.3 * X^3 = 1 * X^0"
#str_test = "4X2 + 5X -2"
#str_test = "X2 + 4 + 5X "
#str_test = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
#str_test = "4X2 + 4X +1 = 0 "
#    str_test = " -115 * X^5  + 7 -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0  "
#    str_test = " -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2  +1 * X^0  "
#    str_test = "8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0 + 2 "
#str_test = "+4.4X^5 +1X^2 +1X^2 +1X^2 -X  = 0 + 5 + X^2"
#str_test = "  X = 2*X^2"
#str_test = "X+X -X + 4 + 4. -4.4 +4.4X -4.4* +4.4*X - 4.4X^ + 4.4X^7 -4.4X^s -*X^5 +X  + 7 -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0  "
#str_test = " -X + X^0  + 1*X^2 +4X^4  +X^3 +  0X^9 + 5 = -2 +X +X^7 -5"
#str_test = " -X + X^0  + 1*X^2 +4X^4  +X^3 +  0X^9 + 5  -2 +X +X^7 -5"

from Equation import *

"""
    reste a tester la fonction get_elemt_expression  pour tout les cas possible 
"""

def run(str_test):
    temp = Equation(0, 0)
    expression = temp.prepare_expression(str_test)
    expression_minim_tab = temp.minimize_expression(expression)
    min_equation = temp.get_min_expression(expression_minim_tab)
    power_max = temp.get_max_power_equation(expression_minim_tab)
    print(f"Reduced form : {min_equation}")
    print(f"Polynomial degree : {power_max}")

    print("------- voir si le degre de l'eqaution < 3 si oui resoudre l'equation si non exit---------------")

    if (power_max > 2):
        print("The Polynomial degree is stricly greater than 2, I can't solve")
        exit(0)
    elif power_max == 2:
        temp.solve_second(expression_minim_tab)
    elif power_max == 1:
        temp.solve_first(expression_minim_tab)
    elif power_max == 0:
        print("All the X ∈ ℝ are the sollution !!") 



if __name__ == "__main__":
    #str_test = "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
    #str_test = "5 * X^0 + 4 * X^1 - 9.3 * X^3 = 1 * X^0"
    str_test = "4X +  5"
    size = len(str_test .split("="))
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










#    str_test = " -115 * X^5  + 7 -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0  "
#    str_test = " -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2  +1 * X^0  "
#    str_test = "8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0 + 2 "
#str_test = "+4.4X^5 +1X^2 +1X^2 +1X^2 -X  = 0 + 5 + X^2"
#str_test = "  X = 2*X^2"
#str_test = "X+X -X + 4 + 4. -4.4 +4.4X -4.4* +4.4*X - 4.4X^ + 4.4X^7 -4.4X^s -*X^5 +X  + 7 -4 + 8*X +  5   *    X ^  0      + 4 *     X  ^1  -   \t 9.3 * X^2 = +1 * X^0  "
#str_test = " -X + X^0  + 1*X^2 +4X^4  +X^3 +  0X^9 + 5 = -2 +X +X^7 -5"
#str_test = " -X + X^0  + 1*X^2 +4X^4  +X^3 +  0X^9 + 5  -2 +X +X^7 -5"

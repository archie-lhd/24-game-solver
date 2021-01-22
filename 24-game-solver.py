from itertools import permutations
from fractions import Fraction

OPERATOR = [' + ', ' - ', ' * ', ' ÷ ']
SAMPLE_LIST = [[2,2,2,9], [2,7,8,9], [1,2,7,7], [4,4,10,10],[6,9,9,10],
               [1,5,5,5], [2,5,5,10], [1,4,5,6], [3,3,7,7], [3,3,8,8]]
                                    
def calc(L) -> list:
    algorithm_list = []
    s_list = []
    p1 = list(set(permutations(L, 2)))
    for op1 in range(4):
        for i in p1:
            lst1 = L[:]
            lst1.remove(i[0])
            lst1.remove(i[1])            
            res = method(i[0], i[1])[op1]   
            lst1.append(res) #3 in L
            p2 = list(set(permutations(lst1,2)))
                   
            for op2 in range(4):
                for j in p2:
                    lst2 = lst1[:]
                    lst2.remove(j[0])
                    lst2.remove(j[1])                   
                    res2 = method(j[0], j[1])[op2]
                    lst2.append(res2) #2 in L 
                    p3 = list(set(permutations(lst2,2)))
                    
                    for op3 in range(4):
                        for k in p3:
                            lst3 = lst2[:]
                            lst3.remove(k[0])
                            lst3.remove(k[1])     
                            res3 = method(k[0], k[1])[op3]
                            lst3.append(res3) #1 in L
                            if res3 == 24: 
                                eq1 = {i[0], op1, i[1], res}
                                eq2 = {j[0], op2, j[1], res2}
                                eq3 = {k[0], op3, k[1], res3}
                                s = {frozenset(eq1), frozenset(eq2), 
                                     frozenset(eq3)}
                                if s not in s_list and res*res2*res3 > 0:
                                    s_list.append(s)
                                    eq1 = equation(i[0], op1, i[1], res)
                                    eq2 = equation(j[0], op2, j[1], res2)
                                    eq3 = equation(k[0], op3, k[1], res3)
                                    e = str(eq1 + ' ;  ' + eq2 + ' ;  ' + 
                                            eq3)                                
                                    if e not in algorithm_list:
                                        algorithm_list.append(e)
    return algorithm_list

def method(a, b) -> tuple:
    res_plus = a + b
    res_minus = a - b
    res_multiply = a * b
    res_divide = 0
    
    if b != 0:
        res_divide = Fraction(a,b)
    
    return res_plus, res_minus, res_multiply, res_divide


def equation(a, op, b, c) -> str:
    return (str(a) + OPERATOR[op] + str(b) + ' = ' + str(c))


for sample in SAMPLE_LIST:
    print(sample)
    alg_list = calc(sample)         
    for i in alg_list:
        print(i)
    print("")
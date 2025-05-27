from z3 import *

#define the variables
x1 = Bool("x_1")
x2 = Bool ("x_2")
x3 = Bool ("x_3")
x4 = Bool ("x_4")
A = Bool("A")
var = {x1,x2,x3,x4}

print(var)

var = [Bool(f'x_{i+1}') for i in range(4)]
print(var)

#solving a formula in conjunction
solve(x1, x2, Not(x3), Not(x4))   #equivalently, x_1∧x_2∧¬x_3∧¬x_4

#Boolean formula And
print(And(x1,x2))
print(And(x1,Not(x2),Not(x3)))
print(And(var))

print()
#solving
solve(And(x1,x2))
solve(And(x1,Not(x2),Not(x3)))
solve(And(var))

#Boolean formula Or
print(Or(x1,x2))
print(Or(x1,Not(x2),Not(x3)))
print(Or(var))

print()
#solving
solve(Or(x1,x2))
solve(Or(x1,Not(x2),Not(x3)))
solve(Or(var))

#Boolean formula implication
print(Implies(x1,And(x2,Not(x3))))
print(Implies(x2,Or(And(x2,Not(x3)),And(x1,x4))))

print()
#solving
solve(Implies(x1,And(x2,Not(x3))))
solve(Implies(x2,Or(And(x2,Not(x3)),And(x1,x4))))

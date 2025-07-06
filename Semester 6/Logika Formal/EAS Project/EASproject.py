from z3 import *

max_steps = 10

X = [Int(f'x_{i}') for i in range(max_steps+1)]
Y = [Int(f'y_{i}') for i in range(max_steps+1)]

print(", ".join([f"({x}, {y})" for x, y in zip(X, Y)]))

s = Solver()

s.add(X[0] == 0, Y[0] == 0)  
s.add(X[max_steps] == 6, Y[max_steps] == 4)

s.add([X[i+1] >= 0 for i in range(max_steps)])
s.add([X[i+1] <= 6 for i in range(max_steps)])
s.add([Y[i+1] >= 0 for i in range(max_steps)])
s.add([Y[i+1] <= 4 for i in range(max_steps)])

obs = [(3, 1), (4, 1), (4, 2), (2, 2), (2, 3), (3, 3)]
s.add([Or(X[i+1] != m, Y[i+1] != n) for i in range(max_steps-1) for (m, n) in obs])

def right_step(i):
    return And(X[i+1] == X[i] + 1, Y[i+1] == Y[i])

def up_step(i):
    return And(X[i+1] == X[i], Y[i+1] == Y[i] + 1)

def module_a(solver):
    new_solver = Solver()
    new_solver.add(solver.assertions())
    for i in range(max_steps):
        new_solver.add(Or(
            right_step(i),
            up_step(i)
        ))
    return new_solver

def print_all_paths(solver,c):
    count = c
    s_local = Solver()
    s_local.append(solver.assertions())
    while s_local.check() == sat:
        m = s_local.model()
        path = [(m.evaluate(X[i]).as_long(), m.evaluate(Y[i]).as_long()) for i in range(max_steps+1)]
        print(f"path {count+1} :", path)

        # Block current model
        s_local.add(Or([
            Or(X[i] != m.evaluate(X[i]), Y[i] != m.evaluate(Y[i]))
            for i in range(max_steps+1)
        ]))
        count += 1
    return count

solver_module_a = module_a(s)
count_module_a = print_all_paths(solver_module_a,c=0)
print(f"Total number of paths: {count_module_a}")

C = (2, 1)

solver_module_a.add(Or([And(X[i] == C[0], Y[i] == C[1]) for i in range(max_steps + 1)]))

if solver_module_a.check() == unsat:
  print(f"No valid path includes coordinate C{C}.")
else:
  print(f"There is a valid path that includes coordinate C{C}.")

def upward_diagonal_step(i):
    return And(X[i+1] == X[i] + 1, Y[i+1] == Y[i] + 1)

min_steps = 1

def module_b(solver):
    counter = 0
    for i in range(min_steps, max_steps+1):
        new_solver = Solver()
        new_solver.add(solver.assertions())
        new_solver.add(X[i]== 6, Y[i] == 4)  
        new_solver.add([And(X[k] == 0, Y[k] == 0) for k in range(i+1, max_steps)])
        for j in range(i):
            new_solver.add(Or(
                right_step(j),
                up_step(j),
                upward_diagonal_step(j)
            ))
        if new_solver.check() == sat:
            print(f"Module B with {i} steps:")
            counter = print_all_paths(new_solver,counter)
        else:
            print(f"Module B with {i} steps: No valid paths found.")
    print(f"Total number of paths: {counter}")

module_b(s)

def module_b_ii(solver):
    new_solver = Solver()
    new_solver.add(solver.assertions())
    new_solver.add([Not(Or(And(X[i] == 2,Y[i] == 1),And(X[i] == 3,Y[i] == 2),And(X[i] == 4,Y[i] == 3))) for i in range(1,max_steps)])
    new_solver.add(X[6]== 6, Y[6] == 4)  
    new_solver.add([And(X[k] == 0, Y[k] == 0) for k in range(7, max_steps)])
    for j in range(6):
        new_solver.add(Or(
            right_step(j),
            up_step(j),
            upward_diagonal_step(j)
        ))
    if new_solver.check() == sat:
        print("There exists a minimal path of 6 steps that does NOT pass through C(2,1), D(3,2), or E(4,3):")
        print_all_paths(new_solver, 0)
    else:
        print("Not exist paths of 6 steps without pass through C(2,1), D(3,2), or E(4,3).")

module_b_ii(s)
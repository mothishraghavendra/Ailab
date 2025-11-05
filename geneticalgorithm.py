import pygad
import numpy as np

def fitness(ga_instance,solution,solution_idx):
    x = int("".join(str(int(gene)) for gene in solution),2)
    fiteness = x**2
    return fiteness

num_generations=50
num_parents_mating = 4
sol_per_pop= 10
num_genes = 5

ga_instance = pygad.GA(num_generations=num_generations,num_parents_mating=num_parents_mating,
                       fitness_func=fitness,sol_per_pop=sol_per_pop,num_genes=num_genes,
                       gene_type=int,gene_space=[0,1])

ga_instance.run()

solution,fit,sol_idx = ga_instance.best_solution()
x_best = int("".join(str(int(gene))for gene in solution),2)
print("best solution = ",solution)
print("best x value = ",x_best)
print("best fitness = ",fit)
#Stochastic Fairness Queing 

[0.001178741455078125, 0.0012102127075195312, 0.001093149185180664, 0.0010879039764404297, 0.0011639595031738281,
  0.0010128021240234375, 0.0009949207305908203, 0.000965118408203125, 0.0009589195251464844, 0.0008440017700195312]

import simpy    
import time
import random

def task(env, name, burst_time, weight, ready_queue):
    yield env.timeout(burst_time)
    print(f'{name} finished at time {env.now}')

def sfq_scheduler(env, tasks):
    ready_queue = simpy.Store(env)
    
    # Assign random weights to tasks
    for task_name, burst_time in tasks:
        weight = random.randint(1, 10)  # You can adjust the weight range as needed
        env.process(task(env, task_name, burst_time, weight, ready_queue))

if __name__ == "__main__":
    
    times = []
    for i in range(1, 11):
        start_time = time.time()  # Record the start time

        env = simpy.Environment()

        # Define the tasks as (name, burst_time) pairs
        tasks = [("Task 1", 10), ("Task 2", 9), ("Task 3", 8), ("Task 4", 7), ("Task 5", 6), ("Task 6", 5), ("Task 7", 4), 
                 ("Task 8", 3), ("Task 9", 2), ("Task 10", 1), ("Task 11", 10), ("Task 12", 9), ("Task 13", 8), ("Task 14", 7), 
                 ("Task 15", 6), ("Task 16", 5), ("Task 17", 4), ("Task 18", 3), ("Task 19", 2), ("Task 20", 1), ("Task 21", 10),
                 ("Task 22", 9), ("Task 23", 8), ("Task 24", 7), ("Task 25", 6), ("Task 26", 5), ("Task 27", 4), ("Task 28", 3),
                 ("Task 29", 2), ("Task 30", 1), ("Task 31", 10), ("Task 32", 9), ("Task 33", 8), ("Task 34", 7), ("Task 35", 6), 
                 ("Task 36", 5), ("Task 37", 4), ("Task 38", 3), ("Task 39", 2), ("Task 40", 1), ("Task 41", 10), ("Task 42", 9), 
                 ("Task 43", 8), ("Task 44", 7), ("Task 45", 6), ("Task 46", 5), ("Task 47", 4), ("Task 48", 3), ("Task 49", 2), 
                 ("Task 50", 1), ("Task 51", 10), ("Task 52", 9), ("Task 53", 8), ("Task 54", 7), ("Task 55", 6), ("Task 56", 5), 
                 ("Task 57", 4), ("Task 58", 3), ("Task 59", 2), ("Task 60", 1), ("Task 61", 10), ("Task 62", 9), ("Task 63", 8), 
                 ("Task 64", 7), ("Task 65", 6), ("Task 66", 5), ("Task 67", 4), ("Task 68", 3), ("Task 69", 2), ("Task 70", 1), 
                 ("Task 71", 10), ("Task 72", 9), ("Task 73", 8), ("Task 74", 7), ("Task 75", 6), ("Task 76", 5), ("Task 77", 4),
                 ("Task 78", 3), ("Task 79", 2), ("Task 80", 1), ("Task 81", 10), ("Task 82", 9), ("Task 83", 8), ("Task 84", 7), 
                 ("Task 85", 6), ("Task 86", 5), ("Task 87", 4), ("Task 88", 3), ("Task 89", 2), ("Task 90", 1), ("Task 91", 10), 
                 ("Task 92", 9), ("Task 93", 8), ("Task 94", 7), ("Task 95", 6), ("Task 96", 5), ("Task 97", 4), ("Task 98", 3), 
                 ("Task 99", 2), ("Task 100", 1)]

        # Run the SFQ scheduler
        sfq_scheduler(env, tasks)

        # Run the simulation
        env.run()

        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time
        
        times.append(execution_time)

        print(f"Execution time: {execution_time} seconds")
   
    print(times)

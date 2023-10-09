import simpy
import time

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

def task_generator(env, task_queue, tasks):
    for task_name, priority in tasks:
        task = Task(task_name, priority)
        task_queue.append(task)
        yield env.timeout(1)  # Generate tasks every 1 time unit

def cbq_scheduler(env, task_queue):
    while True:
        if task_queue:
            # Sort tasks by priority (higher priority first)
            task_queue.sort(key=lambda x: x.priority, reverse=True)
            
            task = task_queue.pop(0)
            print(f"Processing '{task.name}' with priority {task.priority} at time {env.now}")
            
            # Simulate processing time based on priority (adjust as needed)
            yield env.timeout(2 if task.priority >= 5 else 4)
        else:
            yield env.timeout(1)

if __name__ == "__main__":
   
    times = []
    for i in range(1,11):
        start_time = time.time()
        env = simpy.Environment()
        task_queue = []
        
        
        # Your list of tasks with priorities
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
        
        env.process(task_generator(env, task_queue, tasks))
        env.process(cbq_scheduler(env, task_queue))
        print("\n\n\n")

        env.run(10000) # Run the simulation for 100 time units or adjust as needed
        end_time = time.time()
        ex_time = end_time - start_time
        times.append(ex_time)
    print(times)
    
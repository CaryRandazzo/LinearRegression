import numpy as np
from timeit import timeit


def time_function(func, *args, reps=10):
    
    """
    Passes *args into a function, func, and times it reps times, returns the average time in milliseconds (ms).
    """
    
    avg_time = timeit(lambda: func(*args), number=reps) / reps
    
    return avg_time * 1000


def time_func2(
    func,
    vector_length,
    input_type = "array",
    data_reps = 10,
    reps = 10
):
    
    """
    Takes func, a function that perfroms a calculation on two vectors (array-lines) and   
    returns the times (in ms) the function takes to run on std. normal generated vectors.
    
    Arguments:
    ----------
    func (function): a function that perfroms a calculation on two vectors (array-lines)
    vector_length (int): the length that the radom vectors should be
    input_type (str): Vontrols the data type of the random vector. Takes values \"list\" or \"array\"
    data_reps (int): the number of times to generate the data
    reps (int): the number of time to run the timer for each data set
    """
    
    
    total_time = 0
    
    for i in range(0, data_reps):
        
        A = np.random.standard_normal(vector_length)
        B = np.random.standard_normal(vector_length)
        X = np.column_stack((np.ones(len(A),dtype=int),A))
        y = B
        
#         if input_type == "list":
#             A = list(A)
#             B = list(B)
            
#         inst_time = time_function(func, A, B, reps=reps)
        try:
            inst_time = time_function(func, X, y, reps=reps)
        except:            
            return print("ERROR:vector length must be greater than 1 AND Must have enough RAM to allocate matrices of size (n x n)")
        total_time += inst_time
    
    avg_time = total_time / data_reps
    
    return avg_time

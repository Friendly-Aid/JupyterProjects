import numpy as np

def manipulate_array(input_array):
    shape=input_array.shape
    D1=input_array.flatten()
    D1=D1[::-1]
    D1=D1.reshape(shape)
    return D1

# Example usage:
original_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result_array = manipulate_array(original_array)
print(result_array)
print("\n")

def count_unique_items(input_array):
    A,B=np.unique(input_array,return_counts=True)
    return {int(Ai):int(Bi) for Ai,Bi in zip(A,B)}

# Example usage:
input_array = np.array([1, 2, 3, 2, 1, 4, 5, 3, 6, 5, 4, 7, 8, 9, 8, 7, 6])
result_dict = count_unique_items(input_array)
print(result_dict)
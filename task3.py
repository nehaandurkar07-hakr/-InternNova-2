import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([2, 4, 5, 8, 10])
print("First Array:", arr1)
print("Second Array:", arr2)

print("\nMathematical Operations")

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Modulus:", arr1 % arr2)

print("\nStatistical Operations")

print("Mean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Minimum:", np.min(arr1))
print("Maximum:", np.max(arr1))
print("Standard Deviation:", np.std(arr1))
print("Sum:", np.sum(arr1))
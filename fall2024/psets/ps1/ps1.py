from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and singletonBucketSort functions, and for the BC helper function.
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def singletonBucketSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    """TODO: Implement Radix Sort using BC and singletonBucketSort"""
    n = len(arr)
    k = (univsize - 1).bit_length() // (base - 1).bit_length() + 1
    
    V_prime = []
    for i in range(n):
        K_i, V_i = arr[i]
        V_i_prime = BC(K_i, base, k)
        V_prime.append((V_i_prime, V_i))
    
    for j in range(k):
        K_prime = []
        for i in range(n):
            V_i_prime, V_i = V_prime[i]
            K_i_prime = V_i_prime[j]
            K_prime.append((K_i_prime, (V_i_prime, V_i)))
        
        K_prime = singletonBucketSort(base, K_prime)
        V_prime = [item[1] for item in K_prime]
    
    sorted_A = []
    for i in range(n):
        V_i_prime, V_i = V_prime[i]
        K_i = sum(V_i_prime[idx] * (base ** idx) for idx in reversed(range(k)))
        sorted_A.append((K_i, V_i))
    
    return sorted_A

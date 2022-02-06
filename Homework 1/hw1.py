#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:20:00 2021

@author: hboateng
"""
class hwone:
    def tuple_sum(A,B):
        """
        input: lists A and B of the same length, where each element in each
               list is a pair (x,y) of numbers
        output: list of pairs (x,y) in which the first element of the ith
                pair is the sum of the first element of the ith pair in
                A and the first element of the ith pair in B. Similarly, the
                second element of the ith pair is the sum of the second
                element of the ith pair of A and the second element of the 
                ith pair in B.
                Example: Given lists A = [(1,2), (10,20)] and 
                         B = [(3,4), (30,40)], tuple_sum(A,B) 
                         returns [(4,6), (40,60)]
        """
        """
        Using internal functions of tuple class: information and code structured inspired by 
        GeeksforGeeks page on adding tuples together. 
        
        Each tuple is First mapped to the sum function, but before passing the list data the zip 
        function is used to stitch each tuple at index i together which enables proper addition of elements.
        
        Finally these two numbers are passed as arguments to the parameterized constructor of the tuple class 
        which places the desired tuple in a new list to be returned by the function. 
        """
        L=[tuple(map(sum, zip(A[i], B[i]))) for i in range(len(A))]
        return L
    
    "Test code"
    "A=[(1,2), (10,20)]"
    "B=[(3,4), (30,40)]"
    "print(tuple_sum(A,B))"
    
    def inv_dict(d):
        
        """
        input: dictionary d representing an invertible function
        output: dictionary representing the inverse of f, the returned
                dictionary's keys are the values of d and its values are the
                keys of d
        Example: Given d = {'thank you': 'merci', 'goobye': 'au revoir'} ,
                 inv_dict(d) returns 
                 {'merci': 'thank you', 'au revoir': 'goobye'} 

        """
        
        """ 
        This function uses a list comprehension embedded in the dictionary paramterized constructor.
        for each element in d the key and value are swapped and placed in a list container to be passed to 
        the constructor 
        """
        inverse = dict([(value, key) for key, value in d.items()])
        return inverse
    "Test code"    
    "d = {'thank you': 'merci', 'goodbye': 'au revoir'} "
    "print(inv_dict(d))"
    
    def myUnion(L):
        """
        input : list of sets
        output: A set which is the union of all sets in L

        Example: Given L=[{1,2}, {'A','B'}], myUnion(L) returns
                 {'A','B',1, 2}

        """
        
        Union=set()
        for x in range(len(L)):
            Union=set.union(Union, L[x])
            """current =  # Fill in here"""
        return Union
    
   
    
    def transform(a,b, L):
    
        """
        input: complex numbers a and b, and a list L of complex numbers
        output: the list of complex numbers obtained by applying
                f(z) = az + b to each complex number in L
                
        Example: if a = i, b = -i and L = [1+i, 1-i], transform(a,b, L)
                 returns [i*(1+i)-i, i*(1-i)-i] = [-1,1]
        """
        T=[a*i+b for i in L]
        return T
          
    def f(z): 
        return (2j*z)+3
      
    L=[1+1j,2-1j,0+3j]
    print(sum([2j*z for z in L]))


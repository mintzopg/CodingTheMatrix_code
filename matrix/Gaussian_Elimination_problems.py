# version code f4bde2e5d0a5+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
import math
from vec import Vec
from vecutil import zero_vec



## 1: (Problem 1) Recognizing Echelon Form
# Write each matrix as a list of row lists

echelon_form_1 = [[1, 2, 0, 2, 0],
                  [0, 1, 0, 3, 4],
                  [0, 0, 2, 3, 4],
                  [0, 0, 0, 2, 0],
                  [0, 0, 0, 0, 4]]

echelon_form_2 = [[0, 4, 3, 4, 4],
                  [0, 0, 4, 2, 0],
                  [0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]]

echelon_form_3 = [[1, 0, 0, 1],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

echelon_form_4 = [[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]



## 2: (Problem 2) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[9,-1,2],[0,4,5],[0,0,2]])
        True
        >>> is_echelon([[0,4,5],[0,3,0],[0,0,2]])
        False
        >>> is_echelon([[9,10]])
        True
        >>> is_echelon([[5]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
    '''
    rows = len(A) # m rows
    if rows == 1 or rows == 0: return True
    cols = len(A[0]) # n columns
    if cols == 0: return True
    d = {} # key: row number, val: position of 1-st non zero element
    for m in range(rows):
        for n in range(cols):
            if A[m][n] != 0: # the 1st non zero...
                d[m] = n     # add in the dictionary as row #: index #
                break        # break the loop
        else:
            d[m] = -1
        
    if d[0] == -1: d[0] = float('inf')
    logic = []
    for k in range(1, rows):
        if d[k] == -1:
            logic.insert(k, True)
            tmp = True
            for j in range(k+1, rows):
                if d[j] == d[k]:
                    tmp = tmp and True
                    logic.insert(j, tmp)
                else:
                    logic.insert(j, False)    
        else:
            logic.insert(k, d[k]>d[k-1])
    
    return all(logic)   
   
       


## 3: (Problem 3) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = [1, 0, 3, 0]
echelon_form_vec_b = [-3, 0, -2, 3]
echelon_form_vec_c = [-5, 0, 2, 0, 2]



## 4: (Problem 4) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21, 0, 2, 0, 0]



## 5: (Problem 5) Echelon Solver
def echelon_solve(row_list, label_list, b):
    '''
    Input:
        - row_list: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in row_list
        - b: a vector (represented as a list)
    Output:
        - Vec x such that row_list * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    '''
    D = row_list[0].D
    assert D == set(label_list)
    x = zero_vec(D)
    for i in reversed(range(len(row_list))):
        row = row_list[i]
        for j in (range(len(D))):
            if row[label_list[j]] != 0 :
                c = label_list[j]
                x[c] = (b[i] - x*row)/row[c]
                break
    return x



## 6: (Problem 6) Solving General Matrices via Echelon
row_list = [Vec({'A', 'B', 'C', 'D'}, {'A':one, 'B':one, 'D':one}), Vec({'A', 'B', 'C', 'D'}, {'B':one}), Vec({'A', 'B', 'C', 'D'}, {'C':one}), Vec({'A', 'B', 'C', 'D'}, {'D':one})]    # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [one, one, 0, 0]          # Provide as a list of GF(2) values



## 7: (Problem 7) Nullspace A
null_space_rows_a = {3, 4} # Put the row numbers of M from the PDF



## 8: (Problem 8) Nullspace B
null_space_rows_b = {4} # Put the row numbers of M from the PDF


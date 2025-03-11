import numpy as py

#Toy BOx matrix

a = py.array ([ [2 , 7 , 3] , 
                [1 , 19 , 7] ])

def m_n (matrix):
    rows = len (matrix) 
    colums = len(matrix[0])
    return rows,colums

def norma (matrix) :
    rows,colums = m_n(matrix)
    
    norms = py.array([])
    for n in range (colums):
        results = 0
        for m in range (rows):
            results += matrix [m,n] ** 2
            
        results = results ** 0.5
        norms= py.append(norms,results)
    return norms
        
        
    
    

def qr_Construction (matrix) :
    rows,colums = m_n(matrix)
    norms=norma(matrix)
    q = py.array([matrix.T[0]/norms[0]])
   
    
    
    for n in range(1,colums ):
        proyection =py.array((py.dot(q[n-1],(matrix.T)[n]))*q[n-1])
        q =py.vstack([q,matrix.T[n]-proyection])
        
    q=q.T
    
    return q
            
        
    
    
    
    
    
    
    
qr_Construction (a)
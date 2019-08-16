import numpy as np
import math

def array():
    #creating arrays
    a = np.ones(10, dtype='int')
    print(a)
def creatingMatrix():
    #creating a 3 row x 5 column matrix
    b = np.zeros((3,5), dtype='float')
    print(b)

def matrixWithPreDefinedValue():
    #creating a matrix with a predefined value
    c = np.full((3,5),1.23)
    print(c)

def arrayWithSetSequence():
    #create an array with a set sequence
    d = np.arange(3, 20, 2)
    print(d)

def arrayWithEvenSpace():
    #create an array of even space between the given range of values
    e = np.linspace(0, 2, 5)
    print(e)
def matrix():
    #create a 3x3 array with mean and standard deviation 1 in a given dimension
    f = np.random.normal(0, 1, (3,3))
    print(f)
    print(np.mean(f))
    print(np.std(f))

def identityMatrix():
    #create an identity matrix
    g = np.eye(3)
    print(g)

    #set a random seed
    #print("===seed===")
    #print(np.random.seed(1))

def randomMatrix(): #########################################################
    x1 = np.random.randint(10, size=6) #one dimension
    x2 = np.random.randint(10, size=(3,4)) #two dimension
    x3 = np.random.randint(10, size=(3,4,5)) #three dimension
    print("=====x1====")
    print(x1)
    print("=====x2====")
    print(x2)
    print("=====x3====")
    print(x3)
    print("x3 ndim:", x3.ndim)
    print("x3 shape:", x3.shape)
    print("x3 size: ", x3.size)


def arrayIndexing():
    #Array Indexing
    x1 = np.array([4, 3, 4, 4, 8, 4])
    print(x1)
    print(x1[0])
    print(x1[4])
    print(x1[-1])
    print(x1[-2])


    x2 = np.full((3,3),np.random.randint(10,size=(3,3)))
    print(x2)
    print(x2[2,-3])
    x2[0,0]=12
    print(x2)
def arraySlicing():
    #Array Slicing
    x = np.arange(10)
    print(x)

def arrayTravserse():
    x = np.arange(10)
    #from start to 4th position
    print(x[:5])

    #from 4th position to end
    print(x[4:])

    #from 4th to 6th position
    print(x[4:7])

    #return elements at even place
    print(x[ : : 2])

def returnElements():
    x = np.arange(10)
    #return elements from first position step by two
    print(x[1::2])
    #reverse the array
    print(x[::-1])

def concateArray():
    #You can concatenate two or more arrays at once.
    x = np.array([1, 2, 3])
    y = np.array([3, 2, 1])
    z = [21,21,21]
    print(np.concatenate([x,y,z]))
def createArray2d():
    #You can also use this function to create 2-dimensional arrays.
    grid = np.array([[1,2,3],[4,5,6]])
    print(np.concatenate([grid,grid]))
def displayRowAndColumn():
    #Using its axis parameter, you can define row-wise or column-wise matrix
    grid = np.array([[1, 2, 3], [4, 5, 6]])
    print(np.concatenate([grid,grid],axis=1))

    #Concatenating 2D with 1D
def concatenating2dwith1d():
    x = np.array([3,4,5])
    grid = np.array([[1,2,3],[17,18,19]])
    print(np.vstack([x,grid]))
def nphstack():
    #Similarly, you can add an array using np.hstack
    grid = np.array([[1, 2, 3], [4, 5, 6]])
    z = np.array([[9],[12]])
    print(np.hstack([grid,z]))
def splitIndexBasedArray():
    #Splitting array based on pre defined index positions
    x = np.arange(10)


    x1,x2,x3 = np.split(x,[0,6])
    print(x1,x2,x3)



def OperationOnArray():
    a = np.arange(9, dtype = np.float_).reshape(3,3)

    print ('First array:')
    print (a)


    print ('Second array:')
    b = np.array([10,10,10])
    print (b)


    print ('Add the two arrays:')
    print (np.add(a,b))


    print ('Subtract the two arrays:')
    print (np.subtract(a,b))


    print ('Multiply the two arrays:')
    print (np.multiply(a,b))


    print ('Divide the two arrays:')
    print (np.divide(a,b))

concateArray()
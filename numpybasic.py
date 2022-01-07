import numpy as np


# +

    
edge = 3
a = np.zeros(edge*edge)


for c in range (0,(edge*edge)):
    a[c]=c


a.reshape(3,3)




# +


b=np.arange(edge,edge**2,.1)
b.reshape(6,10)

# -

return(a)

    
    assert edge > 0

def zero_border(square: np.ndarray) -> np.ndarray:
    """Return a (new) square array with a `border' of zeros.
    The returned array has the same shape as the one given.

    >>> zero_border(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    array([[0, 0, 0],
           [0, 5, 0],
           [0, 0, 0]])

    >>> x = np.array([[1, 2], [3, 4]])
    >>> y = zero_border(x)
    >>> x[0,0] != y[0,0]
    True
    >>> (y == np.zeros((2, 2), 'int32')).all()
    True

    >>> zero_border(np.ones((7,7)))
    array([[0., 0., 0., 0., 0., 0., 0.],
           [0., 1., 1., 1., 1., 1., 0.],
           [0., 1., 1., 1., 1., 1., 0.],
           [0., 1., 1., 1., 1., 1., 0.],
           [0., 1., 1., 1., 1., 1., 0.],
           [0., 1., 1., 1., 1., 1., 0.],
           [0., 0., 0., 0., 0., 0., 0.]])
    """
    assert len(square.shape) == 2 and square.shape[0] == square.shape[1]
    c = np.copy(square)
    c[0]=0
    c[:,0]=0
    c[:,-1]=0
    c[-1,:]=0
    c
    return(c)


c=zero_border


def std_array(seq: list[int]) -> list[float]:
    """Return a list with all the element standardized.
    An element is standardized by subtracting the mean of the sequence
    and dividing by the standard deviation.

    >>> std_array([1,2,3,4,5])
    [-1.414213562373095, -0.7071067811865475, 0.0, 0.7071067811865475, 1.414213562373095]

    """

    mean = seq.mean()
    sd = seq.std()
    y= (seq-mean)/sd
    return y


b=np.arange(0,5,1)
f=std_array(b)
f

# + active=""
#
# -




def fast_std_array(seq: list[int]) -> list[float]:
    """Return a list with all the element standardized.
    Make a faster version of the function std_array above
    (Hint: use numpy, but do not change the signature!)

    >>> std_array([1,2,3,4,5]) == fast_std_array([1,2,3,4,5])
    True

    >>> import timeit
    >>> slow = timeit.timeit('std_array(list(range(1, 10**6)))', number=5, globals={'std_array': std_array})
    >>> fast = timeit.timeit('fast_std_array(list(range(1, 10**6)))', number=5, globals={'fast_std_array': fast_std_array})
    >>> fast < (slow / 1.3)
    True

    """
    
    arr = np.array(seq)
    
    mean = arr.mean()
    sd = arr.std()
    
    y = (arr - mean)/sd
    return list (y)
    
    pass


x=fast_std_array(b)
x

# You can create other functions if you need them


# Do not change anything below
if __name__ == "__main__":
    import doctest, sys
    fail, _ = doctest.testmod()
    sys.exit(fail)

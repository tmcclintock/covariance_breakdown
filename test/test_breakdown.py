import covariance_breakdown as cb
import numpy as np
import numpy.testing as npt

def test_breakdown_builds():
    C = np.identity(2)
    b = cb.breakdown(C)
    return
    
def test_breakdown_exceptions():
    #Too many dimensions
    C = np.array([np.identity(2)])
    with npt.assert_raises(Exception):
        cb.breakdown(C)
    #Too few dimensions
    C = np.array(0)
    with npt.assert_raises(Exception):
        cb.breakdown(C)
    #Not symmetric
    C = np.array([[2., 0.], [1., 3.]])
    with npt.assert_raises(Exception):
        cb.breakdown(C)
    return

def test_breakdown_attributes():
    #Example covariance matrix
    C = np.array(np.identity(2))

    #Has all attributes it should have
    attrs = ["C","D","L","Lprime"]
    b = cb.breakdown(C)
    for attr in attrs:
        assert hasattr(b, attr), True
    #Test the other constructor
    D = b.D
    Lprime = b.Lprime
    b2 = cb.breakdown.from_D_Lprime(D,Lprime)
    for attr in attrs:
        assert hasattr(b2, attr), True
    return

def test_reconstruction():
    attrs = ["C","D","L","Lprime"]
    #Make a randomized covariance matrix
    sizes = [2,3,4,5,10,20]
    for size in sizes:
        A = np.random.rand(size, size)
        C = np.dot(A, A.T) #positive semi-definite matrix
        b1 = cb.breakdown(C)
        D = b1.D
        Lprime = b1.Lprime
        b2 = cb.breakdown.from_D_Lprime(D,Lprime)
        for attr in attrs:
            a1 = getattr(b1, attr)
            a2 = getattr(b2, attr)
            npt.assert_array_almost_equal(a1,a2, 1e-8)
            continue
        #Now with diagonal unraveling
        b1 = cb.breakdown(C, unravel_diagonally=True)
        D = b1.D
        Lprime = b1.Lprime
        b2 = cb.breakdown.from_D_Lprime(D, Lprime, unravel_diagonally=True)
        for attr in attrs:
            a1 = getattr(b1, attr)
            a2 = getattr(b2, attr)
            npt.assert_array_almost_equal(a1,a2, 1e-8)
            continue
        continue
    return

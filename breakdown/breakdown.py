import numpy as np

class breakdown(object):
    """
    Take in a covariance matrix and break it down into constituent parts.
    :param C:
        2D array of a covariance matrix
    """
    
    def __init__(self, C):
        C = np.array(C)

        #Error checking
        if C.ndim < 2:
            raise Exception("Covariance matrix has too few dimensions.")
        if C.ndim > 2:
            raise Exception("Covariance matrix has too many dimensions.")
        if not np.allclose(C, C.T, atol=1e-8):
            raise Exception("Covariance matrix is not symmetric.")

        #Save the covariance
        self.C = C

        #Perform GCD
        #will be slow if C is large
        #in which case swap this for a better library
        L = np.linalg.cholesky(C)
        D = L.diagonal()
        self.D = D
        self.L = L

        #Loop over the independent elements of L and save them
        ND = len(D)
        Lprime = np.zeros(ND*(ND-1)/2)
        k = 0
        for i in xrange(1,ND):
            for j in xrange(0,i):
                Lprime[k] = L[i,j]
                k+=1
                continue
            continue
        self.Lprime = Lprime

    @classmethod
    def from_D_Lprime(cls, D, Lprime):
        """
        Reconstruct a covariance matrix from a diagonal and flattened L matrix.
        The covariance C and L matrices will be self-assigned 
        and aren't returned.

        :param D:
            diagonal of decomposed covariance matrix
        :param Lprime:
            flattened lower triangular matrix from decomposition
        :return:
            None
        """
        D = np.array(D)
        Lprime = np.array(Lprime)
        if D.ndim > 1 or D.ndim == 0:
            raise Exception("D must be a 1D array")
        ND = len(D)
        if not (ND*(ND-1)/2 == len(Lprime)):
            raise Exception("Mismatched length:\n\tlen(Lprime) must be len(D)*(len(D)-1)/2")
        
        L = np.zeros((ND,ND))
        k = 0
        for i in xrange(1,ND):
            for j in xrange(0,i):
                L[i,j] = Lprime[k]
                k+=1
                continue
            continue
        Lfull = np.copy(L)
        for i in xrange(0, ND):
            Lfull[i,i] = D[i]
        C = np.dot(Lfull, Lfull.T.conj())
        return cls(C)

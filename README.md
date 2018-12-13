# covariance_breakdown

Constructing emulators of covariance matrices requires first breaking the matrix down into its constituent parts using a decomposition, and then rearranging diagonal and lower triangular data into a more useful form. This is a small package to do that.

Specifically, this packages takes in a covariance matrix, tests that it _can_ be decomposed, performs generalised Cholesky decomposition, and saves:
- the lower triangular matrix `L`
- the diagonal of the GCD `D` (which is in L)
- the flattened independent elements of L that aren't in D, `Lprime`

Additionally, the `breakdown` tool can reconstruct a covariance (and all the other parts) from `D` and `Lprime`.

## Usage

```python
#Given a covariance matrix C

from breakdown import *

C_breakdown = breakdown(C)

C_attr = C_breakdown.C #saves C as an attribute
D      = C_breakdown.D
L      = C_breakdown.L
Lprime = C_breakdown.Lprime

C_breakdown2 = from_D_Lprime(D, Lprime)
#Has all the same attributes as C_breakdown
```
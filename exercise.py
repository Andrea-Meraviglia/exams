import numpy as np # type: ignore

def laplace_five(grid: np.ndarray) -> np.ndarray:
    """Compute the Laplace operator (5-point stencil).

    >>> g = np.array([[0, 0, 0, 0],
    ...               [0, 1, 0, 0],
    ...               [0, 0, 1, 0],
    ...               [0, 0, 0, 0]])
    >>> laplace(g)
    array([[-4,  2],
           [ 2, -4]])
    """
n=2
d=5
lg=np.zeros_like(grid)
lg=lg[1:-1,1:-1]
lg = g[:-2,1:-1] + g[1:-1,:-2] + g[2:,1:-1] + g[1:-1,2:] - 4 * g[1:-1,1:-1]
u=np.zeros_like(g)
u[1:-1,1:-1] = np.random.uniform(-d, d, size=(n,n))
return

g = np.array([[0, 0, 0, 0],
               [0, 1, 0, 0],
                 [0, 0, 1, 0],
                  [0, 0, 0, 0]])
n=2
d=5
lg=np.zeros_like(g)
lg=lg[1:-1,1:-1]
lg = g[:-2,1:-1] + g[1:-1,:-2] + g[2:,1:-1] + g[1:-1,2:] - 4 * g[1:-1,1:-1]
print()
u=np.zeros_like(g)
u[1:-1,1:-1] = np.random.uniform(-d, d, size=(n,n))
print(u)

# +
v=np.random.uniform(0,5,(1,4,4))

v.shape[0]=0
print(v)

# +
n=2
r=5

U = np.zeros((n+2,n+1))
U[U.shape[0]//2 - r//2 : U.shape[0]//2 + r//2, U.shape[0]//2 - r//2 : U.shape[0]//2 + r//2]=4
r = np.shape(U)
print(U)
print(r)
# -

u=[1,2,3,4,5],[6,7,8,9,33]
u=np.pad(u,1)
print(u)

U, V = np.random.normal(loc=0, scale=0.05, size=(n, n)), np.random.normal(loc=1, scale=0.05, size=(n, n))
U, V = np.pad(U, 1), np.pad(V, 1)
print(U)
print(V)





def laplace_nine(grid: np.ndarray) -> np.ndarray:
    """Compute the Laplace operator (9-point stencil).

    >>> g = np.array([[0, 0, 0, 0],
    ...               [0, 1, 0, 0],
    ...               [0, 0, 1, 0],
    ...               [0, 0, 0, 0]])
    >>> laplace8(g)
    array([[-7,  2],
           [ 2, -7]])
    """
    # TODO (Optional)
    pass



def gray_scott(u: np.ndarray, v: np.ndarray,
               d_u: float, d_v: float,
               f: float, k: float) -> tuple[np.ndarray, np.ndarray]:
    """Compute a new pair of matrices with updated values after a time unit.

    d_u, d_v are diffusion rates of chemicals U and V.
    f is the rate of conversion of U and V in V (U + V -> 3V)
    k is the rate of conversion of V in P (V -> P, not represented)
    """
    # TODO
    pass

def init_square(n: int,
                r: int = 20, u_0: float = 0.5, v_0: float = 0.25,
                d: float = .05) -> tuple[np.ndarray, np.ndarray]:
    """Create a pair of matrices (n+2, n+2).

    The matrices have a zero border.
    The inner part of the first one is 1 +/- a uniform random choice between [-d, d].
    The inner part of the second one is 0 +/- a uniform random choice between [-d, d].
    A central square seed is set to fixed values (u_0, v_0) with edge r. 
    """
    # TODO
    pass

def init_circle(n: int,
                r: int = 20, u_0: float = 0.5, v_0: float = 0.25,
                d: float = .05) -> tuple[np.ndarray, np.ndarray]:
    """Create a pair of matrices (n+2, n+2).

    The matrices have a zero border.
    The inner part of the first one is 1 +/- a uniform random choice between [-d, d].
    The inner part of the second one is 0 +/- a uniform random choice between [-d, d].
    A central circle seed is set to fixed values (u_0, v_0) with edge r. 
    """
    # TODO (Optional)
    pass


def init_normal(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Create a pair of matrices (n+2, n+2).

    The matrices have a zero border.
    The inner part of the first one is a normal random choice with mean=0, std=0.05.
    """
    U, V = np.random.normal(loc=0, scale=0.05, size=(n, n)), np.random.normal(loc=1, scale=0.05, size=(n, n))
    U, V = np.pad(U, 1), np.pad(V, 1)

    return U, V



if __name__ == '__main__':
    U, V = init_normal(256)
    Du, Dv, f, k = .16, .08, .025, 0.055

    import matplotlib.pyplot as plt                # type: ignore
    from matplotlib.animation import FuncAnimation # type: ignore

    # TODO Setup the graphics
    # 2 subplots (imshow) must be called im_U and im_V
    im_U = None
    im_V = None

    def update(frame):
        global U, V, im_V, im_U

        if frame % 100 == 0:
            print(frame)

        for _ in range(20):
            U, V = gray_scott(U, V, Du, Dv, f, k)
            assert not np.isinf(V).any(), f'V {frame}'
            assert not np.isinf(U).any(), f'U {frame}'

        im_V.set_data(V)
        im_U.set_data(U)

    a = FuncAnimation(fig, update, interval=10, frames=2000)
    plt.show()



import numpy as np # type: ignore

def laplace_five(grid: np.ndarray) -> np.ndarray:
    """Compute the Laplace operator (5-point stencil).
    >>> g = np.array([[0, 0, 0, 0],
    ...               [0, 1, 0, 0],
    ...               [0, 0, 1, 0],
    ...               [0, 0, 0, 0]])
    >>> laplace_five(g)
    array([[-4,  2],
           [ 2, -4]])
    """
    res = grid[1:-1,1:-1].copy()
    

    res = grid[1:-1,2:] + grid [1:-1,:-2] + grid [2:,1:-1] + grid[:-2,1:-1] - 4 * grid[1:-1,1:-1]
   
    
    return res



def laplace_nine(grid: np.ndarray) -> np.ndarray:
    """Compute the Laplace operator (9-point stencil).
    >>> g = np.array([[0, 0, 0, 0],
    ...               [0, 1, 0, 0],
    ...               [0, 0, 1, 0],
    ...               [0, 0, 0, 0]])
    >>> laplace_nine(g)
    array([[-7,  2],
           [ 2, -7]])
    """
    res = grid[1:-1,1:-1].copy()
    
    res = grid[:-2,:-2] + grid[:-2,1:-1] + grid[:-2,2:] + grid[1:-1,:-2] + grid[1:-1,2:] + grid[2:,:-2] + grid[2:,1:-1] + grid[2:,2:] - 8 * grid[1:-1,1:-1]
    return res


def gray_scott(u: np.ndarray, v: np.ndarray,
               d_u: float, d_v: float,
               f: float, k: float) -> tuple[np.ndarray, np.ndarray]:
    """Compute a new pair of matrices with updated values after a time unit.
    d_u, d_v are diffusion rates of chemicals U and V.
    f is the rate of conversion of U and V in V (U + V -> 3V)
    k is the rate of conversion of V in P (V -> P, not represented)
    """
    u2 = u.copy()
    v2 = v.copy()

    U,V = u[1:-1,1:-1], v[1:-1,1:-1]

    Lu = laplace_five(u)
    Lv = laplace_five(v)

    
    partial_u = d_u*Lu - U*(V**2) + f*(1 - U)
    partial_v = d_v*Lv + U*(V**2) - (f + k)*V

    u2[1:-1,1:-1] = u2[1:-1,1:-1] + partial_u
    v2[1:-1,1:-1] = v2[1:-1,1:-1] + partial_v
    
    return (u2,v2)


def init_square(n: int,
                r: int = 20, u_0: float = 0.5, v_0: float = 0.25,
                d: float = .05) -> tuple[np.ndarray, np.ndarray]:
    """Create a pair of matrices (n+2, n+2).
    The matrices have a zero border.
    The inner part of the first one is 1 +/- a uniform random choice between [-d, d].
    The inner part of the second one is 0 +/- a uniform random choice between [-d, d].
    A central square seed is set to fixed values (u_0, v_0) with edge r.
    """
   
        
    U = np.zeros((n+2,n+2))
    V = np.zeros((n+2,n+2))
    
    U [1:-1,1:-1] = 1+np.random.uniform(-d, d, size=(n,n))
    V [1:-1,1:-1] = 0+np.random.uniform(-d, d, size=(n,n))
    U[U.shape[0]//2 - r//2 : U.shape[0]//2 + r//2, U.shape[0]//2 - r//2 : U.shape[0]//2 + r//2]=u_0
    V[V.shape[0]//2 - r//2 : V.shape[0]//2 + r//2, U.shape[0]//2 - r//2 : U.shape[0]//2 + r//2]=v_0

    return U,V


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
    U, V = init_square(256)
    Du, Dv, f, k = .16, .08, .025, 0.055

    import matplotlib.pyplot as plt                # type: ignore
    from matplotlib.animation import FuncAnimation # type: ignore

    fig, ax = plt.subplots(nrows=2, ncols=2)
    im1 =ax[0,0].imshow(U)
    ax[0,0].set_title('Initial U')
    im2 =ax[0,1].imshow(V)
    ax[0,1].set_title('Initial V')
    ax[1,0].set_title('U(t)')
    ax[1,1].set_title('V(t)')

    
    im_U = ax[1,0].imshow(U)
    im_V = ax[1,1].imshow(V)

    plt.tight_layout()
    

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





for x in (1,2,3):
    print (x)



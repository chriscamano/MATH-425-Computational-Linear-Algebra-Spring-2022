from plotting import plot
from math import e, pi
S=[complex(2,2),complex(3,2),complex(1.75,1),complex(2,1),complex(2.25,1),complex(2.75,1),complex(3,1),complex(3.25,1)]


plot(S,4)
plot({1 + 2j + z for z in S}, 4)


n=20
w=e**(complex(0,(2*pi)/n))
L=[w**i for i in range(n) if i >0]
plot(L,5)
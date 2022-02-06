from plotting import plot
from math import e, pi
from image import file2image,color2gray
S=[complex(2,2),complex(3,2),complex(1.75,1),complex(2,1),complex(2.25,1),complex(2.75,1),complex(3,1),complex(3.25,1)]

#-----------
#part 2
#----------
#plot(S,4)

#------
#part3
#Create a new plot using a comprehension to provide a set of points derived from S by
#adding 1 + 2i to each
#-----
#plot({1 + 2j + z for z in S}, 4)

#------
#part 5 plot all numbers of the form e^2pii/n from n=1-20
#------
n=20
w=e**(complex(0,(2*pi)/n))
L=[w**i for i in range(n) if i >0]
#plot(L,5)

#-----------
#part 6
#----------
#multiply by e^pi/4i for 45 degree rotation and scale by 1/2 
H=[i*.5*e**(pi/4*1j) for i in S ]
#plot(H,4)

#------
#part 7 Center the points of S at origin 
#------
def rePosition(arg1):
    a=arg1.real-2.5
    b=arg1.imag-1.5
    return complex(a,b)

f=[rePosition(z) for z in S]
plot(f,4)

#------
#part 8  Center the points, rotate by pi/4 scale by 1/2 
#------
f2=[rePosition(i)*e**(pi/4*1j)*1/2 for i in S]
plot(f2,4)

#------
#Question 2
#------

#------
#part 1
#------
data = color2gray(file2image("img01.png"))
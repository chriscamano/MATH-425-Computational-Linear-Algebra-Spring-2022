from vec import Vec

D1={0,1,2}

F1={0:-1,1:1,2:1}
F2={0:2,1:-1,2:5}

u=Vec({i for i in F1},F1)
v=Vec({i for i in F2},F2)

print( u+v)
print(2*v-u)
print(v+2*u)
print(v-u)
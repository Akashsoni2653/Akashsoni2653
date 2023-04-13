#tuppples are immutable
tupple_1 = (1,2,3,4,5,6,6,2)
#unpacking  
# assigning each value of this tppple to an var
# old school method
a = tupple_1[0]
b = tupple_1[2]
print(f"{a} and {b}")
# unpacking method
a,b,c,d,e,f,g,h = tupple_1
print(f"{a} {b} {c} {d} {e} {f} {g} {h}")
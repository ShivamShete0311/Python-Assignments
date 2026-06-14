#Since Python reuses immutable values, both varaibles with same value will show same memory address

a = 10
b = 10

print(id(a))                #140728904172952  
print(id(b))                #140728904172952


#Since lists are mutable, both varaibles with same value will show different memory address

A = [10]
B = [10]
print(id(A))                #2105939047360
print(id(B))                #2105938931648
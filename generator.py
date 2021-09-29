def gene_function():
    li = [45,32,56,31,22,24,56,232,567]
    for x in li:
        # print(x)
       
        yield x
    

val = gene_function()
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print('size',val.__sizeof__())
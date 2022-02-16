def zip_function(tuple1,tuple2: tuple):
    sub_tuple=[]
    if len(tuple1) < len(tuple2):
      for i in range(len(tuple1)):
            sub_tuple.append((tuple1[i],tuple2[i]))
      return tuple(sub_tuple)
    else:
      for i in range(len(tuple2)):
            sub_tuple.append((tuple1[i], tuple2[i]))
      return tuple(sub_tuple)



A=('a', 'b', 'c', 'd')
B=('1','3','5','7','9')
print(zip_function(A,B))






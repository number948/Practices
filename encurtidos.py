import pickle


#numeros = 12.3
f = open("test.pick","wb")
pickle.dump(12.3, f)
pickle.dump([1,2,3], f)

f.close()
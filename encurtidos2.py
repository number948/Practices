import pickle

f = open("test.pick","rb")
x = pickle.load(f)
y = pickle.load(f)
print(x)
print(y)
print(type(x))
print(type(y))
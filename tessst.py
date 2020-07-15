list_test=[1,2,3,4,5,6]
list_test_2=[]
c=10
for i in list_test:
    print(i)
    print("This is the change i would revert")
    list_test_2.append(c)
    c=c+1
print(list_test_2)

print("I want to check this line")


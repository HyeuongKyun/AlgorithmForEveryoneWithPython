
def Couple(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            print(list[i] + ' - ' + list[j])
     
list = ['Tom', 'Jerry', 'Mike']
Couple(list)






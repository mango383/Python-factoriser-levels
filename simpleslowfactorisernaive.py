#initialisation sequence initiated beep boop
num = int(input("what number:"))
factors = []
factorsfilt = []
finalfactorisation = ''
#this will check the smallest factor, divide by it as many times as possible and then repeat,
# searching higher since the previous prime factor is not important
for i in range(2,num):
    if num%i == 0:
        #remove this prime factor 
        while num%i ==0:
            num = num/i
            factors.append(i)
#get a list factorsfilt that contains only one of each factor
for i in factors:
    if i not in factorsfilt:
        factorsfilt.append(i)
#for each 
for i in factorsfilt:
    if factors.count(i)==1:
        finalfactorisation = finalfactorisation+f"{str(i)}" + '*'
    else:
        finalfactorisation = finalfactorisation+f"{str(i)}^{factors.count(i)}" + '*'
print(finalfactorisation[0:-1])
#if its prime
if finalfactorisation == '':
    print("PRIME JACKPOT")

        
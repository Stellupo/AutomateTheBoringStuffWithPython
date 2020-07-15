def collatz(number):

            if (number)%2==0 : #si number est pair
                    number=number//2
                    print (number)
                    return number
            elif (number)%2==1:  #si number est impair
                    number=3*number+1
                    print (number)
                    return number



while True:
    print('Enter number')
    n= input()
    try:
        while n!=1:
            n=collatz(int(n))
    except ValueError:
        print('Enter a proper number!')




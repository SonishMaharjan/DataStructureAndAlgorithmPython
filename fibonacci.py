import time


def fibonacci(n):

    if n==1 or n==2:
        return 1
    else:
        result = fibonacci(n-1)+fibonacci(n-2)
        return result


def fibonacci_memo(n,memo):
    """thi si fibonacci series with meoization"""
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2:
        return 1
    else:
        result = fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
    memo[n]= result
    return result


def fibonacci_bottomUp(n):
    arr = [None]*(n+1)

    for i in range(1,n+1):
        if i ==1 or i==2:
            arr[i]=1
        else:
            arr[i] = arr[i-1]+arr[i-2]
    return arr[n]



if __name__=="__main__":

    n=30

    #normal fibonacci
    t1 = time.time()
    print(fibonacci(n))

    t2 = time.time()

    print("Normaal fibonacci Time required: ",t2-t1)




    #fibonacci with memoization...
    memo=[None]*(n+1)

    t1 = time.time()
    print(fibonacci_memo(n, memo))
    t2 = time.time()

    print("Memoization fibonacci Time required: ", t2 - t1)



    #fibonacci bottom up
    t1 = time.time()
    print(fibonacci_bottomUp(n))
    t2 = time.time()

    print("Bottom up fibonacci Time required: ", t2 - t1)




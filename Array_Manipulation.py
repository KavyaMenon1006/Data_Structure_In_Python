'''The program inputs n array and uses k is the value to be added in the query and a b are starting and ending points of the array on which we add the value k the result will be the maximum value in the query '''
def arrayManipulation(n, queries):
    arr=[0]*(n+1)
    for a,b,k in queries:
        arr[a-1]+=k
        if b<n:
            arr[b]-=k
    Maximum=temp=0
    for value in arr:
        temp+=value
        Maximum=max(Maximum,temp)
    return Maximum

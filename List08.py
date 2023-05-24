def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    k=[]
    while i<len(list1):
        if list1[i]==1:
            k.append(True)
        else:
            k.append(False)
        i+=1
    return k
                       
print(main([1,0,1,0,1,1,1,1,0,0,1]))
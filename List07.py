def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    k=[]
    while i<len(list1):
        if list1[i]==1:
            k.append(1)
        else:
            k.append(False)
        i+=1
    return k
                       
print(main([1,0,1,0,1]))
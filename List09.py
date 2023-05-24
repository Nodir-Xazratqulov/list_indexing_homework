def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    k=[]
    while i<len(list1):
        if list1[i]==1:
            k.append(True)
        else:
            k.append(False)
        i+=1
        break
    return k
                       
print(main([1,1,1,1,1,1]))
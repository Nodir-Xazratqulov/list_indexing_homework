def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
   
    # return max(list_num[0],list_num[-1])
    i=0
    max=0

    while i<len(list_num):
        
        if list_num[i]>max:
            max=list_num[i]
        i+=1
    list_num.remove(max)
    j=0
    max1=0
    while j<len(list_num):
        
        if list_num[j]>max1:
            max1=list_num[j]
        j+=1
    return max1
print(main([12, 32, 1, 4, 33]))
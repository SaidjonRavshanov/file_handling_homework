def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data)
    data=f.read()
    f.close()
    l=data.split('\n')
    k=[]
    for i in l:
        k.append(len(i))
    return k
print(main("./data/data06.txt"))

def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data)
    data=f.read()
    f.close()
    k=0
    for i in data:
        if i.isdigit():
            k+=int(i)
    return k
print(main("./data/data07.txt"))
def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data)
    data=f.read()
    f.close()
    k=0
    for i in data.split('\n'):
        k=max(k,len(i))
    return k
print(main("./data/data10.txt"))
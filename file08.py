def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
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
            k=max(k,int(i))
    return k
print(main("./data/data08.txt"))
# Read data from file
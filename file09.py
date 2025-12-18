def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data)
    data=f.read()
    f.close()
    k=9
    for i in data:
        if i.isdigit():
            k=min(k,int(i))
    return k
print(main("./data/data09.txt"))
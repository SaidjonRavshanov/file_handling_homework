def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    data = f.read()
    f.close()
    l=[]
    for i in data:
        if not i.isdigit():
            l+=i
    return l

print(main("./data/data04.txt"))
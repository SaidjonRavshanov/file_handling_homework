def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data)
    data=f.read()
    count=0
    for i in data:
        if not i.isdigit():
            count+=1
    f.close()
    return [len(data),count]
print(main("./data/data05.txt"))
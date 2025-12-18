def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data)
    data=f.read()
    list_data = data.split(',')
    f.close()
    return list_data
print(main("./data/data01.txt"))

from read_data import fromJson
import datetime

def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    count=0
    for i in data["messages"]:
        if i["type"]=="message":
            if f'{month}'==i["date"][5:7]:
                count+=1
    
    return count

print(get_post_month(fromJson("data/result.json"),11))
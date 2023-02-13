from read_data import fromJson

def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    st=set()
    for i in data["messages"]:
        if i["type"]=="service" or i["type"]=="message":
            st.add(i["date"][5:7])
    d=dict()
    for i in st:
        d[i]=0
    st=set()
    for i in data["messages"]:
        if i["type"]=="service" or i["type"]=="message":
            d[i["date"][5:7]]+=1
    return d
print (get_post_per_month(fromJson("data/result.json")))
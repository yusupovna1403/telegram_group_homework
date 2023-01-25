from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    lst = []
    messages = data['messages']
    for user in messages:
        if user['type'] == 'service':
            if user['actor_id'] not in lst:
                lst.append(user['actor_id'])
        else:
            if user['from_id'] not in lst:
                lst.append(user['from_id'])
    
    return lst

data = read_data('data//result.json')
print(find_all_users_id(data))
    
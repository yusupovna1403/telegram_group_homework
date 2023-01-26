from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    sum = 0
    messages = data['messages']
    for user in messages:
        if user['type'] == 'message':
            sum += 1
    
    return sum

data = read_data('data//result.json')
print(find_number_of_messages(data))
    
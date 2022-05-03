#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%% imports 
import re



def sanity_check():

    return True


def get_chat_message(row):
    
    message = re.split(r'> ', row)
    return "> ".join(message[1:])


#R.A
def get_current_date(dateline):
    """    Parse the IRC log date format to find the current date
    Return a POSIX (datetime) form date for midnight
    Args:
        dateline (str): Row that begins with `---`
    Returns:
        datetime: datetime object with the date from the row 
    """
    pass




def get_hours_minutes(time_row):

    hour_minute={}
    hour_minute['hour'] = 1
    return hour_minute

   
#R.A
#(NOT COMPLETED) save this for last
def get_join_quit_type(row):
    """Returns if a row is a join or a quit,
    Args:
        row (str): join or quit row
    Returns:
        str: "join" or "quit"
    """
    joinQuit = re.search(r'join','quit','left', row)
    return joinQuit



def get_join_quit_username(row):

    joinQuitUser = re.search(r'(-!-)\s(.*) \[.*@', row)
    return joinQuitUser.group(2)




def get_user_name(row):
 
    user_name = re.search(r'<.(.*?)>',row)
    return user_name.group(1)



#R.A
def get_user_prefix(row):
    """ Gets the prefix of a username, if any.
    If there is not a prefix, return None.
    For example, '@' or '+'.
    Args:
        row (str): chat message row.
    Returns:
        str: the user prefix (if any)
    """
    pass





def is_date_row(row):
    
    if re.search(r'---', row):
        return True
    return False



#R.A
def is_join_quit(row):
    """
    Check if message is a join/quit/metadata row.
    Row contains -!- at the start
    Parameters
    ----------
    row : str
        row that you want to check.
    
    Returns
    -------
    bool
        DESCRIPTION.
    """
    pass



def is_message(row):

    if row[6] == '<':
        return True
    return False



def find_urls(text):

   urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(text))
   return urls


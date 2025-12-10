#2- Authentication and authorization

import functools
#Simulated user database
users_db = {
    'ankit': {'password':'pass123', 'authenticated':True},
    'amit' : {'password':'pass123', 'authenticated':True},
    'ayush': {'password':'guest', 'authenticated':False}
}

def login_required(func):
    """Simple authentication decorator"""
    @functools.wrap(func)
    def wrapper(username, *args, **kwargs):
        #check if user exists and is authenticated 
        user = users_db.get(username)
        if not user:
            return f"Error: User '{username}' not found"
        if not user['authenticated']:
            return f"Error: User '{username}' not authenticated. Please login first."
        
    #If authenticated, call the original function
        return func(username, *args, **kwargs)
    return wrapper

#Usage
@login_required
def view_profile(username):
    return f"Welcome to your profile, {username}!"

@login_required
def view_settings(username):
    return f"Here are your settings, {username}"

#Test the decorator 
print("===Authentication Test===")
print(view_profile("ankit")) #Works - user is authenticated
print(view_profile("amit")) #Works - user is authenticated
print(view_profile("ayush")) #Fails - not authenticated
print(view_profile("unknown")) #Fails - user doesn't exist
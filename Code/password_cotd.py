"""A website requires the users to input username and password to register. Write a function to check the validity of password input by users.
	Following are the criteria for checking the password:
	
	 
	
	- At least 1 letter between [a-z]
	- At least 1 number between [0-9]
	- At least 1 letter between [A-Z]
	- At least 1 character from [$#@]
	- Minimum length of transaction password: 6
	- Maximum length of transaction password: 12
	
	 
	
	Your program should accept a list of passwords of an indeterminate length and will check them according to the above criteria. Passwords that match the criteria are to be returned in a list.
	
	 
	
	Example
	
	 
	
	If the following passwords are given as input to the program:
	["ABd1234@1","a F1#","2w3E*","2We3345"]
	Then, the output of the program should be:
	["ABd1234@1"]"""

def check_password(list_of_pw):
    accepted = []
    symbols = ['$', '@', '#']
    for i in range (len(list_of_pw)):
        if len(list_of_pw[i]) <= 12 and len(list_of_pw[i]) >= 6:
                if any(char.isdigit() for char in list_of_pw[i]):
                    if any (char.isupper() for char in list_of_pw[i]):
                        if any (char.islower() for char in list_of_pw[i]):
                            if any(char in symbols for char in list_of_pw[i]):
                                accepted.append(list_of_pw[i])
    return accepted

list_of_pw = ['ABd1234@1', 'a F1#', '2w3E', '2We3345']

print(check_password(list_of_pw))
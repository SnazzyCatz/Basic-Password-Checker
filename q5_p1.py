PasswordValidity = False

while (PasswordValidity == False):
    Username = input('Please Enter Your Username')
    Password = input('Please Enter Your Password')
    #Checks For Password Length
    if ((len(Password) < 6) | (len(Password) > 20)):
        print('Invalid Password, Try Again')
        continue
    #Checks for upper, lower, number, and special characters
    hasUpper = False
    hasSpecial = False
    hasNumber = False
    for character in Password:
        if character.isupper() == True:
            hasUpper = True
        if character.isnumeric() == True:
            hasNumber = True
        if ((character.isupper() == False) & (character.islower() == False) & (character.isnumeric() == False)):
            hasSpecial = True
    if((hasUpper == False) | (hasNumber == False) | (hasSpecial == False)):
        print('Invalid Password, Try Again')
        continue
    #Checks if two 3 letter substrings match in the password
    passLength = len(Password) - 1
    counter = 0
    substringList = []
    while (counter <= (passLength - 2)):
        substringList.append(Password[counter:counter + 3])
        counter += 1
    if(len(substringList) != len(set(substringList))):
        print('invalid password, Try Again')
        continue
    #Checks if password is a Palindrome
    isPalindrome = True
    for i in range(0,int(len(Password)/2)):
        if Password[i] != Password[len(Password)-i-1]:
            isPalindrome = False
    if(isPalindrome == True):
        print('Invalid Password, Try Again')
    #Checks if number of unique characters is high enough
    dupeList = []
    for i in range(0,len(Password)):
        dupeList.append(i)
    uniqueList = []
    for i in dupeList:
        if i not in uniqueList:
            uniqueList.append(i)
    if(len(uniqueList) < (len(Password)/2)):
        print('Invalid Password, Try Again')
        continue
    #Checks if username or reverse of username is in password
    compList = []
    reverseList = []
    count = 0
    revCount = 0
    userLength = len(Username) - 1
    reverseUser = Username[::-1]
    if (len(Username) < len(Password)):
        while count <= (len(Password) - userLength - 1):
            compList.append(Password[count:(count + userLength + 1)])
            count += 1
    if Username in compList:
        print('Invalid Password, Try Again')
        continue
    if reverseUser in compList:
        print('Invalid Password, Try Again')
        continue

     #All Conditions have been met if it reaches this point
    print('Account Creation Successful')
    break
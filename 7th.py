def passwd_check(passwd):
    
    SpecialSym=['!','"','#','$','%','&',"'",'(',')','*','+','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']
    return_val=True
    if len(passwd) < 6:
        print(' Password length should be at least 6 char long')
        return_val=False
    if len(passwd) > 16:
        print(' Password length should be not be greater than 8')
        return_val=False
    if not any(char.isdigit() for char in passwd):
        print(' Password should have at least one numerical Value')
        return_val=False
    if not any(char.isupper() for char in passwd):
        print(' Password should have at least one uppercase letter')
        return_val=False
    if not any(char.islower() for char in passwd):
        print(' Password should have at least one lowercase letter')
        return_val=False
    if not any(char in SpecialSym for char in passwd):
        print(' Password should have at least one of the symbols !"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
        return_val=False
    if return_val:
        print('Valid password')
    return return_val


passwd = input('Enter the password : ')
passwd_check(passwd)

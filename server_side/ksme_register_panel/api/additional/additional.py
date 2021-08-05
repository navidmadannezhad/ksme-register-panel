import re

def isEnglish(value):

    try:
        value.encode('utf-8').decode('ascii')
        return True # is completely english

    except UnicodeDecodeError: # it is completely persian, or a mix of persian and english
        pattern = re.compile('[a-zA-Z0-9$@$!%*?&#^-_.+]+')
        if pattern.findall(value):
            return True
        else:
            return False


def verificationToken():
    pass

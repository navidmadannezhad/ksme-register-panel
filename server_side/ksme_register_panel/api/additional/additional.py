import re

def isEnglish(value):

    try:
        value.encode('utf-8').decode('ascii')
        return True

    except UnicodeDecodeError:
        pattern = re.compile('[a-zA-Z0-9$@$!%*?&#^-_. +]+')
        if pattern.findall(value):
            return True
        else:
            return False


def verificationToken():
    pass

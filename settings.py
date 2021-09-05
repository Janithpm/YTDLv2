from db import DEFAULT_CONFIGS, CONFIG_FILE

def checkValidity(conf):
    return conf == "True"

def removeNewline(listOfStrings):
    return [string.rstrip('\n') for string in listOfStrings]


def extract(conf):
    conf = removeNewline(conf)
    return conf[0], int(conf[1]), checkValidity(conf[2]), checkValidity(conf[3])
    

def getSettings():
    try:
        with open(CONFIG_FILE, 'r') as config:
            conf = config.readlines()
            return extract(conf)
    except:
        with open(CONFIG_FILE, 'w') as config:
            for conf in DEFAULT_CONFIGS:
               config.write(conf)
        return extract(DEFAULT_CONFIGS)


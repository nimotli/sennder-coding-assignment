import json
from os.path import dirname,join,abspath

def getEnv(activeProfile):
    configPath = join(dirname(dirname(dirname(abspath(__file__)))),"resources\profile")
    if activeProfile == "dev":
        configPath=join(configPath,"application-dev.json")
    elif activeProfile == "test":
        configPath=join(configPath,"application-test.json")
    else :
        configPath=join(configPath,"application-prod.json")

    env = json.load(open(configPath))
    return env
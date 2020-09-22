import json
from os.path import dirname,join,abspath

def getEnv(activeProfile):
    configPath = join(dirname(dirname(dirname(abspath(__file__)))),"resources")
    if activeProfile == "dev":
        configPath=join(configPath,"application-dev.json")
    else :
        configPath=join(configPath,"application-prod.json")

    env = json.load(open(configPath))
    return env
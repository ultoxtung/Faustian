import ruamel.yaml as yaml

def loadConf(configfile):
    with open(configfile) as stream:
        try:
            conf = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return None, exc
    return conf, None
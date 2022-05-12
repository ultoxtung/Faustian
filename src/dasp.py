import src.helper as helper

class DASP:
    def __init__(self):
        datafile = './data/dasp.yaml'
        conf, exc = helper.loadConf(datafile)
        if exc is None:
            self.data = conf['error']
        else:
            raise exc

    def getByCode(self, code):
        return self.data[code]
import docker
import os
import requests

import src.helper as helper


DEFAULT_TIMEOUT = 10


class Result:
    def __init__(self, name, codes):
        self.name = name
        self.codes = codes


class Tool:
    def __init__(self, configname, logPath):
        self.logPath = logPath
        configfile = './config/{}'.format(configname)
        conf, exc = helper.loadConf(configfile)
        if exc is None:
            if (conf['image'] == ''):
                raise Exception('Invalid tool running command')
            if (conf['type'] not in ['flag', 'boolean-flag']):
                raise Exception('Invalid flag config')
            self.config = conf
        else:
            raise exc

    def checkLine(self, line, flag) -> bool:
        if self.config['type'] == 'boolean-flag':
            f = line.find(flag)
            if (f != -1) and (line.find('true', f+len(flag)) != -1):
                return True
        elif self.config['type'] == 'flag':
            if line.find(flag) != -1:
                return True
        else:
            return False

    def parse(self, toolOutput):
        codeList = []

        lines = toolOutput.split('\n')
        for flag, code in self.config['flag'].items():
            for line in lines:
                if self.checkLine(line.lower(), flag.lower()):
                    codeList.append(code)
        
        codeList = list(dict.fromkeys(codeList))
        return codeList

    def run(self, filepath):
        absPath = os.path.realpath(filepath)
        path = absPath.rsplit('/', 1)[0]

        client = docker.from_env()

        try:
            client.images.get(self.config['image'])
        except docker.errors.ImageNotFound:
            print('INFO: Pulling image {}...\r'.format(self.config['image']))
            client.images.pull(self.config['image'])

        container = client.containers.run(image=self.config['image'], command=self.config['command'] + ' ' + absPath,
            mounts=[docker.types.Mount(path, path, type='bind')], detach=True)
        try:
            container.wait()
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            # according to the docs, timeout gives ReadTimeout, but sometimes it is ConnectionError
            pass

        output = container.logs(follow=False)
        with open('{}/{}.log'.format(self.logPath, self.config['name']), 'w+') as f:
            f.write(output.decode("utf-8"))

        codeList = self.parse(output.decode("utf-8"))
        return Result(self.config['name'], codeList)
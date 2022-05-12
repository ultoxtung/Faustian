import os

from src.dasp import DASP


CODE_COUNT = 10


class Synthesizer:
    def __init__(self):
        self.dasp = DASP()
        self.renderHeader()
        
    def renderHeader(self):
        headerPath = './data/header.txt'
        if os.path.exists(headerPath):
            header = open(headerPath).readlines()
        for line in header:
            print(line.strip('\n') + '\r')
        print('\r')

    def loadTools(self, tools):
        self.toolList = [[] for i in range(CODE_COUNT + 1)]
        toolName = []

        for tool in tools:
            codeCnt = [0 for i in range(CODE_COUNT + 1)]
            toolName.append(tool.config['name'])
            for flag, code in tool.config['flag'].items():
                if codeCnt[code] == 0:
                    codeCnt[code] += 1
                    self.toolList[code].append(tool.config['name'])

        print('INFO: Finished loading tools. Found {} tool(s): {}\r'.format(len(tools), ', '.join(toolName)))

    def renderRun(self):
        print('INFO: Running, please wait...\r')

    def renderResult(self, resultList):
        found = False

        for code in range(1, CODE_COUNT + 1):
            detectedTool = []
            for result in resultList:
                if code in result.codes:
                    detectedTool.append(result.name)

            if len(detectedTool) > 0:
                if not found:
                    print('INFO: Vunerability found!\r')
                    print('INFO: Analysis result:\r')
                    found = True

                print('| Code {}: {}\r'.format(code, self.dasp.getByCode(code)['name']))
                print('| └> Detected by: {}\r'.format(', '.join(detectedTool)))
            
                notDetectedTool = [item for item in self.toolList[code] if item not in detectedTool]
                if len(notDetectedTool) > 0:
                    print('| └> Not detected by: {}\r'.format(', '.join(notDetectedTool)))
                
                a = len(detectedTool)
                b = len(self.toolList[code])
                print('| └> Ratio: {}/{} ({}%)\r'.format(a, b, 100 * a // b))    
                        
        if not found:
            print('INFO: No vulnerability detected! Looks great!\r')
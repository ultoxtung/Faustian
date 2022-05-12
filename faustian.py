import argparse
import multiprocessing as mp

from datetime import datetime
from os import walk, mkdir

from src.tool import Tool
from src.synthesizer import Synthesizer


output = mp.Queue()


def worker(obj, source):
    output.put(obj.run(source))


def faustian(sourcefile):
    synth = Synthesizer()

    configfiles = next(walk('./config'), (None, None, []))[2]
    logPath = './logs/{}_{}'.format(datetime.now().strftime('%y%m%d%H%M%S'), sourcefile.rsplit('/', 1)[1])
    mkdir(logPath)

    tools = []
    for filename in configfiles:
        try:
            tool = Tool(filename, logPath)
        except:
            pass
        else:
            tools.append(tool)

    synth.loadTools(tools)
    synth.renderRun()

    # processes = [mp.Process(target=worker, args=(obj, sourcefile)) for obj in tools]
    # for p in processes:
    #     p.start()
    # for p in processes:
    #     p.join()

    # resultList  = [output.get() for p in processes]

    resultList = []
    for tool in tools:
        resultList.append(tool.run(sourcefile))

    synth.renderResult(resultList)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar='PATH', type=str, help='path to the solidity code')
    
    args = parser.parse_args()
    faustian(args.path)
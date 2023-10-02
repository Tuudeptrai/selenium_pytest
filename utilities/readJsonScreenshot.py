

class ReadJsonScreenshot:
    @staticmethod
    def geinputData():
        f = open("../testCases/screenshot.json", "r")
        return eval(f.read())
    @staticmethod
    def writetoafile(json):
        with open("../testCases/screenshot.json", 'w') as fp:
            fp.write(str(json))
  



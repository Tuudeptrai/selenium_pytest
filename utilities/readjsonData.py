

class ReadJson:
    @staticmethod
    def geinputData():
        f = open("../testCases/datatoken.json", "r")
        return eval(f.read())
    @staticmethod
    def writetoafile(json):
        with open("../testCases/datatoken.json", 'w') as fp:
            fp.write(str(json))
  



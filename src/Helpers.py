class Helpers:
    def getById(self, objList, objId):
        for i in objList:
            if i['ID'] == objId:
                return i

    def getByDescription(self, objList, description):
        for d in objList:
            if d['DESCRIPTION'] == description:
                return d

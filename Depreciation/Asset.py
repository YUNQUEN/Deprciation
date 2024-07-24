#Asset object class by (PIKI)

class Asset:
    """Depreciation class"""

    def __init__(self, cost=0.0, salvage=0.0, life=0):
        self.setCost(cost)
        self.setSalvage(salvage)
        self.setLife(life)
        self.checkValidity()
        if self.isValid():
            self.buildAsset()

    def setCost(self, c):
        self._cost = c  #pseudo-private instance variable

    def getCost(self):
        return self._cost

    def setSalvage(self, s):
        self._salvage = s

    def getSalvage(self):
        return self._salvage

    def setLife(self, l):
        self._life = l

    def getLife(self):
        return self._life

    def checkValidity(self):
        self._errmsg = ""
        self._valid = True
        if self._cost <= 0:
            self._errmsg += "Cost must be > 0"
            self._Valid = False
        if self._salvage < 0:
            self._errmsg += " Salvage cannot be negative."
            self._Valid = False
        if self._salvage >= self._cost:
            self._errmsg += " Salvage must be less than cost."
            self._valid = False
        if self._life <= 0:
            self._errmsg += "Life must be positive."
            self._valid = False

    def buildAsset(self):
        self._built = False
        try:
            #annual straigh line depreciation...
            self._anndepsl = (self._cost - self._salvage) / self._life
            ddlrate = 1.0 / self._life * 2.0

            self._built = True
        except Exception as e:
            self._errmsg = "Asset build error: " + str(e)
            self._built = False

    def getErrorMsg(self):
        return self._errmsg

    def isValid(self):
        return self._valid

    def getAnnDep(self, yr=None):
        if yr == None:
            return self._anndepsl

        return -1
    def getBegBalSL(self, yr):
        if self.dataOK(yr):
            return self._cost - (self._anndepsl * (yr -1 ))
        return -1
    def getEndBalSL(self, yr):
        if self.dataOK(yr):
            return self._cost - (self._anndepsl * yr)
    def dataOK(self, yr):
        ok = self._built
        if not ok:
            self.buildAsset()
            ok = self._built
        if ok and (yr < 1 or yr > self._life):
            ok = False
        return ok


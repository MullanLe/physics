import units as un


class IdealGas:

    def __init__(self, moles=None, pres=None, temp=None, vol=None):
        self._moles = moles
        self._pres = pres
        self._temp = temp
        self._R = IdealGas.R
        self._vol = vol

    @property
    def moles(self):
        if self._moles == None:
            moles = (self.pres*self.vol)/(self.R*self.temp)
            return moles
        else: 
            return self._moles

    @moles.setter
    def moles(self, new_moles):
        self._moles = new_moles

    @property
    def pres(self):
        if self._pres == None:
            pres = (self.R*self.moles*self.temp) / self.vol
            return pres
        else:
            return self._pres

    @pres.setter
    def pres(self, new_pres):            
        self._pres = new_pres

    @property
    def temp(self):
        if self._temp == None:
            temp = (self.R*self.moles*self.pres) / self.vol
            return temp
        else:
            return self._temp

    @temp.setter
    def temp(self, new_temp):
        self._temp = new_temp

    @property
    def R(self):
        return un.MolarConstant('J/molK').SImagnitude

    @property
    def vol(self):
        if self._vol == None:
            _R = self.R if not self.R == type(un.Unit) else self.R.magnitude
            _pres = self.pres if not isinstance(self.pres, un.Pres) else self.pres.magnitude
            _temp =  self.temp if not self.temp == type(un.Unit) else self.temp.magnitude
            volume = (_R*self.moles*_pres) / _temp
            return volume
        else:
            return self._vol
        
    @vol.setter
    def vol(self, new_vol):
        self._vol = new_vol
        

inletpres = un.Pres(10, 'psi')
inlet = IdealGas(pres=inletpres, temp=50, moles=1)
print(inlet.moles, inlet.R, inlet.vol, inlet.temp, inlet.pres)
inlet.pres = 20
print(inlet.moles, inlet.R, inlet.vol, inlet.temp, inlet.pres)
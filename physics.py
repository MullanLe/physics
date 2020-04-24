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
        return self._moles

    @moles.setter
    def moles(self, new_moles):
        self._moles = new_moles

    @property
    def pres(self):
        return self._pres

    @pres.setter
    def pres(self, new_pres):
        self._pres = new_pres

    @property
    def temp(self):
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
            _moles = self.moles
            _pres = self.pres
            _temp = self.temp.magnitude
            _R = self.R
            volume = (_R*_moles*_pres) / _temp
            return volume
        else:
            return self._vol
        
    @vol.setter
    def vol(self, new_vol):
        self._vol = new_vol
        

inlettemp = un.Temp(50, 'C')

inlet = IdealGas(moles=1, pres=10, temp=inlettemp)
print(inlet.vol)

inlettemp = 40
print(inlet.vol)
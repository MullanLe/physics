import units as un


class IdealGas:

    def __init__(self, moles=None, pres=None, temp=None, vol=None):
        self._moles = moles
        self._pres = pres
        self._temp = temp
        self._R = IdealGas.R
        self._vol = vol
        self.Rcalc = self.R if not isinstance(self.R, un.Unit) else self.R.magnitude
        self.Pcalc = self.pres if not isinstance(self.pres, un.Pres) else self.pres.magnitude
        self.Tcalc =  self.temp if not isinstance(self.temp, un.Temp) else self.temp.magnitude
        self.Mcalc = self.moles if not isinstance(self.moles, Moles) else self.moles.moles
        self.Vcalc = self.vol if not isinstance(self.vol, un.Vol) else self.vol.magnitude


    @property
    def moles(self):
        if self._moles == None:
            moles = (self.Pcalc*self.Vcalc)/(self.Rcalc*self.Tcalc)
            return Moles(moles)
        else: 
            return self._moles

    @moles.setter
    def moles(self, new_moles):
        self._moles = new_moles

    @property
    def pres(self):
        if self._pres == None:
            pressure = (self.Rcalc * self.Mcalc * self.Tcalc) / self.Vcalc
            return un.Pres(pressure, 'Pa')
        else:
            return self._pres

    @pres.setter
    def pres(self, new_pres):            
        self._pres = new_pres

    @property
    def temp(self):
        if self._temp == None:
            temp = (self.Rcalc*self.Mcalc*self.Pcalc) / self.Vcalc
            return un.Temp(temp, 'K')
        else:
            return self._temp

    @temp.setter
    def temp(self, new_temp):
        self._temp = new_temp

    @property
    def R(self):
        return un.MolarConstant('J/molK')

    @property
    def vol(self):
        if self._vol == None:
            volume = (self.Rcalc*self.Mcalc*self.Pcalc) / self.Tcalc
            return un.Vol(volume, 'm3')
        else:
            return self._vol
        
    @vol.setter
    def vol(self, new_vol):
        self._vol = new_vol
        
    def show(self):
        txt = f"""\n presure = {self.pres.magnitude} {self.pres.unit}""" \
            + f"""\n temperature = {self.temp.magnitude} {self.temp.unit}""" \
            + f"""\n volume = {self.vol.magnitude} {self.vol.unit}""" \
            + f"""\n moles = {self.moles.moles}""" \
            + f"""\n R = {self.R.magnitude} {self.R.unit}"""
        return txt


class Moles():

    def __init__(self, moles=None, gas_mass=None, molar_mass=None):
        self._moles = moles
        self._gas_mass = gas_mass
        self._molar_mass = molar_mass

    @property
    def moles(self):
        if self.gas_mass == None or self.molar_mass == None:
            return self._moles
        else:
            return self.gas_mass / self.molar_mass

    @moles.setter
    def moles(self, new_moles):            
        self._moles = new_moles
        self.gas_mass = None
        self.molar_mass = None

    @property
    def gas_mass(self):
        return self._gas_mass

    @gas_mass.setter
    def gas_mass(self, new_mass):
        self._gas_mass = new_mass

    @property
    def molar_mass(self):
        return self._molar_mass

    @molar_mass.setter
    def molar_mass(self, new_mass):
        self._molar_mass = new_mass

    def show(self):
        txt = f"""\n moles = {self.moles}"""
        return txt


if __name__ == "__main__":
    
    gasp = un.Pres(14.4, 'psi')
    gast = un.Temp(40, 'C')
    gasv = un.Vol(100, 'L')
    gasm = Moles(gas_mass=1, molar_mass=18.15)

    gas = IdealGas(moles=gasm, pres=gasp, temp=gast)
    print(gas.show())
    
    gasB = IdealGas(moles=gasm, vol=gasv, temp=gast)
    print(gasB.show())

    #gas = IdealGas(pres=gasp, vol=gasv, temp=gast)
    #print(gas.show())

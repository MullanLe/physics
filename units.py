class Unit:

    def __init__(self, magnitude, unit):
        self._magnitude = magnitude
        self._unit = unit
        self.factors = dict(zip(self.units, self.conversions))
        self.SIunit = self.units[0]
        self._SImagn = Unit.convert(self.magnitude, self.unit, self.SIunit, self.factors)

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, new_unit):
        if new_unit == self.unit:
            pass
        elif new_unit in self.factors:
            self.magnitude = Unit.convert(self.magnitude, self.unit, new_unit, self.factors)
            self._unit = new_unit       

    @property
    def magnitude(self):
        return self._magnitude

    @magnitude.setter
    def magnitude(self, new_magnitude):
        if new_magnitude == self.magnitude:
            pass
        else:
            self._magnitude = new_magnitude

    def convert(magn, unit, new_unit, factors):
        SI = magn / factors[unit]
        _current=factors[unit]
        _convert=factors[new_unit]
        _converted = SI * _convert
        return _converted


class Len(Unit):

    def __init__(self, magnitude, unit):
        self.units = ['mm', 'cm', 'm', 'in', 'ft']
        self.conversions = [1, 0.1, 0.001, 0.03937, 0.00328]
        super().__init__(magnitude, unit)


class Area(Unit):

    def __init__(self, magnitude, unit):
        self.units = ['mm2', 'cm2', 'm2', 'in2', 'ft2']
        self.conversions = [1, 0.01, 1E-6, 1.55E-3, 1.07639E-5]
        super().__init__(magnitude, unit)


class Vol(Unit):

    def __init__(self, magnitude, unit):
        self.units = ['mm3', 'cm3', 'm3', 'L', 'in3', 'ft3']
        self.conversions = [1, 0.001, 1E-9, 1E-6, 6.1024E-5, 3.5315E-8]
        super().__init__(magnitude, unit)


class Pres(Unit):

    def __init__(self, magnitude, unit):
        self.units = ['Pa', 'kPa', 'mPa', 'atm', 'bar','psi','mbar','kg/cm2']
        self.conversions = [1,1E-3,0.1,9.8692E-6,1E-5,1.45038E-4,0.01,1.019716E-5]
        super().__init__(magnitude, unit)


class Temp(Unit):

    def __init__(self, magnitude, unit):
        self.units=['K', 'C', 'F', 'R']
        self.SIunit = self.units[0]
        self._unit = unit
        self._magnitude = magnitude
        self.SImagnitude = Temp.kelvins(self)

    @Unit.unit.setter
    def unit(self, new_unit):
        if new_unit == self.unit:
            pass
        elif new_unit in self.units:
            self._unit = new_unit
            self._magnitude = Temp.convert(self, self.SImagnitude, new_unit)

    @Unit.magnitude.setter
    def magnitude(self, new_magnitude):
        if new_magnitude == self.magnitude:
            pass
        else:
            self._magnitude = new_magnitude

    def kelvins(self):
        if self.unit=='K':
            _base = self.magnitude
        elif self.unit=='C':
            _base = self.magnitude+273.15
        elif self.unit=='F':
            _base = ((self.magnitude - 32.0)*5.0/9.0)+273.15
        elif self.unit=='R':
            _base = self.magnitude*5.0/9.0
        return _base

    def convert(self, base, new_unit):
        if new_unit=='K':
            _magnitude = base
        elif new_unit=='C':
            _magnitude=base-273.15
        elif new_unit=='F':
            _magnitude = ((base-273.15) * 9.0 / 5.0) + 32.0
        elif new_unit=='R':
            _F = ((base-273.15)* 9.0 / 5.0) + 32.0
            _magnitude = _F + 459.67
        return _magnitude


class VolFlow(Unit):

    def __init__(self, magnitude, unit):
        self.units = ['m3/s', 'm3/h', 'cfm', 'gpm US', 'gpm I','L/s','L/min']
        self.conversions = [1,3600,2118.88,13198.15,15850.32,1000,60000]
        super().__init__(magnitude, unit)


class MassFlow(Unit):

    def __init__(self, magnitude, unit):
        self.units = ['kg/s', 'kg/h', 'lb/min']
        self.conversions = [1,3600,132.277357]
        super().__init__(magnitude, unit)


class MolarVol(Unit):

    def __init__(self, magnitude, unit):
        self.units = ['m3/mol', 'L/mol', 'ft3/lbmol']
        self.conversions = [1,0.001,16018.463]
        super().__init__(magnitude, unit)


class MolarConstant(Unit):

    def __init__(self, unit):
        self.units = ['J/molK', 'ft.lbf/lb mol']
        self.conversions = [8.314, 1545.35]
        self.factors = dict(zip(self.units, self.conversions))
        self._unit = unit
        self._magnitude = self.factors[unit]
        self.SImagnitude = self.conversions[0]

        @Unit.unit.setter
        def unit(self, new_unit):
            if new_unit == self.unit:
                pass
            elif new_unit in self.factors:
                self.magnitude = self.factors[new_unit]
                self._unit = new_unit


if __name__ == "__main__":
    pass
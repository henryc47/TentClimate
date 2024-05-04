#personal parameters
person_exhale_co2 = 40 #g/hr
person_exhale_water = 40 #g/hr
person_heat = 80#W = J/hr
#physical parameters
R = 8.314 #gas constant, J/mol*k
co2_molar_mass = 44 #g/mol
water_molar_mass = 18 #g/mol
air_molar_mass = 29 #combined total, 80% O2 and 20% N2
#world parameters
air_pressure = 100000 #pa
co2_concentration = 425 #ppm

class Tent:
    def __init__(self,floor_area,roof_area,volume,ach):
        self.floor_area = floor_area #m^2
        self.roof_area = roof_area #m^2
        self.volume = volume #m^3
        self.ach = ach #air changes per hour

    #add people to the tent
    def add_people(self,number):
        self.tent_heat = number*person_heat #W
        self.tent_exhale_water = number*person_exhale_water #g/hour
        self.tent_exhale_co2 = number*person_exhale_co2 #g/hour
    
    #get co2 equilibrium co2 levels inside the tent, note tent_air_temp is in K
    def get_co2_concentration(self,tent_air_temp : float) -> float:
        mols_co2_per_hour = self.tent_exhale_co2/co2_molar_mass #how many mols of co2 produced per hour
        ach_total = self.volume*self.ach #m^3 of air changed per hour
        mols_air_per_m3 = (air_pressure)/(tent_air_temp*R) #mols of air per cubic meter
        ach_mols = ach_total*mols_air_per_m3 #mols of air per cubic meter
        delta_co2 = (mols_co2_per_hour/ach_mols)*1000000 #rise in co2 inside tent, ppm
        return (delta_co2 + co2_concentration)




        
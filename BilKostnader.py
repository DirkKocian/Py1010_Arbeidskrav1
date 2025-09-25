
"""
Årlige kostnader ved elbil sammenlignet med bensinbil
Created on Wed Sep 24 19:55:08 2025
Dirk Kocian (dikoc@usn.no)

"""
"Input"
Km = 30000 # [km kjørt]
Fors_El = 5000 # forsikring elbil
Fors_Ben = 7500 # forsikring bensinbil
Trafikk_Fors = 8.38 * 365 # trafikkforsikringsavgift får både el- og besinbil for et år
PrisKM_El = 0.4 # [0.2 kWh/km * 2.0kr/kWh = 0.4kr/Km]
PrisKM_Ben = 1.0 # [kr/Km]
Bom_El = 0.1 # [kr/km] 
Bom_Ben = 0.3 # [kr/km] 

"beregning"
Kost_El = Fors_El + Trafikk_Fors + (PrisKM_El * Km) + (Bom_El * Km)
Kost_Ben = Fors_Ben + Trafikk_Fors + (PrisKM_Ben * Km) + (Bom_Ben * Km)
Kost_Diff = abs(Kost_El - Kost_Ben)

"utskrift"
print("Årlige kostnader for elbil =", Kost_El)
print("Årlige kostnader for bensinbil =", Kost_Ben)
print("Kostnadsdifferansen er =", Kost_Diff)
from pHcalc import Acid

from pH_helpers import generate_sillen, generate_Verteilung

# sample acids/bases
Heptylamine = Acid(pKa=[10.67], charge=1, conc=1e-6)
Carbonic_acid = Acid(pKa=[6.35, 10.33], charge=0, conc=0.1)
Hydrochloric_acid = Acid(pKa=[-1], charge=0, conc=0.1)
Natriumhydrogensulfat = Acid(pKa=[1.99], charge=-1, conc=0.1)
Natriumfluorid = Acid(pKa=[3.17], charge=0, conc=5e-2)
Salpetersäure = Acid(pKa=[-1, 37], charge=0, conc=1e-7)
Essigsäure = Acid(pKa=[4.7], charge=0, conc=0.01)
Spartein = Acid(pKa=[9.46, 2.24], charge=2, conc=0.01)
H2Sp2Plus = Acid(pKa=[2.24], charge=0, conc=0.05)


# Structure of the functions:
# generate_sillen([acids], [names], [acids_names], pHbar, labels)
# generate_Verteilung(acids, [names], [acids_names])


def main():
    generate_sillen([Spartein], ["H2Sp2+", "HSp+", "Sp"], ["Spartein"], True, True)
    generate_Verteilung(Spartein, ["H2Sp2+", "HSp+", "Sp"], ["Spartein"])


if __name__ == "__main__":
    main()

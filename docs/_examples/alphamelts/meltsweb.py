from pyrolite.ext.alphamelts.web import *


def default_datadict():
    d = {}
    d["title"] = ("TestREST",)
    d["initialize"] = {
        "SiO2": 48.68,
        "TiO2": 1.01,
        "Al2O3": 17.64,
        "Fe2O3": 0.89,
        "Cr2O3": 0.0425,
        "FeO": 7.59,
        "MnO": 0.0,
        "MgO": 9.10,
        "NiO": 0.0,
        "CoO": 0.0,
        "CaO": 12.45,
        "Na2O": 2.65,
        "K2O": 0.03,
        "P2O5": 0.08,
        "H2O": 0.20,
    }
    d["calculationMode"] = "findLiquidus"
    d["constraints"] = {"setTP": {"initialT": 1200, "initialP": 1000}}
    return d


D = default_datadict()
# %% Oxides
melts_oxides(D)
# %% Phases
melts_phases(D)
# %% Compute
melts_compute(D)
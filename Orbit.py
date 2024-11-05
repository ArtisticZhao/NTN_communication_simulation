from skyfield.api import Loader, EarthSatellite
from skyfield.timelib import Time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from utils import utc_str_to_utc_time

class Orbit:
    def __init__(self, tle_context: str, start_utc: str, elapsed_hours: float, step_sec: float) -> None:
        L0, L1, L2 = tle_context.splitlines()
        self.sat = EarthSatellite(L1, L2)
        self.name = L0
        self.load = Loader('./')
        self.data = self.load('de421.bsp')
        self.ts   = self.load.timescale()
        utc = utc_str_to_utc_time(start_utc)
        hours = np.arange(0, elapsed_hours, step_sec/3600)
        print(hours.shape)
        self.time = self.ts.utc(utc.year, utc.month, utc.day, utc.hour + hours, utc.minute, utc.second)

    def get_orbit(self):
        Rpos = self.sat.at(self.time).position.km
        Rposecl = self.sat.at(self.time).ecliptic_position().km
        return Rpos, Rposecl


if __name__ == "__main__":
    from cfg import *
    o = Orbit(TLE, simulation_start_time_UTC, simulation_elapse_hours, simulation_step_seconds)
    Rpos, Rposecl = o.get_orbit()
    print(Rpos.shape)

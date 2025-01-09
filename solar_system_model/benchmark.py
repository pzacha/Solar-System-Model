import random
import numpy as np
from solar_system_model.simulation import SolarSystemSimulation
import time

from solar_system_model.models import SpaceObject


def simulation_step(sim: SolarSystemSimulation):
    planets_x = np.zeros(len(sim.celestials) - 1, dtype=float)
    planets_y = np.zeros(len(sim.celestials) - 1, dtype=float)
    sun_x = [0]
    sun_y = [0]

    for _ in range(365 * 24):
        sim.simulate_step()
        sim.update_animation_data(planets_x, planets_y, sun_x, sun_y)


def add_random_planets(sim: SolarSystemSimulation, num_of_planets: int):
    def _random_position():
        """
        Returns a random position within the window.
        """
        return random.choice([1, -1]) * random.uniform(1, 10) * 10 ** random.randint(2, 12)

    def _random_velocity():
        """
        Returns a random velocity.
        """

        return random.choice([1, -1]) * random.uniform(1, 10) * 10 ** random.randint(2, 5)

    SolarSystemSimulation.celestials = {"Sun": sim.sun}
    for num in range(num_of_planets - 1):
        SolarSystemSimulation.celestials[str(num)] = SpaceObject(
            mass=(10**16) * random.uniform(1, 10) * 10 ** random.randint(1, 5),
            position=[_random_position(), _random_position()],
            velocity=[_random_velocity(), _random_velocity()],
        )


sim = SolarSystemSimulation(3600)
add_random_planets(sim, 4)

start_time = time.time()
simulation_step(sim)
end_time = time.time()

print(f"Simulation took {end_time - start_time} seconds")

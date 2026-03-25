import numpy as np
import random

from utils.track_utils import compute_curvature, compute_slope
from agents.kart_agent import KartAgent


class Agent6(KartAgent):
    def __init__(self, env, path_lookahead=3):
        super().__init__(env)
        self.path_lookahead = path_lookahead
        self.agent_positions = []
        self.obs = None
        self.isEnd = False
        self.name = "mantani-leon" # team7 s'appelle mantani-leon
        self.pas = 0
        self.marchearriere = False

    def reset(self):
        self.obs, _ = self.env.reset()
        self.agent_positions = []

    def endOfTrack(self):
        return self.isEnd

    def choose_action(self, obs):
        acceleration = random.random()
        steering = random.random()
        if self.pas <=200:
            action = {
                "acceleration": 0.0,
                "steer": 0.0,
                "brake": self.marchearriere,
                "drift": False,
                "nitro": False,
                "rescue": False,
                "fire": False,
            }
            return action
        else:
            action = {
                    "acceleration": 1.0,
                    "steer": 0.0,
                    "brake": False,
                    "drift": False,
                    "nitro": False,
                    "rescue": False,
                    "fire": False,
                }
            return action
import numpy as np

class DieNSolver:

    def __init__(self):
        pass

    def find_optimal_policy(self, bad_side_vector):
        self._calculate_states(bad_side_vector)

    def _calculate_states(self, bad_side_vector):
        self._load_good_index(bad_side_vector)
        self._initialize_states(bad_side_vector)
        self._initialize_rewards()
        # self._build_state_and_rewards()

    def _load_good_index(self, bad_side_vector):
        self.good_indicies = []
        for i, isBad in enumerate(bad_side_vector):
            if not isBad:
                self.good_indicies.append(i + 1)

    def _initialize_states(self, bad_side_vector):
        self.N = len(bad_side_vector)
        self.max_states_n = 3 * N + 2
        self.T = np.zeros((2, self.max_states_n, self.max_states_n))
        
        self.T_roll = np.zeros((self.max_states_n, self.max_states_n))
        self.T_quit = np.zeros((self.max_states_n, self.max_states_n))

    def _initialize_rewards(self):
        self.R = np.zeros((2, self.max_states_n, self.max_states_n))
    
        self.R_roll = np.zeros((self.max_states_n, self.max_states_n))
        self.R_quit = np.zeros((self.max_states_n, self.max_states_n))


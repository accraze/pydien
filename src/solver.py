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
        self._build_arrays()

    def _load_good_index(self, bad_side_vector):
        self.good_indicies = []
        for i, isBad in enumerate(bad_side_vector):
            if not isBad:
                self.good_indicies.append(i + 1)

    def _initialize_states(self, bad_side_vector):
        self.N = len(bad_side_vector)
        self.max_states_n = 3 * self.N + 2
        self.T = np.zeros((2, self.max_states_n, self.max_states_n))
        
        self.T_roll = np.zeros((self.max_states_n, self.max_states_n))
        self.T_quit = np.zeros((self.max_states_n, self.max_states_n))

    def _initialize_rewards(self):
        self.R = np.zeros((2, self.max_states_n, self.max_states_n))
    
        self.R_roll = np.zeros((self.max_states_n, self.max_states_n))
        self.R_quit = np.zeros((self.max_states_n, self.max_states_n))

    def _build_arrays(self):
        """Build state and reward arrays."""
        possible_rows = [0] + self.good_indicies
        
        for row in range(0, self.max_states_n):
            # row vector
            self.T_roll_row = np.zeros(self.max_states_n)
            self.R_roll_row = np.zeros(self.max_states_n)
            
            if row in possible_rows:
                terminal_p = 1
                for idx in self.good_indicies:
                    col = idx + row
                    if col < self.max_states_n - 1:
                        self.T_roll_row[col] = 1 / self.N
                        terminal_p = terminal_p - (1 / self.N)
                        
                        self.R_roll_row[col] = idx
                        
                        if col not in possible_rows:
                            possible_rows.append(col)
                self.T_roll_row[self.max_states_n - 1] = terminal_p
                self.R_roll_row[self.max_states_n - 1] = -row
            else:
                self.T_roll_row[self.max_states_n - 1] = 1.0
            
            self.T_roll[row] = self.T_roll_row
            self.R_roll[row] = self.R_roll_row
            
            self.T_quit_row = np.zeros(self.max_states_n)
            self.T_quit_row[self.max_states_n - 1] = 1.0
            self.T_quit[row] = self.T_quit_row


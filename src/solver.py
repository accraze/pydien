import numpy as np

class DieN:

    def __init__(self):
        pass

    def find_optimal_policy(self):
        self._calculate_states()

    def _calculate_states(self, num, bad_side_vector):
        self.N = num
        run = 3
        self.States = run*N+2  # from 0 to 2N, plus quit
        self.isBadSide = np.array(list(bad_side_vector))
        self.isGoodSide = ~isBadSide+2  # [ 0, 0, 0, 1, 1, 1]
        self.Die = np.arange(1, N+1)        # [1, 2, 3, 4, 5, 6]
        self.dollar = Die * isGoodSide  # [0, 0, 0, 4, 5, 6]

    def _create_probability_list(self):
        self.prob = np.zeros((2, self.States, self.States))
        # if leave
        np.fill_diagonal(prob[0], 1)
        # if roll
        # Calculate probability for Input:
        p = 1.0/self.N

        # Create pro_1
        # Create 1 X (1+run*N+2) array
        # Don't change it! It must have size= run-1)*N+1
        zero = np.array([0]).repeat((self.run-1)*self.N+2)
        isGoodSide_2 = np.concatenate(
            (np.array([0]), self.isGoodSide, zero), axis=0)  # rbind
        # Create 1 X (run*N+3)*3 array
        isGoodSide_N = np.concatenate((isGoodSide_2, isGoodSide_2), axis=0)
        # Create 1 X ((run*N+3)^2 array
        for i in range(0, run*N+2):
            isGoodSide_N = np.concatenate((isGoodSide_N, isGoodSide_2), axis=0)
            i = i + 1
        # Create 1 X (2N+2)^2 array by trancation
        isGoodSide_N = isGoodSide_N[:(self.States**2)]

        isGoodSide_N = isGoodSide_N.reshape(
            self.States, self.States)  # Reshaping (rows first)
        self.prob[1] = np.triu(isGoodSide_N)  # upper triangle matirx
        self.prob[1] = self.prob[1]*p
        # last column
        prob_quit = 1 - \
            np.sum(self.prob[1, :self.States, :self.States-1], axis=1).reshape(-1, 1)

        self.prob[1] = np.concatenate(
            (self.prob[1, :self.States, :self.States-1], prob_quit), axis=1)  # cbind

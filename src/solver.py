class DieN:

    def __init__(self):
        pass

    def find_optimal_policy(self):
        self._calculate_states()

    def _calculate_states(self, num, bad_side_vector):
        N = num
        run = 3
        self.States = run*N+2  # from 0 to 2N, plus quit
        self.isBadSide = np.array(list(bad_side_vector))
        self.isGoodSide = ~isBadSide+2  # [ 0, 0, 0, 1, 1, 1]
        self.Die = np.arange(1, N+1)        # [1, 2, 3, 4, 5, 6]
        self.dollar = Die * isGoodSide  # [0, 0, 0, 4, 5, 6]


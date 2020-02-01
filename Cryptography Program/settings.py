class Settings():
    """A class to store all settings for Cryptography."""
    
    def __init__(self):
        """Initialize the static settings."""
        # Characters
        self.space = [32]
        self.capital_letters = list(range(65, 91))
        self.full_stop = [46]
        self.question_mark = [63]
        
        # Matrix
        self.A = [
                [1, -1],
                [1, 0],
                ]
        self.det_A = self.A[0][0] * self.A[1][1] - self.A[0][1] * self.A[1][0]
        self.A_inverse()
        
    def A_inverse(self):
        """Taking Inverse of Matrix A."""
        adj_A = [
                [self.A[1][1], self.A[0][1] * -1],
                [self.A[1][0] * -1, self.A[0][0]]
                ]
        
        A_inverse = [[0, 0], [0, 0]]
        
        if self.det_A != 0:
            for i in range(len(adj_A)):
                for j in range(len(adj_A)):
                    A_inverse[i][j] += adj_A[i][j] // self.det_A
        
        return A_inverse

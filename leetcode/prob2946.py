class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        r = len(mat)
        c = len(mat[0])
        for row in range(0, r):
            for col in range(0, c):
                if row % 2 == 0:
                    moved = (col - k) % c
                    if mat[row][moved] != mat[row][col]:
                        return False
                    
                else:
                    moved = (col + k) % c
                    if mat[row][moved] != mat[row][col]:
                        return False
                    
        return True

from base import Base
import misc
import copy


class Matrix:
    def __init__(self, matrix):
        self.size = len(matrix)
        self.matrix = matrix
    
    def __getitem__(self, key):
        return self.matrix[key]
    
    def __mul__(self, m):
        if isinstance(m, Matrix):
            if len(self.matrix[0]) != m.size:
                raise TypeError
            nrow = self.size
            ncol = len(m[0])
            M = [[0 for i in range(ncol)] for j in range(nrow)]
            for j in range(nrow):
                for i in range(ncol):
                    for index in range(len(self.matrix[0])):
                        M[j][i] += self.matrix[j][index] * m[index][i]
            return Matrix(M)
        elif isinstance(m, Base):
            result = self.__mul__(Matrix([[m.x],
                                        [m.y],
                                        [m.z],
                                        [m.w]]))
            return result.to_type('base')
    
    def to_type(self, output='base'):
        for row in self.matrix:
            if len(row) != 1:
                raise TypeError
        return Base(self.matrix[0][0], self.matrix[1][0], self.matrix[2][0], self.matrix[3][0])
    
    def determinant(self):
        if self.size == 2:
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
        else:
            result = 0
            for j, row in enumerate(self.matrix):
                result += self.matrix[j][0] * self.cofactor(j, 0)
            return result
    
    def transpose(self):
        nrow = self.size
        ncol = len(self.matrix[0])
        M = [[0 for i in range(ncol)] for j in range(nrow)]
        for j in range(nrow):
            for i in range(ncol):
                M[i][j] = self.matrix[j][i]
        return Matrix(M)
    
    def submatrix(self, j, i):
        M = copy.deepcopy(self.matrix)
        for row in M:
            del row[i]
        del M[j]
        return Matrix(M)
    
    def minor(self, j, i):
        sub = self.submatrix(j, i)
        return sub.determinant()

    def cofactor(self, j, i):
        if (j + i)%2 == 1:
            factor = -1
        else:
            factor = 1
        return  factor * self.minor(j, i)

    def is_invertible(self):
        if self.determinant() == 0:
            return False
        else:
            return True
    
    def inverse(self):
        if not self.is_invertible():
            raise ValueError
        nrow = self.size
        ncol = len(self.matrix[0])
        det = self.determinant()
        co = Matrix([[0 for i in range(ncol)] for j in range(nrow)])
        for j in range(nrow):
            for i in range(ncol):
                co[j][i] = self.cofactor(j, i) / det
        co = co.transpose()
        return co 

            

def equals(A, B):
    assert A.size == B.size, "input array have different length {} and {}".foramt(len(A), len(B))
    for j in range(A.size):
        assert len(A[j]) == len(B[j]), "input array have different length {} and {}".foramt(len(A[j]), len(B[j]))
        for i in range(len(A[j])):
            equal = misc.equals(A[j][i], B[j][i])
            if not equal:
                return False
    return True
import math

class Vec2D:

    def __init__(self, x: float, y: float):

        self.x = x
        self.y = y

    def to_list(self) -> list:
        return [self.x, self.y]

    def __add__(self, vec):
        return Vec2D(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        _v = Vec2D(self.x - vec.x, self.y - vec.y)
        return _v

    def __eq__(self, vec):
        if isinstance(vec, Vec2D):
            return self.x == vec.x and self.y == vec.y
        return False

    def __mul__(self, alpha):
        """ alpha is a scalar number """
        return Vec2D(alpha*self.x, alpha*self.y)

    def __rmul__(self, alpha):
        return self.__mul__(alpha)

    def __truediv__(self, alpha):
        return Vec2D(self.x/alpha, self.y/alpha)

    def __div__(self, alpha):
        return Vec2D(self.x/alpha, self.y/alpha)

    def __repr__(self):
        return "Vec2(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return self.norm()

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __getitem__(self, index):
        if index == 0:
            return self.x 
        elif index == 1:
            return self.y
        
        raise IndexError

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value 
        elif index == 1:
            self.y = value
        else:        
            raise IndexError
    
    @classmethod
    def left(cls):
        return cls(-1, 0)

    @classmethod
    def right(cls):
        return cls(1, 0)

    @classmethod
    def up(cls):
        return cls(0, 1)

    @classmethod
    def left(cls):
        return cls(0, -1)

    def norm(self):

        return math.sqrt(self.x**2 + self.y**2)

class Mat2D:

    def __init__(self, u: Vec2D, v: Vec2D):

        self.u = u
        self.v = v

    @classmethod
    def identy(cls):

        return cls(Vec2D(1, 0), Vec2D(0, 1))

    def __repr__(self) -> str:

        str_rep = "Mat2D (\n"
        str_rep += f"  [{self.u[0]}\t{self.v[0]}]\n"
        str_rep += f"  [{self.u[1]}\t{self.v[1]}]\n"
        str_rep += ")" 

        return str_rep
    
    def __getitem__(self, indexes):

        assert isinstance(indexes, tuple)

        i, j = indexes

        assert j >= 0 and j < 2
        assert i >= 0 and i < 2

        column = self.u if j == 0 else self.v

        return column[i]

    def __setitem__(self, indexes, value):

        assert isinstance(indexes, tuple)

        i, j = indexes

        assert j >= 0 and j < 2
        assert i >= 0 and i < 2

        column = self.u if j == 0 else self.v

        column[i] = value

    def __mul__(self, alpha):

        return Mat2D(alpha*self.u, alpha*self.v)

    def __rmul__(self, alpha):

        return self.__mul__(alpha)

    def __neg__(self):

        return self.__mul__(-1)

    def transform(self, vec: Vec2D) -> Vec2D:

        return vec[0] * self.u + vec[1] * self.v

    def det(self) -> float:

        return self.u[0]*self.v[1] - self.u[1] * self.v[0]

    def invert(self):
        
        det = self.det()

        assert det != 0 

        new_u = Vec2D(self.v[1], -self.u[1])
        new_v = Vec2D(-self.v[0], self.u[0])

        return (1/det) * Mat2D(new_u, new_v)

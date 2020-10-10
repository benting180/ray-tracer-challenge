from base import Base


class Point(Base):
    def __init__(self, x, y, z):
        super(self.__class__, self).__init__(x, y, z, 1)
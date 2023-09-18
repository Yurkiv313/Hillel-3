class Parameters:

    def __init__(self, index, height, weight):
        self.index = index
        self.height = float(height)
        self.weight = float(weight)

    def __str__(self):
        return f'{self.index} {self.height} {self.weight}'


if __name__ == '__main__':
    pass

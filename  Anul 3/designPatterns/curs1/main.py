class LegoBrick:
    def __init__(self, columns, rows, scaling_factor):
        self.columns = columns
        self.rows = rows
        self.scaling_factor = scaling_factor

    def scale(self):
        return self.scaling_factor * self.columns, self.scaling_factor * self.rows


class ClassicLegoBrick(LegoBrick):
    def __init__(self, columns, rows):
        super().__init__(columns, rows, 1)


class DuploLegoBrick(LegoBrick):
    def __init__(self, columns, rows):
        super().__init__(columns, rows, 4)


class LegoBrickFactory:
    @staticmethod
    def create_lego_brick(columns, rows, brick_type):
        if brick_type == "classic":
            return ClassicLegoBrick(columns, rows)
        elif brick_type == "duplo":
            return DuploLegoBrick(columns, rows)
        else:
            raise ValueError("Invalid brick type")


if __name__ == "__main__":
    brick_type = input("Enter the type of Lego brick (classic or duplo): ")
    columns = int(input("Enter the number of columns: "))
    rows = int(input("Enter the number of rows: "))

    brick = LegoBrickFactory.create_lego_brick(columns, rows, brick_type)
    scaled_columns, scaled_rows = brick.scale()

    print(f"Size: {scaled_columns}x{scaled_rows} inches")

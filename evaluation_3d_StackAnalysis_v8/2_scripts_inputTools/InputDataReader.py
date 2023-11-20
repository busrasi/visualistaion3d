import pandas as pd

class InputDataReader:
    def __init__(self, path, custom_color=None):
        self.path = path
        self.custom_color = custom_color
        self.data = []

    def read_and_process(self):
        with open(self.path, 'r') as pcd_file:
            lines = pcd_file.readlines()

        for line in lines:
            values = line.split()
            if len(values) == 3 or len(values) == 12:
                if len(values) == 3:
                    values.extend(['0', '0', '0', '1', '0', '0', '0', '0', '0'])
                if not values[6].replace('.', '', 1).isdigit():
                    continue  # Skip rows with non-numeric "rgb" values
                if self.custom_color is not None:
                    # Set a custom color if specified
                    values[6] = self.custom_color
                self.data.append([float(value) for value in values])

        columns = ["x", "y", "z", "normal_x", "normal_y", "normal_z", "rgb", "curvature", "referenceColorDistance", \
                   "label", "reserved", "allBitFields"]
        df = pd.DataFrame(self.data, columns=columns)

        return df
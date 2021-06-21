import re
import logging
from logger import logger


class Parser:

    def __init__(self, input_string: str):
        self.input_params = input_string

    def parse_field_size(self):
        size_of_fields = re.findall("(\d+)x(\d+)", self.input_params)

        if len(size_of_fields) <= 0:
            raise IOError("Can not parse a size of the field, shoulde be like (5x5)")
        elif len(size_of_fields) > 1:
            raise IOError("Can not parse a size of the field, more then 1 size of the field, shoulde be like (5x5)")

        logger.info(f'Parsed field_size {size_of_fields}')

        return size_of_fields[0]

    @property
    def get_key_points(self):
        return self.key_points

    def parse_key_points(self):
        self.key_points = re.findall("\((\d+),(\d+)\)", self.input_params)

        if len(self.key_points) <= 0:
            raise IOError("Can not parse points, shoulde be like (1,5)")

        return self.key_points

    def convert_params_to_int(self):
        try:
            self.key_points = [[int(i) for i in element] for element in self.key_points]
            self.size_of_fields = [int(i) for i in self.size_of_fields]
        except Exception:
            logger.exception("Can not convert params to int")

    def check_key_points_pozitions(self):
        for point in self.key_points:
            x, y = point[0], point[1]
            if x < 0 or y < 0:
                raise ArithmeticError("Points must be greater then 0!")

            if x > self.size_of_fields[0] or y > self.size_of_fields[1]:
                raise ArithmeticError("Points must be less then fields size!")

        return True

    def parse_params(self):
        try:
            self.size_of_fields = self.parse_field_size()
            self.parse_key_points()
        except Exception as ex:
            logger.exception(ex)

        self.convert_params_to_int()
        self.check_key_points_pozitions()

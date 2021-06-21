import re
import logging
from logger import logger
class Parser:
    def __init__(self, input_string:str):
        self.input_params = input_string
        

    def parse_field_size(self):
        size_of_fields = re.findall("(\d+)x(\d+)",self.input_params)

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
        self.key_points = re.findall("\((\d+),(\d+)\)",self.input_params)

        if len(self.key_points) <= 0:
                raise IOError("Can not parse points, shoulde be like (1,5)")

        
    def convert_params_to_int(self):
        try:
             self.key_points = [ [int(i) for i in element] for element in self.key_points] 
             self.size_of_fields = [int(i) for i in self.size_of_fields]
        except Exception:
            logger.exception("Can not convert params to int")


    def parse_params(self):
        try:
            self.size_of_fields = self.parse_field_size()
            self.parse_key_points()
        except Exception as ex:
            logger.exception(ex)
        
        self.convert_params_to_int()

    



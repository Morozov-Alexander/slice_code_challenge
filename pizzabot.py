import sys
from logger import logger
from parser import Parser


def sort_function(point):
    return sum(point)

def path_building(delta_x,delta_y):
    path =''
    if delta_x > 0:
        path += 'E'* abs(delta_x)
    elif delta_x < 0:
        path += 'W'* abs(delta_x)
    if delta_y > 0:
        path += 'N'* abs(delta_y)
    elif delta_y < 0:
        path += 'S'* abs(delta_y)
    return path

def find_shortest_path(key_points:list):
    key_points = sorted(key_points,key=sort_function)
    my_point = [0,0]
    string_path=''

    for key_point in key_points:
        delta_x , delta_y = key_point[0] - my_point[0], key_point[1] - my_point[1]
        string_path += path_building(delta_x, delta_y) + 'D'
        my_point = key_point

    print(string_path)
    logger.info("The path was found - {}".format(string_path))


def main():
    input_string = ''

    try:
        input_string = sys.argv[1]
    except SyntaxError as ex:
        logger.exception("Can not find input params.")

    parser = Parser(input_string)
    parser.parse_params()

    logger.info(f'Key points - {parser.get_key_points}')
    find_shortest_path(parser.get_key_points)


if __name__ == "__main__":
    main()
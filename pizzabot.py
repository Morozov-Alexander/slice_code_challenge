import sys
import re

#./ pizzabot "5x5 (1,3) (4,4)"



def main():
    input_string = sys.argv[1]
    print(input_string)
    size_of_fields = re.findall("(\d+)x(\d+)",input_string)[0]
    key_points = re.findall("\((\d+),(\d+)\)",input_string)
    key_points = [ [int(i) for i in element] for element in key_points]
    size_of_fields = [int(i) for i in size_of_fields]
    print(size_of_fields)
    print(key_points)
    find_shortest_path(key_points)


def sort_function(point):
    return sum(point)


def find_shortest_path(key_points:list):
    key_points = sorted(key_points,key=sort_function)
    my_point = [0,0]
    string_path=''
    for key_point in key_points:
        delta_x , delta_y = key_point[0] - my_point[0], key_point[1] - my_point[1]

        if delta_x > 0:
            string_path += 'E'* abs(delta_x)
        elif delta_x < 0:
            string_path += 'W'* abs(delta_x)

        if delta_y > 0:
            string_path += 'N'* abs(delta_y)
        elif delta_y < 0:
            string_path += 'S'* abs(delta_y)
        string_path += 'D'
        my_point = key_point
        
    print(string_path)






if __name__ == "__main__":
    main()
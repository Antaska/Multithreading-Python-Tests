import logging
import random
import datetime 

ARRAY_LENGTH = 10
NUMBER_OF_CHANGES = 1000000

def array_creation():
    array = []
    for index in range(ARRAY_LENGTH):
        array.append(index)
    return array

def array_print(array):
    array_str = ""
    array_str += "("
    first = True
    for item in array:
        if first:
            array_str += "%d" % item
            first = False
        else:
            array_str += ", %d" % item
    array_str += ")"

    logging.info(array_str)

def make_permutations(array,number_of_changes):
    while number_of_changes >= 0:
        number_of_changes -= 1
        positions = choose_positions(len(array)-1)
        logging.info("Changing position %d with position %d",positions['position1'], positions['position2'])
        change_position_values(positions['position1'],positions['position2'], array)

def choose_positions(max_value):
    
    result = {}
    position1 = random.randint(0,max_value)
    position2 = random.randint(0,max_value)
    while position1 == position2:
        position2 = random.randint(0,max_value)
    
    result['position1'] = position1
    result['position2'] = position2

    return result


def change_position_values(position1, position2, array):
    value1 = array[position1]
    value2 = array[position2]
    array[position1] = value2
    array[position2] = value1

if __name__ == "__main__":
    timestamp1 = datetime.datetime.now() 
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Creating the Array")
    array = array_creation()
    logging.info("Array at the beginning")
    array_print(array)

    number_of_changes = NUMBER_OF_CHANGES
    logging.info("Beggining with the changes")
    make_permutations(array,number_of_changes)

    logging.info("Array at the end")
    array_print(array)
    timestamp2 = datetime.datetime.now()
    logging.info("Time used: %s seconds and %d microseconds",abs((timestamp2-timestamp1).seconds),abs((timestamp2-timestamp1).microseconds))

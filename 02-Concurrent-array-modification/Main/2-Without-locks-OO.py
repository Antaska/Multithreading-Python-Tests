import logging
import random
import datetime
import threading 

ARRAY_LENGTH = 10
NUMBER_OF_CHANGES = 10000000
LOGGING_LEVEL = logging.INFO

class Main:

    def __init__(self):
        pass
    
    def initialize_values(self,array_length,number_of_changes):
        self.array = Array(array_length)
        logging.info("Array created with the following data %s", self.array.to_string())
        self.changes = NumberOfChanges(number_of_changes)
    
    def do(self):
        task = Task()
        task.prepare(self.array,self.changes)
        logging.info("Starting the changes.")
        task.do()

    def finish(self):
        logging.info("Array at the end of the changes: %s", self.array.to_string())


class Task:
    def prepare_and_do(self, array, changes):
        self.prepare(array, changes)
        self.do()
        
    def prepare(self, array, changes):
        self._array = array
        self._changes = changes
    
    def do(self):
        while(self._changes.check_and_reserve_run()):
            position1 = self._array.get_random_position()
            position2 = self._array.get_random_position()
            while position1 == position2:
                position2 = self._array.get_random_position()
            self._array.swap_values(position1,position2)


class NumberOfChanges:
    def __init__(self, number_of_changes):
        logging.debug("Setting total number of changes to %d.",number_of_changes)
        self._number_of_changes = number_of_changes
    
    def check_and_reserve_run(self):
        if self.are_executions_remaining():
            self.reserve_run()
            logging.debug("Execution remaining found. There are still %d executions remaining after this one",self._number_of_changes)
            return True
        else:
            logging.debug("No more executions remaining.")
            return False

    def are_executions_remaining(self):
        return self._number_of_changes > 0

    def reserve_run(self):
        self._number_of_changes -= 1


class Array:
    def __init__(self, array_length):
        array = []
        for index in range(array_length):
            array.append(index)
        self._array = array
        self._length = array_length
        logging.debug("Array created with %d positions",array_length)
    
    def to_string(self):
        array_str = "("
        first = True
        for item in self._array:
            if first:
                array_str += "%d" % item
                first = False
            else:
                array_str += ", %d" % item
        array_str += ")"

        return array_str

    def get_array_length(self):
        return self._length
    
    def get_random_position(self):
        value = random.randint(0,self._length -1) 
        logging.debug("Random position chosen is %d", value)
        return value
    
    def swap_values(self, position1, position2):
        value1 = self._array[position1]
        value2 = self._array[position2]
        logging.debug("Value of position %d is %d and value of position %d is %d", position1, value1, position2, value2)
        self._array[position1] = value2
        self._array[position2] = value1
        logging.debug("After swapped: Value of position %d is %d and value of position %d is %d", position1, value1, position2, value2)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=LOGGING_LEVEL, datefmt="%H:%M:%S")

    main = Main()
    main.initialize_values(ARRAY_LENGTH,NUMBER_OF_CHANGES)
    timestamp1 = datetime.datetime.now()
    main.do()
    timestamp2 = datetime.datetime.now()
    main.finish()
    logging.info("Time used for changes: %s seconds and %d microseconds",abs((timestamp2-timestamp1).seconds),abs((timestamp2-timestamp1).microseconds))
class SortingRobot:
    def __init__(self, l):
        self._list = l          
        self._item = None       
        self._position = 0      
        self._light = "OFF"     
        self._time = 0          

    def can_move_right(self):
        return self._position < len(self._list) - 1

    def can_move_left(self):
        return self._position > 0

    def move_right(self):
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        self._time += 1
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        self._light = "ON"

    def set_light_off(self):
        self._light = "OFF"

    def light_is_on(self):
        return self._light == "ON"

    def sort(self):
        for k in range(len(self._list)-1):
            self.swap_item()
            while self.can_move_right():
                self.move_right()
                if self.compare_item() == 1:
                    self.swap_item()
            while self.can_move_left():
                self.move_left()
                if self.compare_item() == None:
                    self.swap_item()
                    break
            self.move_right()



if __name__ == "__main__":
   

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
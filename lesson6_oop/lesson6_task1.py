from datetime import datetime, timedelta


def get_diff_from_now_by_second(time):
    return (datetime.now() - time).seconds


class TrafficLight:
    __lifetime = 30

    _red = "Красный"
    _yellow = "Жёлтый"
    _green = "Зелёный"

    _red_length = 7
    _yellow_length = 2
    _green_length = 7

    colors = {_red: (1, _red_length),
              _yellow: (2, _yellow_length),
              _green: (3, _green_length)}

    def __init__(self):
        self.__color = self._red
        self.init_time = datetime.now()
        self.start_time = self.init_time

    def should_be_red(self, duration=_red_length):
        return get_diff_from_now_by_second(self.start_time) <= duration

    def should_be_yellow(self, duration=_yellow_length):
        return get_diff_from_now_by_second(self.start_time) <= self._red_length + duration

    def should_be_green(self, duration=_green_length):
        return get_diff_from_now_by_second(self.start_time) <= self._red_length + self._yellow_length + duration

    def check_color(self, current_color):
        if len(current_color) == 0:
            current_color = self._red
        index_of_current_color = self.colors.get(current_color)[0]
        index_of_object_color = self.colors.get(self.__color)[0]
        diff_of_index = index_of_object_color - index_of_current_color
        if diff_of_index > 1:
            print(f"Светофор сломался в {self.init_time}, сообщите в поддержку")
            self.__color = self._yellow
            self.init_time = self.init_time - timedelta(seconds=self.__lifetime)
            # raise RuntimeError(f"Светофор сломался в {self.init_time}, сообщите в поддержку")

    def running(self):
        self.start_time = self.init_time
        current_color = ""
        while get_diff_from_now_by_second(self.init_time) < self.__lifetime:
            if current_color != self.__color:
                self.check_color(current_color)
                print(f"{self.__color} горит")
                current_color = self.__color
            if self.should_be_red():
                continue
            elif self.should_be_yellow():
                self.__color = self._yellow
                continue
            elif self.should_be_green():
                self.__color = self._green
                continue
            else:
                self.__color = self._red
                self.start_time = datetime.now()


example = TrafficLight()
example.running()

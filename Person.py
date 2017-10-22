
class Person:

    def __init__(self, tin):
        self.wait_times = []
        self.status = None

        self.tin_door = tin
        self.tout_door = None

        self.choice = None

        self.t_serv_start = None
        self.t_serv_end = None

        self.t_co_start = None

    def total_time(self):
        return self.tout_door - self.tin_door

    def serv_time(self):
        return self.t_serv_end - self.t_serv_start

    def co_time(self):
        return self.tout_door - self.t_co_start

    def food_line_time(self):
        return self.t_serv_start - self.tin_door

    def co_line_time(self):
        return self.t_co_start - self.t_serv_end

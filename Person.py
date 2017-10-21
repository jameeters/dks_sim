
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
        return self.tin_door


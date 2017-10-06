import Line
class DQ:

    def __init__(self, name, service_station):
        self.name = name
        self.line = Line(name)
        self.service_station = service_station


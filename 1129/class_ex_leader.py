from abc import ABC, abstractclassmethod

electiricity_usage = [
    {"date" : "2024-11-01", "usage" : 12.5},
    {"date" : "2024-11-02", "usage" : 15.3},
    {"date" : "2024-11-03", "usage" : 10.8},
    {"date" : "2024-11-04", "usage" : 14.2},
    {"date" : "2024-11-05", "usage" : 13.6}
]

#추상클래스
class ElectrictityData(ABC) :
    def __init__(self, usage_data, total_usage) :
        self._usage_data = usage_data
        self._total_usage = total_usage

    @property
    def usage_data(self) :
        return self._usage_dat
    @usage_data.setter
    def usage_date(self, new_data) :
        self._usage_data = new_data

    @property
    def total_usage(self) :
        return self._total_usage
    @total_usage.setter
    def total_usage(self, new_total) :
        self._total_usage = new_total

    @abstractmethod
    def calculate_total_usage(self) :
        pass
    
    @abstractmethod
    def get_usage_on_data(self, date) :
        pass

    def add_usage(self, date, usage) :
        pass
    def remove_usage(self, date) :
        pass

class HomeElectricity(ElectrictityData) :

    def callculate_total_usage(self) :
        self.total_usage = sim(i["usage"] for i in self.usage_data)

    def get_usage_on_date(self, date) :
        for i in self.usage_data:
            if i["date"] == date :
                return i["usage"]

 
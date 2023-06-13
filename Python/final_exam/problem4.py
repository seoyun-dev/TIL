class date:
    def __init__(self, year, month, day):
        self.year  = year
        self.month = month
        self.day   = day
    
    def calculate_day(self):
        days = 360 * (self.year - 2023) + 30 * (self.month - 6) + (self.day - 13)
        res  = days % 7
        if res == 0:
            return "화요일"
        if res == 1:
            return "수요일"   
        if res == 2:
            return "목요일"  
        if res == 3:
            return "금요일"  
        if res == 4:
            return "토요일"  
        if res == 5:
            return "일요일"  
        if res == 6:
            return "월요일"  


date1 = date(2023, 6, 12)
print(date1.calculate_day())
date1 = date(2023, 6, 11)
print(date1.calculate_day())
date1 = date(2023, 5, 12)
print(date1.calculate_day())
date1 = date(2023, 6, 14)
print(date1.calculate_day())
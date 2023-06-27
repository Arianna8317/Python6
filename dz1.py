def _leap_year(year: int):
    if year % 4 == 0 and year % 100 != 0 or year % 400:
        return True 



def if_date(date: str="1.1.1111"):
    day, month, year = list(map(int, date.split('.')))
    if 1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            return _leap_year(year) and 1 <= day <= 29 or not _leap_year(year) and 1 <= day <= 28
        


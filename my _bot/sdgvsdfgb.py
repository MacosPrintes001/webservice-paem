from datetime import date, datetime
import datetime
def data_valida(data_user):
    try:
        
        data_ = str(data_user).split("/")

        day = int(data_[0])
        month = int(data_[1])
        year = int(data_[2])

        newDate = datetime.date(year, month, day)
        print(newDate)
        print(date.today())

        if newDate >= date.today():
            print("é valido")
        else:
            print("não é valido")  

    except ValueError:
        print("Deu ruim")

data = "27/07/2021"
data_valida(data)
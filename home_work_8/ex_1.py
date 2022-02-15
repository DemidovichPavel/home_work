class Data:

    def __init__(self, data):
        self.data = data


    @classmethod
    def fix_data(cls, data):
        my_data = data.split('.')
        my_list = []
        for i in my_data:
            my_list.append(int(i))
        return my_list

    @staticmethod
    def check_data(data):
        real_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if data[1] < 1 or data[1] > 12:
            print('do not getting laid my brain')
        else:
            if data[0] < 1 or data[0] > real_day[data[1]-1]:
                print('do not getting laid my brain')
            else:
                print(corect_data)


user_data = '38.06.1987'
corect_data = Data.fix_data(user_data)
corect_data_2 = Data.check_data(corect_data)













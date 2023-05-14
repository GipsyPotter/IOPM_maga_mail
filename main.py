import pandas as pd


def importData():
    Data = pd.read_csv('[Pre-Order] Tạp Chí 10PM (Responses) - Form responses 1.csv', dtype=str)
    Dataframe = pd.DataFrame(Data)
    Dataframe = Dataframe.drop(['Timestamp'], axis=1)
    Dataframe = Dataframe.drop(['Email address'], axis=1)
    Dataframe = Dataframe.drop(Dataframe.columns[9], axis=1).drop(Dataframe.columns[10], axis=1).drop(
        Dataframe.columns[11], axis=1).drop(Dataframe.columns[12], axis=1).drop(Dataframe.columns[13], axis=1)
    cols = [
        'Hãy nêu số lượng tạp chí bạn muốn đặt? (Lưu ý: Tiền sách chưa bao gồm phí ship cho các khách hàng nhận sách ngoài Trường THPT chuyên Trần Đại Nghĩa)',
        'Hãy nêu số lượng tạp chí bạn muốn đặt? (Lưu ý: Tiền sách chưa bao gồm phí ship cho các khách hàng nhận sách ngoài Trường THPT chuyên Trần Đại Nghĩa).1']
    Dataframe['Hãy nêu số lượng tạp chí bạn muốn đặt?'] = (
            Dataframe[cols[0]].astype(str) + Dataframe[cols[1]].astype(str)).str.replace('nan', '')
    Dataframe = Dataframe.drop(cols, axis=1)
    Dataframe.to_csv('Data.csv', index=False)
    return Dataframe


def getData(Dataframe, id):
    name = Dataframe['Họ và Tên của bạn'].values[id]
    mail = Dataframe['Email của bạn là?'].values[id]
    phone = Dataframe['Số điện thoại nha'].values[id]
    method = Dataframe['Bạn muốn nhận tạp chí như thế nào?'].values[id]
    payment = Dataframe['Các hình thức thanh toán mà bạn có thể lựa chọn: '].values[id]
    address = \
    Dataframe['Điền địa chỉ của bạn nè\nVD: Số nhà, Đường, Phường/Xã, Tỉnh/Thành phố, Ghi chú(Nếu có)'].values[id]
    amount = Dataframe['Hãy nêu số lượng tạp chí bạn muốn đặt?'].values[id]
    # print(name, mail, phone, method, payment, address, amount)
    return name, mail, phone, method, payment, address, amount


if __name__ == '__main__':
    Dataframe = importData()
    name, mail, phone, method, payment, address, amount = getData(Dataframe, 1)
    print(name, mail, phone, method, payment, address, amount)

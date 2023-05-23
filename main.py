import pandas as pd
import pyperclip


def importData():
    Data = pd.read_csv('C:\Desktop\[Pre-Order] Tạp Chí 10PM (Responses) - Form responses 1.csv', dtype=str)
    Dataframe = pd.DataFrame(Data)
    Dataframe = Dataframe.drop(['Timestamp'], axis=1)
    Dataframe = Dataframe.drop(['Email address'], axis=1)
    Dataframe = Dataframe.drop(Dataframe.columns[9], axis=1).drop(Dataframe.columns[10], axis=1).drop(
        Dataframe.columns[11], axis=1).drop(Dataframe.columns[12], axis=1).drop(Dataframe.columns[13], axis=1)
    cols = [
        '''Hãy nêu số lượng tạp chí bạn muốn đặt? (Lưu ý: Tiền sách chưa bao gồm phí ship cho các khách hàng nhận sách ngoài Trường THPT chuyên Trần Đại Nghĩa)
*Nếu số lượng sách quá 5 quyển, hãy liên hệ với Minh Trí''',
        '''Hãy nêu số lượng tạp chí bạn muốn đặt? (Lưu ý: Tiền sách chưa bao gồm phí ship cho các khách hàng nhận sách ngoài Trường THPT chuyên Trần Đại Nghĩa)
*Nếu số lượng sách quá 5 quyển, hãy liên hệ với Minh Trí.1''']
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


def manualData():
    name = input('Họ và Tên của bạn: ')
    mail = input('Email của bạn là?: ')
    phone = input('Số điện thoại nha: ')
    methods = ['Gửi bưu điện đến địa chỉ', 'Gửi grab express đến địa chỉ', 'Nhận tại trường THPT Chuyên Trần Đại Nghĩa',
               'Nhận tại điểm phát hành(TpHCM)']
    print('Bạn muốn nhận tạp chí như thế nào?')
    for i in range(len(methods)):
        print(i + 1, methods[i])
    method = methods[int(input('Chọn: ')) - 1]
    payments = ['Banking', 'Trực tiếp(tiền mặt)']
    print('Các hình thức thanh toán mà bạn có thể lựa chọn: ')
    for i in range(len(payments)):
        print(i + 1, payments[i])
    payment = payments[int(input('Chọn: ')) - 1]
    address = input('Điền địa chỉ của bạn nè')
    amount = input('Hãy nêu số lượng tạp chí bạn muốn đặt?')
    return name, mail, phone, method, payment, address, amount


def displayData(name, mail, phone, method, payment, address, amount):
    print('Họ và Tên của bạn: ', name)
    print('Email của bạn là?: ', mail)
    print('Số điện thoại nha: ', phone)
    print('Bạn muốn nhận tạp chí như thế nào?: ', method)
    print('Các hình thức thanh toán mà bạn có thể lựa chọn: ', payment)
    print('Điền địa chỉ của bạn nè: ', address)
    print('Hãy nêu số lượng tạp chí bạn muốn đặt?: ', amount)


def mailAuth(name, mail, phone, method, payment, address, amount):
    if amount == '1 quyển:':
        money = '65,000 VND'
    elif amount == '2 quyển:':
        money = '130,000 VND'
    elif amount == 'Combo 3 quyển:':
        money = '180,000 VND'
    elif amount == 'Combo 4 quyển:':
        money = '240,000 VND'
    elif amount == 'Combo 5 quyển:':
        money = '300,000 VND'
    mailDirectCash = f'''IOPM chào bạn,
Lời đầu tiên, IOPM xin được gửi lời cảm ơn chân thành nhất đến bạn khi đã quan tâm, tin tưởng, và đặt mua tạp chí của chúng mình. IOPM xin thông báo đơn hàng của bạn đã được xác nhận và hiện tại đang trong quá trình xử lý (chúng mình sẽ cố gắng gởi ẩn phẩm sớm nhất có thể cho bạn nhé). 

- Tên người nhận: {name}
- Số điện thoại: {phone}
- Số lượng: {amount}
- Thanh toán trực tiếp: {money}
- Thời gian nhận hàng dự kiến: Từ 1/6/2023
- Điểm nhận hàng: {method}
'''
    mailDirectBank = f'''IOPM chào bạn,
Lời đầu tiên, IOPM xin được gửi lời cảm ơn chân thành nhất đến bạn khi đã quan tâm, tin tưởng, và đặt mua tạp chí của chúng mình. IOPM xin thông báo đơn hàng của bạn đã được xác nhận và hiện tại đang trong quá trình xử lý (chúng mình sẽ cố gắng gởi ẩn phẩm sớm nhất có thể cho bạn nhé). 

- Tên người nhận: {name}
- Số điện thoại: {phone}
- Số lượng: {amount}
- Thanh toán: Đã chuyển khoản
- Thời gian nhận hàng dự kiến: Từ 1/6/2023
- Điểm nhận hàng: {method}
'''
    mailShip = f'''IOPM chào bạn,
Lời đầu tiên, IOPM xin được gửi lời cảm ơn chân thành nhất đến bạn khi đã quan tâm, tin tưởng, và đặt mua tạp chí của chúng mình. IOPM xin thông báo đơn hàng của bạn đã được xác nhận và hiện tại đang trong quá trình xử lý (chúng mình sẽ cố gắng gởi ẩn phẩm sớm nhất có thể cho bạn nhé). 

- Tên người nhận: {name}
- Số điện thoại: {phone}
- Địa chỉ: {address}
- Số lượng: {amount}
- Thanh toán: Đã chuyển khoản
- Thời gian nhận hàng dự kiến: Từ 1/6/2022
'''
    if method == 'Nhận tại điểm phát hành(TpHCM)' or method == 'Nhận tại trường THPT Chuyên Trần Đại Nghĩa':
        if payment == 'Trực tiếp(tiền mặt): Tại trường THPT Chuyên Trần Đại Nghĩa hoặc Điểm phát hành':
            return mailDirectCash
        else:
            return mailDirectBank
    else:
        return mailShip


def getIDfromEmail(Dataframe, mail):
    for i in range(len(Dataframe['Email của bạn là?'])):
        if Dataframe['Email của bạn là?'][i] == mail:
            return i


def autoMail():
    Dataframe = importData()
    print(Dataframe['Họ và Tên của bạn'])
    mailAddress = input('Chọn tên: ')
    id = getIDfromEmail(Dataframe, mailAddress)
    name, mail, phone, method, payment, address, amount = getData(Dataframe, id)
    displayData(name, mail, phone, method, payment, address, amount)
    mailSend = mailAuth(name, mail, phone, method, payment, address, amount)
    print(mailSend)
    pyperclip.copy(mailSend)
def autoMail2(email):
    Dataframe = importData()
    mailAddress = email
    id = getIDfromEmail(Dataframe, mailAddress)
    name, mail, phone, method, payment, address, amount = getData(Dataframe, id)
    displayData(name, mail, phone, method, payment, address, amount)
    mailSend = mailAuth(name, mail, phone, method, payment, address, amount)
    print(mailSend)
    pyperclip.copy(mailSend)

def manualMail():
    name, mail, phone, method, payment, address, amount = manualData()
    displayData(name, mail, phone, method, payment, address, amount)
    mailSend = mailAuth(name, mail, phone, method, payment, address, amount)
    print(mailSend)
    pyperclip.copy(mailSend)


if __name__ == '__main__':
    cur = input('1: Auto .CSV | 2: Manual: | 3: Exit: ')
    while cur != 3:
        # check is email
        if '@' in cur:
            autoMail2(cur)
        elif cur == '1':
            autoMail()
        elif cur == '2':
            manualMail()
        cur = input('1: Auto .CSV | 2: Manual: | 3: Exit: ')

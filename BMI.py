h = input('請輸入身高： ')
w = input('請輸入體重： ')
a = input('請輸入年齡： ')
h = float(h)
w = float(w)
a = int(a)
h = h / 100
BMI = w / h / h
print('你的BMI值為：', BMI)
if BMI < 16: 
    print('嚴重營養不良 ')
elif BMI > 16 and BMI < 18.5:
    print('體重過輕 ')
elif BMI > 18.5 and BMI < 24:
    print('正常範圍')
elif BMI > 24 and BMI < 27:
    print('過重')
elif BMI > 27 and BMI < 30: 
    print('輕度肥胖 ')
elif BMI > 30 and BMI < 35:
    print('中度肥胖')
elif BMI >= 35:
    print('重度肥胖')

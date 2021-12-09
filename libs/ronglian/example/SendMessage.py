from ronglian_sms_sdk import SmsSDK

# 容联云通讯分配的主账号ID
accId = '8aaf07087ce03b67017d19783f7a0c7e'
# 容联云通讯分配的主账号TOKEN
accToken = '0a114064e1e94628ae4484390e7a7d63'
# 容联云通讯分配的应用ID
appId = '8aaf07087ce03b67017d197840930c84'


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    # 容联云通讯创建的模板（免费账号只能使用指定模板）
    tid = '1'
    mobile = '13851601190'
    # 验证码：666666，时效：3分钟
    datas = ('666666', '3')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)


send_message()

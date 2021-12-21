from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from pyShop import settings


def generic_email_verify_token(user_id):
    '''
    对user_id加密生成token
    :param user_id:
    :return: 加密后的token
    '''
    s = Serializer(secret_key=settings.SECRET_KEY, expires_in=3600 * 24)
    # 对数据进行加密
    data = s.dumps({'user_id': user_id})
    return data.decode()


def check_verify_token(token):
    '''
    将token进行解密
    :param token:加密后的token
    :return: 解密后的token
    '''
    s = Serializer(secret_key=settings.SECRET_KEY, expires_in=3600 * 24)
    # 解密
    try:
        result = s.loads(token)
    except Exception as e:
        return None
    # result={'user_id': user_id}，见加密方法中的源数据
    return result.get('user_id')

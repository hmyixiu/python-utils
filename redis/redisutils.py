from redis import StrictRedis

"""
Redis Server
Redis配置文件的bind需要注释掉
但是protected-mode注释掉不可以，得手动设置为no

Python Redis Client
默认返回的是bytes格式的，设置个decode_responses=True，返回的是字符串了
"""

REDIS_HOST = '192.168.52.3'
REDIS_PORT = 6379

CONN = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

print(CONN)

a = CONN.get('a')
print(a)

from memcache import Client

"""
安装memcache时，遇到的问题，提示libevent
解决 yum install libevent
     yum install libevent-devel

"""

# 这里是个list，可以吧memcache集群这么搞
MC_SERVERS = ['192.168.52.3:11211', '192.168.52.3:11212']

CONN = Client(MC_SERVERS)

status = CONN.set('key1', 'val2', 0)
print(status)

status = CONN.delete('key')
print(status)

status = CONN.add('key', 'val', 20)
print(status)

status = CONN.replace('key', 'val1', 0)
print(status)

status = CONN.append('key', ',val2')
print(status)

data = CONN.get('key')
print(data)

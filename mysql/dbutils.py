import MySQLdb

DB_URL = '192.168.52.3'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = 'root'
DB_NAME = 'vip_test'

CONN = MySQLdb.connect(host=DB_URL, port=DB_PORT, user=DB_USER, passwd=DB_PWD,
                       db=DB_NAME, charset='utf8')


def ddl(sql, conn=None):
    """
    做ddl操作
    :param sql:
    :param conn:
    :return:
    """
    # 可以指定MySQL连接，不指定则使用默认连接
    if not conn:
        conn = CONN

    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()


def insert():
    pass


def delete():
    pass


def update():
    pass


def select_single():
    pass


def select_multi():
    pass


def render_data(data):
    """
    对执行sql返回的结果进行转换
    :param data:
    :return:
    """

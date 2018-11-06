import logging

"""
默认情况，logging模块将日志打印到屏幕上，日志级别高于WARNING才会输出
输出格式：
 WARNING  :    root    : warn message
日志级别  Logger实例名称  日志消息内容

日志级别
级别	何时使用
DEBUG	    详细信息，典型地调试问题时会感兴趣。
INFO	    证明事情按预期工作。
WARNING	    表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。
ERROR	    由于更严重的问题，软件已不能执行一些功能了。
CRITICAL	严重错误，表明软件已不能继续运行了。


Logger 记录器，暴露了应用程序代码能直接使用的接口。
Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
Formatter 格式化器，指明了最终输出中日志记录的布局。
"""
logger = logging.getLogger('wesfsd')
logger.setLevel(logging.ERROR)
handler = logging.StreamHandler(stream=None)
logger.addHandler(handler)
formatter = logging.Formatter(fmt=None, datefmt=None)
handler.setFormatter(formatter)
# logging.basicConfig(filename='logger.log', level=logging.WARNING)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

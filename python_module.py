# # -*- coding:utf-8 -*-
import sys
print('\n---------------------module:__builtin__--------------------')
print(vars())
print(dir(sys.modules['__builtin__']))

print('\n---------------------module:time--------------------')
import time

print(time.asctime())      # 返回时间格式：Sun May  7 21:46:15 2017
print(time.time())         # 返回时间戳 ‘1494164954.6677325’
print(time.gmtime())       # 返回本地时间 的struct time对象格式，time.struct_time(tm_year=2017, tm_mon=5, tm_mday=7, tm_hour=22, tm_min=4, tm_sec=53, tm_wday=6, tm_yday=127, tm_isdst=0)
print(time.localtime())    # 返回本地时间 的struct time对象格式，time.struct_time(tm_year=2017, tm_mon=5, tm_mday=7, tm_hour=22, tm_min=4, tm_sec=53, tm_wday=6, tm_yday=127, tm_isdst=0)
print(time.gmtime(time.time()-800000))   # 返回utc时间的struc时间对象格式
print(time.asctime(time.localtime()))    # 返回时间格式Sun May  7 22:15:09 2017
print(time.ctime())                      # 返回时间格式Sun May  7 22:15:09 2017
print(time.strftime('%Y-%m-%d'))         #默认当前时间 2017-05-07
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #默认当前时间 2017-05-07

string_struct = time.strptime("2016/05/22","%Y/%m/%d") # 将日期字符串 转成 struct时间对象格式
print(string_struct)                     # 返回struct time对象格式 time.struct_time(tm_year=2016, tm_mon=5, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=143, tm_isdst=-1)

# 将日期字符串转成时间戳
struct_stamp = time.mktime(string_struct) # 将struct time时间对象转成时间戳
print(struct_stamp)                         # 返回时间戳 ‘1463846400.0’

# 将时间戳转为字符串格式
print(time.gmtime(time.time()-86640))         # 将utc时间戳转换成struct_time格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) # 将utc struct_time格式转成指定的字符串格式


print('\n---------------------module:datetime--------------------')
import datetime
# 时间加减
print(datetime.datetime.now())           # 返回当前时间 2017-05-07 22:36:45.179732
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转换成日期格式 2017-05-07
print(datetime.datetime.now() + datetime.timedelta(3))    # 返回时间在当前日期上 +3 天
print(datetime.datetime.now() + datetime.timedelta(-3))    # 返回时间在当前日期上 -3 天
print(datetime.datetime.now() + datetime.timedelta(hours= 3)) # 返回时间在当前时间上 +3 小时
print(datetime.datetime.now() + datetime.timedelta(minutes= 30)) # 返回时间在当前时间上 +30 分钟

c_time  = datetime.datetime.now()
print(c_time)                          # 当前时间为 2017-05-07 22:52:44.016732
print(c_time.replace(minute=3,hour=2)) # 时间替换 替换时间为‘2017-05-07 02:03:18.181732’

print(datetime.timedelta)      # 表示时间间隔，即两个时间点之间的长度
print (datetime.datetime.now() - datetime.timedelta(days=5))  # 返回时间在当前时间上 -5 天

print('\n---------------------module:calendar--------------------')
# python 日历模块
import calendar

print(calendar.calendar(theyear= 2017))     # 返回2017年整年日历
print(calendar.month(2017,5))               # 返回某年某月的日历，返回类型为字符串类型

calendar.setfirstweekday(calendar.WEDNESDAY) # 设置日历的第一天(第一天以星期三开始）
cal = calendar.month(2017, 4)
print (cal)

print(calendar.monthrange(2017,5))        # 返回某个月的第一天和这个月的所有天数
print(calendar.monthcalendar(2017,5))     # 返回某个月以每一周为元素的序列

cal = calendar.HTMLCalendar(calendar.MONDAY)
print(cal.formatmonth(2017, 5))           # 在html中打印某年某月的日历

print(calendar.isleap(2017))             # 判断是否为闰年
print(calendar.leapdays(2000,2017))       # 判断两个年份间闰年的个数

print('\n---------------------module:random--------------------')
import random

# 随机数
print(random.random())              # 返回一个随机小数'0.4800545746046827'
print(random.randint(1,5))          # 返回（1-5）随机整型数据
print(random.randrange(1,10))       # 返回（1-10）随机数据

# 生成随机验证码
code = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    code += str(temp)

print(code)

print('\n---------------------module:os--------------------')
import os

print(os.getcwd())        # 获得当前工作目录
print(os.chdir(os.getcwd())) # 改变当前脚本的工作路径，相当于shell下的cd
print(os.curdir)            # 返回当前目录‘.'
print(os.pardir)            # 获取当前目录的父目录字符串名‘..'
print(os.makedirs('dirname1/dirname2'))     # 可生成多层递归目录
print(os.removedirs('dirname1/dirname2'))      # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
print(os.mkdir('test4'))         # 生成单级目录；相当于shell中mkdir dirname
print(os.rmdir('test4'))        # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir(os.getcwd()))   # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# print(os.remove('log.log'))            # 删除一个指定的文件
os.mkdir('oldname')
print(os.rename("oldname","newname"))    # 重命名文件/目录)
print(os.stat(os.getcwd()))     # 获取文件/目录信息
print(os.pathsep)            # 输出用于分割文件路径的字符串';'
print(os.name)               # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# print(os.system(command='ls'))   # 运行shell命令，直接显示
print(os.environ)                  # 获得系统的环境变量
print(os.path.abspath(os.getcwd()))   # 返回path规范化的绝对路径
print(os.path.split(os.getcwd()))     # 将path分割成目录和文件名二元组返回
print(os.path.dirname(os.getcwd()))    # 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(os.getcwd()))   # 返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists('test'))                 # 判断path是否存在
print(os.path.isabs(os.getcwd()))    # 如果path是绝对路径，返回True
print(os.path.isfile('test'))                   # 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isdir(os.getcwd()))    # 如果path是一个存在的目录，则返回True。否则返回False
print(os.path.getatime(os.getcwd()))   # 返回path所指向的文件或者目录的最后存取时间
print(os.path.getmtime(os.getcwd()))   # 返回path所指向的文件或者目录的最后修改时间


print('\n---------------------module:sys--------------------')
import sys

print(sys.argv)          # 命令行参数List，第一个元素是程序本身路径
# print(sys.exit(0))     # 退出程序，正常退出时exit(0)
print(sys.version)       # 获取python的版本信息
print(sys.path)          # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)      # 返回操作平台的名称


print('\n---------------------module:shutil--------------------')
import shutil
fsrc = open("fsrc.txt", 'w+') #直接打开一个文件，如果文件不存在则创建文件
fdst = open("fdst.txt", 'w') #直接打开一个文件，如果文件不存在则创建文件
fsrc.write('fsrc')
src = "fsrc.txt"
dst = "fdst.txt"
shutil.copyfileobj(fsrc, fdst, length=16*1024)      # 将文件内容拷贝到另一个文件中，可以是部分内容
shutil.copyfile(src, dst)                           # 拷贝文件
shutil.copymode(src, dst)                           # 仅拷贝权限。内容、组、用户均不变
shutil.copystat(src, dst)                           # 拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copy(src, dst)                               # 拷贝文件和权限
shutil.copy2(src, dst)                              # 拷贝文件和状态信息
shutil.move(src, dst)                               # 递归的去移动文件

# base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径
# format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# root_dir： 要压缩的文件夹路径（默认当前目录）
# owner： 用户，默认当前用户
# group： 组，默认当前组
# logger： 用于记录日志，通常是logging.Logger对象
shutil.make_archive('archive_base_name', 'zip',os.getcwd())   # 创建压缩包并返回文件路径，例如：zip、tar

print('\n---------------------module:zipfile--------------------')
#shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的：
# zipfile 压缩解压
import zipfile
# 压缩
z = zipfile.ZipFile('archive_base_name.zip', 'w')
z.write('fdst.txt')
z.close()

# 解压
z = zipfile.ZipFile('archive_base_name.zip', 'r')
z.extractall()
z.close()

print('\n---------------------module:tarfile--------------------')
# tarfile 压缩解压
import tarfile

# 压缩
tar = tarfile.open('your.tar','w')
tar.add('archive_base_name.zip')
# tar.add('/Users/wupeiqi/PycharmProjects/cmdb.zip', arcname='cmdb.zip')
tar.close()

# 解压
tar = tarfile.open('your.tar','r')
tar.extractall()  # 可设置解压地址
tar.close()


print('\n---------------------module:xml--------------------')
# xml的格式如下，就是通过<>节点来区别数据结构的:
xmlstr = r'''<?xml version="1.0"?>
<data>

    <country name="Liechtenstein">

        <rank updated="yes">2</rank>

        <year>2008</year>

        <gdppc>141100</gdppc>

        <neighbor name="Austria" direction="E"/>

        <neighbor name="Switzerland" direction="W"/>

    </country>

    <country name="Singapore">

        <rank updated="yes">5</rank>

        <year>2011</year>

        <gdppc>59900</gdppc>

        <neighbor name="Malaysia" direction="N"/>

    </country>

    <country name="Panama">

        <rank updated="yes">69</rank>

        <year>2011</year>

        <gdppc>13600</gdppc>

        <neighbor name="Costa Rica" direction="W"/>

        <neighbor name="Colombia" direction="E"/>

    </country>

</data> 
'''

#  xml协议在各个语言里的都 是支持的，在python中可以用以下模块操作xml 　

import xml.etree.ElementTree as ET
fpxml = open('xmltest.xml', 'w+')
fpxml.write(xmlstr)
fpxml.close()
tree = ET.parse("xmltest.xml")
root = tree.getroot()
print(root.tag)

#遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag,i.text)

#只遍历year 节点
for node in root.iter('year'):
    print(node.tag,node.text)


# 修改和删除xml文档内容

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")
root = tree.getroot()

#修改

for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated","yes")
tree.write("xmltest.xml")

#删除node

for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
       root.remove(country)
tree.write('output.xml')


# 自己创建xml文档
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
age = ET.SubElement(name, "age")
age.text = '33'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'
et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)
ET.dump(new_xml)  # 打印生成的格式

print('\n---------------------module:configparser--------------------')
# 好多软件的常见文档格式如下
'''
[DEFAULT]
 compressionlevel = 9
 serveraliveinterval = 45
 compression = yes
 forwardx11 = yes
 
 [bitbucket.org]
 user = hg
 
 [topsecret.server.com]
 host port = 50022
 forwardx11 = no
'''
 # python 生成一个这样的文档
try:
  import configparser
except ImportError as e:
  pass
else:
  


  config = configparser.ConfigParser()

  config["DEFAULT"] = {'ServerAliveInterval': '45',
                  'Compression': 'yes',
                  'CompressionLevel': '9'}

  config['bitbucket.org'] = {}
  config['bitbucket.org']['User'] = 'hg'
  config['topsecret.server.com'] = {}
  topsecret = config['topsecret.server.com']
  topsecret['Host Port'] = '50022'
  topsecret['ForwardX11'] = 'no'
  config['DEFAULT']['ForwardX11'] = 'yes'
  with open('example.ini', 'w') as configfile:
    config.write(configfile)

  # 写完了还可以再读出来
  config = configparser.ConfigParser()
  config.sections()
  file = config.read('example.ini')
  print(file)      # ['example.ini']

  title = config.sections()
  print(title)     # ['bitbucket.org', 'topsecret.server.com']

  print('bitbucket.org' in config)     # True
  print('bytebong.com' in config)      # False
  print(config['bitbucket.org']['User'])   # hg
  print(config['DEFAULT']['Compression'])   # yes

  topsecret = config['topsecret.server.com']
  print(topsecret['ForwardX11'])           # no
  print(topsecret['Host Port'])         # 50022

  for key in config['topsecret.server.com']:
  	print(key)
  '''
  输出结果:
         host port
         forwardx11
         compressionlevel
         serveraliveinterval
         compression
  '''
  print(config['topsecret.server.com']['Compression'])   # yes

  # configparser增删改查语法
  config = configparser.ConfigParser()
  config.read('i.cfg')

  secs = config.sections()       # 返回配置文件中的主节点
  print (secs)

  options = config.options('bitbucket.org')
  print(options)                 # 返回所有子节点信息

  item_list = config.items('bitbucket.org')
  print(item_list)              # 列出所有子节点详细信息

  val = config.get('topsecret.server.com','host port')
  print(val)                    # 返回单个子节点信息

  val2 = config.getint('topsecret.server.com','host port')
  print(val2)

  # 删除'bitbucket.org'
  sec = config.remove_section('bitbucket.org')
  config.write(open('i.cfg','w'))

  sec2 = config.add_section('huhuan2')      # 添加主节点
  config.set('huhuan2','k','1111')          # 添加子节点
  config.set('huhuan','kk','2222')
  config.remove_option('huhuan','kk')       # 删除子节点
  config.write(open('i.cfg','w'))

print('\n---------------------module:logging--------------------')
import logging

# %(message)s 日志信息
# %（levelno)s 日志级别
# datefmt  设置时间格式
# filename  设置日志保存的路径
# level=loggin.INFO意思是，把日志纪录级别设置为INFO，也就是说，只有比日志是INFO或比INFO级别更高的日志才会被纪录到文件里，
# 在这个例子， 第一条日志是不会被纪录的，如果希望纪录debug的日志，那把日志级别改成DEBUG就行了。
logging.basicConfig(format='%(asctime)s %(message)s %(levelno)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='example.log',level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')

logger = logging.getLogger('TEST_LOG')    # 获得一个Logger
logger.setLevel(logging.DEBUG)            # 设置日志级别

ch = logging.StreamHandler()            # logging.StreamHandler这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息。
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler("access.log")  # 用于向一个文件输出日志信息。不过FileHandler会帮你打开这个文件
fh.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 设置日志记录的最终输出格式

ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 添加ch,fh到logger
logger.addHandler(ch)
logger.addHandler(fh)


logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

print('\n---------------------module:pickle--------------------')
try:
  import pickle
except ImportError as e:
  pass
else:
  date = {'k1':'123','k2':'hello'}

  str = pickle.dumps(date)    # pickle.dumps 将数据通过特殊的形式转换为只有python认识的字符串
  print(str)

  with open('result.pk','w') as fp:  # pickle.dump 将数据通过特殊的形式转换为只有python认识的字符串并写入文件
      pickle.dump(date,fp)


print('\n---------------------module:json--------------------')
import json

str1 = json.dumps(date)     # json.dumps 将数据通过特殊形式转换为所有程序语言都认识的字符串
print(str1)

with open('result1.json','w') as fp:  #json.dump 将数据通过特殊的形式转换为只有python认识的字符串并写入文件
    json.dump(date,fp)
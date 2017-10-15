import re

ptn = re.compile(r'[a-zA-Z0-9]+@[a-z0-9]+\.[a-z]{2,3}|\d{11}')


def matching(ptn, string):
    message = re.findall(ptn, string)
    print(message)


def main():
    txt = '''我的电子邮件tom@gmail.com.
             将什么发送到jerry123@163.com或者3123432@qq.com.
             若遇特殊情况打电话给18212344567.'''
    matching(ptn, txt)


main()

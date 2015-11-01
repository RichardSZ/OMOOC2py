# _*_ coding:utf-8 _*_
# Quick Python Script Expalanation for Programmers
# 给程序员的超快速py脚本解说
import os

def main():
    print 'Hello world!'

    print "This is Alice's greeting."
    print 'This is Bob\'s greeting.'

    foo(5,10)

    print '=' * 10
    print 'Current working directory is '+os.getcwd()

    counter = 0
    counter += 1

    food = ['apples','oranges','cats']
    for i in food:
        print 'I like to eat '+i

    print 'count to ten:'
    for i in range(10):
        print i

def foo(param1,secondparam):
    res = param1 + secondparam
    print '%s plus %s equal %s' %(param1,secondparam,res)
    if res < 50:
        print 'foo'
    elif(res>=50) and ((param1==42) or (secondparam==24)):
        print 'bar'
    else:
        print 'moo'
    return res   #这是单行注释
    '''这是多
行注释.....'''

if __name__=='__main__':
    main()

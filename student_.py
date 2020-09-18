"""测试github"""
import fire
import os
import sys
import importlib
class A():
    def hello(self,name):
        print("你好呀")
        return "hello"+name
    #
    def student(self):
        print("student")
        return "helllo"
    @property
    def print_(self):
        print("xz"+os.getcwd())
        a = importlib.import_module("test_scr.s1")
        a.main()
        return "dfdfdfds"

if __name__ == '__main__':
    fire.Fire(A)

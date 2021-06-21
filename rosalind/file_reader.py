'''
テストデータを読み込む処理
input : file_name:str -> 各テストケースを特定する文字列
output : List[str] -> テストケースを配列に変換して返す
'''
import os

def readFile(file_name):
    file_name = file_name.replace('.py','')
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind_'+file_name+'.txt')
    with open(file, "r") as file:
        return file.readlines()

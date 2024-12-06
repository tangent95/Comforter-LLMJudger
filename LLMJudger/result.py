# -*- coding: utf-8 -*-

'''
这里封装了大模型调用结果
'''

import pydantic

from . import basis

class DataJudgeResultBlock(pydantic.BaseModel):
    index : int
    basis : str = ''
    level : str

class DataJudgeResult(pydantic.BaseModel):
    result : list[DataJudgeResultBlock] = []

def level_to_score(input : str) -> int:
    '''
    根据ai的结果，将设置的评级转化为分数
    '''
    result = 0
    if (input == '非常反对'):
        result = -3
    elif (input == '反对'):
        result = -2
    elif (input == '比较反对'):
        result = -1
    elif (input == '比较支持'):
        result = 1
    elif (input == '支持'):
        result = 2
    elif (input == '非常支持'):
        result = 3
    return result

class JudgeResult(object):
    '''
    大模型判断结果的类
    '''
    def __init__(self):
        self.result = DataJudgeResult()
        self.basis_list = basis.basis_list

    def add_result(self, index : int, level : str):
        self.result.result.append(DataJudgeResultBlock(index=index, basis=self.basis_list[index-1], level=level))

    def to_vector(self) -> list[int]:
        '''
        按依据顺序返回依据对应的评级数字（-3, -2, -1, 0, 1, 2, 3）列表，可用于神经网络
        '''
        ret = [0 for _ in range(len(self.basis_list))]
        for item in self.result.result:
            ret[item.index-1] = level_to_score(item.level)
        return ret

    def to_dict(self) -> dict:
        '''
        按依据名称并对应评级名字返回字典，不保证依据顺序与依据文件相同
        '''
        ret = {}
        for item in self.result.result:
            ret[item.basis] = item.level
        return ret

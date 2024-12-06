# -*- coding: utf-8 -*-

'''
这里封装了判断依据
'''

import os

# 获取依据列表
with open(os.path.join(os.path.dirname(__file__), 'judge_basis.txt'), encoding='utf-8-sig') as f:
    __basis_str = f.read()
basis_list = __basis_str.strip().split('\n')
basis_list = list(map(lambda obj : obj.strip(), basis_list)) # 多余空格
basis_list = list(filter(lambda obj : obj, basis_list)) # 多余回车

def generate_basis(offset_range : tuple[int, int]):
    basis_str = ''
    for offset in range(offset_range[0], min(offset_range[1], len(basis_list)), 1):
        basis_str += str(offset + 1) + '. ' + basis_list[offset] + '\n'
    return basis_str

def generate_all(granularity : int):
    result = []
    for offset_start in range(0, len(basis_list), granularity):
        result.append(generate_basis((offset_start, offset_start + granularity)))
    return result

def get_basis(offset : int):
    return basis_list[offset]
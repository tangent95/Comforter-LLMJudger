# -*- coding: utf-8 -*-

'''
这里封装了请求模板
'''

import os
import langchain
import langchain.prompts

with open(os.path.join(os.path.dirname(__file__), 'judge_task_template.md'), encoding='utf-8-sig') as f:
    judge_template_str = f.read().strip()
judge_template = langchain.prompts.ChatPromptTemplate.from_messages([('user',judge_template_str)])

def generate_one(judge_basis : str, content : str):
    return judge_template.invoke({'judge_basis':judge_basis, 'content':content})
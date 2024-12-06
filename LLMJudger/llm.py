# -*- coding: utf-8 -*-

'''
这里封装了大模型调用
'''

import asyncio
import json
import langchain
import langchain.chat_models
import langchain.chat_models.base
import langchain_openai

from . import basis, template, result

async def async_run_task(model : langchain.chat_models.base.BaseChatModel, task):
    response_text = ''
    async for token in model.astream(task):
        response_text += token.content
    return response_text

def run_judge_task(model : langchain.chat_models.base.BaseChatModel, content : str, granularity : int) -> result.JudgeResult:
    '''
    运行大模型判断任务

    Args:
        model (BaseChatModel):LLM
        content (str):发言内容
        granularity (int):分割粒度（每次最大处理多少条依据），越小判断越准确，但花费更大

    Returns:
        JudgeResult
    '''
    response = result.JudgeResult()
    task_list = []
    for split_basis in basis.generate_all(granularity):
        task = template.generate_one(split_basis, content)
        task_list.append(async_run_task(model, task))

    async def main():
        tasks = asyncio.gather(*task_list)
        return await tasks
    
    for response_text in asyncio.run(main()):
        response_dict : dict = json.loads(response_text)
        for index, level in response_dict.items():
            response.add_result(int(index), level)
    return response

# openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current requests list.', 'type': 'limit_requests', 'param': None, 'code': 'limit_requests'}, 'request_id': 'xxx'}
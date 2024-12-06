# -*- coding: utf-8 -*-

'''
模块功能：使用大模型判断发言是否需要被安慰或温暖

使用例子：
limit = InMemoryRateLimiter(requests_per_second=1200/60, check_every_n_seconds=0.01, max_bucket_size=1000000)

指出在这里创建InMemoryRateLimiter后会输出：
LangChainBetaWarning: Introduced in 0.2.24. API subject to change.
  limit = InMemoryRateLimiter(requests_per_second=1200/60, check_every_n_seconds=0.01, max_bucket_size=1000000)

model = langchain_openai.ChatOpenAI(base_url='https://dashscope.aliyuncs.com/compatible-mode/v1', api_key='xxx', model='qwen-max', rate_limiter=limit)
ret = judger.llm.run_judge_task(model, 'xxx', 1)
print(json.dumps(ret.to_dict(), ensure_ascii=False, indent=4))
'''
from .llm import run_judge_task

from .result import JudgeResult

from .basis import generate_basis
from .basis import generate_all
from .basis import get_basis

from .template import generate_one

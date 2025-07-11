import os

from dashscope import Generation


def main():
    messages = [
        {'role': 'system',
         'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？你能做什么？'}
    ]

    response = Generation.call(api_key=os.environ['AI_DASHSCOPE_API_KEY'], model=Generation.Models.qwen_max, messages=messages,
                           result_format="message", )

    if response.status_code == 200:
        print(response.output.choices[0].message.content)
    else:
        print(f"HTTP返回码：{response.status_code}")
        print(f"错误码：{response.code}")
        print(f"错误信息：{response.message}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")

if __name__ == '__main__':
    main()
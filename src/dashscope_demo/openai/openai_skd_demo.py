import os
from openai import OpenAI


def main():
    try:
        client = OpenAI(
            api_key=os.environ['AI_DASHSCOPE_API_KEY'],
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        chat_completion = client.chat.completions.create(model="qwen-plus",
                                                         messages=[{'role': 'system',
                                                                    'content': 'You are a helpful assistant.'},
                                                                   {'role': 'user', 'content': '你是谁？'}])

        print(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"错误信息：{e}")
        print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")

if __name__ == '__main__':
    main()

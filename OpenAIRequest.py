from openai import OpenAI


class OpenAIRequest(object):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.chat_log = list()
        self.client = OpenAI(api_key=self.api_key)

    def get_chat_log(self):
        return self.chat_log

    def send_message(self, message: str):
        try:
            self.chat_log.append({"role": "user", "content": message})
            completions = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                # model="gpt-4o",
                messages=self.chat_log
            )
            response = {
                "role": completions.choices[0].message.role,
                "content": completions.choices[0].message.content,
            }
            self.chat_log.append(response)
            return response
        except Exception as ex:
            print(f'Error in send_message(): {ex}')
            return None

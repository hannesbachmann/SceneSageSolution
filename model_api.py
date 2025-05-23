import ollama


def model_request(req_append):
    # define used model
    # define input messages for roles system and user
    ollama_response = ollama.chat(model='deepseek-r1:14b', messages=[
       {
         'role': 'system',
         'content': 'You are a helpful assistant which is analysing subtitles of a video scene. The sentences given are all from one scene.',
       },
       {
         'role': 'user',
         'content': f'Give a one-sentence summary of the scene. Including who might speak. Use the following subtitles: "{req_append}"'
       },
    ])
    # return generated response
    # <think> thinking_process </think> model_response      -> format for deepseek-r1 models
    return ollama_response['message']['content']


# if __name__ == '__main__':
#     model_request()
#     pass
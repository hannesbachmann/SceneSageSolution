import ollama


def model_request(sys_input, user_input):
    # define used model
    # define input messages for roles system and user
    ollama_response = ollama.chat(model='deepseek-r1:14b', messages=[
       {
         'role': 'system',
         'content': sys_input,
       },
       {
         'role': 'user',
         'content': user_input,
       },
    ])
    # return generated response
    # <think> thinking_process </think> model_response      -> format for deepseek-r1 models
    return ollama_response['message']['content']


def get_summary(scene_sub):
    sys_input = 'You are a helpful assistant which is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'Give a one-sentence summary of the scene. Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input)


def get_speakers(scene_sub):
    sys_input = 'You are a helpful assistant which is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'List up all distinct speakers in the scene in the form "[speaker 1, speaker 2, ...]". Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input)


def get_mood(scene_sub):
    sys_input = 'You are a helpful assistant which is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'Which is the dominant mood in the scene?. Answer in only one word. Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input)


def get_references(scene_sub):
    sys_input = 'You are a helpful assistant which is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'List any cultural references that are contained within the scene. If there is no reference, return only the word "None". Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input)


# if __name__ == '__main__':
#     model_request()
#     pass
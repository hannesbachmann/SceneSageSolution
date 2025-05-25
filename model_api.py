import ollama


def model_request(sys_input: str, user_input: str, model: str):
    """Generate a LLM output using a system and user prompt for a specified LLM.

    :param sys_input: system prompt
    :param user_input: user prompt
    :param model: model name
    :return: string, model response
    """
    # define used model
    # chat with model with messages for roles system and user
    ollama_response = ollama.chat(model=model, messages=[
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


def get_summary(scene_sub: str, model: str):
    """Use an LLM to generate a summary of a given scene subtitles.

    :param scene_sub: Subtitles for the current scene
    :param model: model name
    :return: string, summary of the scene content
    """
    sys_input = 'You are a helpful assistant who is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'Give a one-sentence summary of the scene. Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input, model)


def get_speakers(scene_sub: str, model: str):
    """Use an LLM to determine which speakers are corresponding to the subtitles.

    :param scene_sub: Subtitles for the current scene
    :param model: model name
    :return: string, all speakers corresponding to the subtitles
    """
    sys_input = 'You are a helpful assistant who is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'List up all distinct speakers in the scene in the form "[role 1, role 2, ...]". ' \
                 f'Always return at least one speaker, use Narrator as default speaker role if no other information is given. ' \
                 f'Return only a list of speakers represented as their roles in the scene. Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input, model)


def get_mood(scene_sub: str, model: str):
    """Use an LLM to determine the overall represented mood in this scene.

    :param scene_sub: Subtitles for the current scene
    :param model: model name
    :return: string, mood
    """
    sys_input = 'You are a helpful assistant who is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'Which is the dominant mood in the scene? ' \
                 f'Select one of the following: ["Melancholic", "Romantic", "Tense", "Mysterious", "Humorous", "Cheerful", "Exciting", "Dark", "Hopeful", "Contemplative"]. ' \
                 f'Return only one word. Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input, model)


def get_references(scene_sub: str, model: str):
    """Use an LLM to detect all cultural references that might be contained in the scene subtitles.

    :param scene_sub: Subtitles for the current scene
    :param model: model name
    :return: string, cultural references contained within the scene content
    """
    sys_input = 'You are a helpful assistant who is analysing subtitles of a video scene. The sentences given are all from one scene.'
    user_input = f'List any cultural references that are contained within the scene. ' \
                 f'Return for each reference mentioned only up to three words. ' \
                 f'Return a list of references in the form: "[reference 1, reference 2]". ' \
                 f'If there is no reference, return only the word "None". Use the following subtitles: "{scene_sub}"'
    return model_request(sys_input, user_input, model)

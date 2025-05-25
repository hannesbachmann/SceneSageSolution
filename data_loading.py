import srt
import json


def load_srt_from_file(filename):
    """Load a .srt file containing subtitles. Converting them into an easy-to-process format.

    :param filename: input subtitle filename, should end with .srt
    :return: list of dicts: {start: timedelta, end: timedelta, content: str}
    """
    with open(filename, 'r') as f:
        subs = srt.parse(f.read())
    subtitles = list(subs)
    contained_in_subs = [{'start': sub.start,
                          'end': sub.end,
                          'content': sub.content.replace('\n', ' ')} for sub in subtitles]
    return contained_in_subs


def store_json(data: list, exp_filename: str):
    """Store data in a json format file.

    :param data: list of dicts: {start: str, end: str, transcript: str,
                                summary: str, characters: list, mood: str, cultural_ref: list}
    :param exp_filename: export filename, should end on .json
    """
    # convert a json like python structure to json and store in file
    json_data = json.dumps(data)
    with open(exp_filename, 'w') as f:
        json.dump(json_data, f)
    pass


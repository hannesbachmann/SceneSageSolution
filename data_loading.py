import srt
import json


def load_srt_from_file(filename):
    with open(filename, 'r') as f:
        subs = srt.parse(f.read())
    subtitles = list(subs)
    contained_in_subs = [{'start': sub.start,
                          'end': sub.end,
                          'content': sub.content.replace('\n', ' ')} for sub in subtitles]
    return contained_in_subs


def store_json(data, exp_filename):
    # convert a json like python structure to json and store in file
    json_data = json.dumps(data)
    with open(exp_filename, 'w') as f:
        json.dump(json_data, f)
    pass


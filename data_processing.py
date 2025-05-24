from datetime import timedelta
import re


def combine_subs_into_sentences(srt_data):
    subs = [sub['content'] for sub in srt_data]
    new_srt_data = []
    full_sentences = []
    current_sentence = []
    start_time = srt_data[0]['start']

    for i, subsentence in enumerate(subs):
        current_sentence.append(subsentence.strip())
        # check if sentence ends
        if subsentence[-1] in '.!?':
            # join the subsentences
            full_sentences.append(' '.join(current_sentence))
            new_srt_data.append({'start': start_time,
                                 'end': srt_data[i]['end'],
                                 'content': ' '.join(current_sentence)})
            current_sentence = []
            if i + 1 < len(subs):
                start_time = srt_data[i + 1]['start']

    # add leftover subsentences
    if current_sentence:
        full_sentences.append(' '.join(current_sentence))
        new_srt_data.append({'start': start_time,
                             'end': srt_data[-1]['end'],
                             'content': ' '.join(current_sentence)})

    return new_srt_data


def split_by_pauses(srt_data, pause_length=4):
    subs = [sub['content'] for sub in srt_data]
    new_srt_data = []
    full_sentences = []
    current_sentence = []
    start_time = srt_data[0]['start']
    pauses = []

    # calculate pauses
    for i, subsentence in enumerate(subs):
        current_sentence.append(subsentence.strip())
        # test if pause between two consecutive (current and next) subs is >= pause_length
        if i + 1 < len(subs):
            pause = srt_data[i + 1]['start'] - srt_data[i]['end']
        else:
            pause = timedelta(seconds=pause_length + 1)
        pauses.append(pause)
        if pause >= timedelta(seconds=pause_length):
            full_sentences.append(' '.join(current_sentence))
            # join the subsentences
            full_sentences.append(' '.join(current_sentence))
            new_srt_data.append({'start': start_time,
                                 'end': srt_data[i]['end'],
                                 'content': ' '.join(current_sentence)})
            current_sentence = []
            if i + 1 < len(subs):
                start_time = srt_data[i + 1]['start']

    # add leftover subsentences
    if current_sentence:
        full_sentences.append(' '.join(current_sentence))
        new_srt_data.append({'start': start_time,
                             'end': srt_data[-1]['end'],
                             'content': ' '.join(current_sentence)})

    return new_srt_data


def format_timedelta(td):
    # format timedelta into a more readable string output of the form 00:00:00:000 (same as in .srt)
    total_milliseconds = int(td.total_seconds() * 1000)

    hours, remainder = divmod(total_milliseconds, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds, milliseconds = divmod(remainder, 1000)

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def extract_model_response(text):
    # removes everything within <think>...</think> to only return the model response without the thinking process
    return re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL)

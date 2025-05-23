from data_loading import load_srt_from_file
from model_api import model_request
from data_processing import combine_subs_into_sentences, split_by_pauses


def run_all():
    # load subtitle data from a .srt
    srt_data = load_srt_from_file('subtitles.srt')
    # combine into full sentences
    sentences = combine_subs_into_sentences(srt_data)
    scenes = split_by_pauses(sentences, pause_length=4)
    # process using a LLM model via API
    for scene in scenes:
        response = model_request(scene['content'])
        print(response)
    pass


if __name__ == '__main__':
    run_all()
    pass

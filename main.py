from data_loading import load_srt_from_file
from model_api import get_summary, get_mood, get_speakers, get_references
from data_processing import combine_subs_into_sentences, split_by_pauses


def run_all():
    # load subtitle data from a .srt
    srt_data = load_srt_from_file('subtitles.srt')
    # combine into full sentences
    sentences = combine_subs_into_sentences(srt_data)
    scenes = split_by_pauses(sentences, pause_length=4)
    # process using a LLM model via API
    constructed_output = []
    for scene in scenes:
        # constructed_output.append(
        #     {
        #      "start": "00:00:22,719",
        #      "end": "00:00:31,507",
        #      "transcript": ,
        #      "summary": ,
        #      "characters": [],
        #      "mood": ,
        #      "cultural_refs": []
        #     })
        mood = get_mood(scene['content'])
        summary = get_summary(scene['content'])
        speakers = get_speakers(scene['content'])
        cultural_references = get_references(scene['content'])
        print(mood)
        pass
    pass


if __name__ == '__main__':
    run_all()
    pass

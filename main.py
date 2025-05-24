from data_loading import load_srt_from_file
from model_api import get_summary, get_mood, get_speakers, get_references
from data_processing import combine_subs_into_sentences, split_by_pauses, format_timedelta, extract_model_response


def run_all():
    # load subtitle data from a .srt
    srt_data = load_srt_from_file('subtitles.srt')
    # combine into full sentences
    sentences = combine_subs_into_sentences(srt_data)
    scenes = split_by_pauses(sentences, pause_length=4)

    # process using a LLM model via API
    constructed_output = []
    for i, scene in enumerate(scenes):
        mood = extract_model_response(get_mood(scene['content']))
        summary = extract_model_response(get_summary(scene['content']))
        speakers = extract_model_response(get_speakers(scene['content']))
        cultural_references = extract_model_response(get_references(scene['content']))
        constructed_output.append(
            {
             "start": format_timedelta(scene['start']),
             "end": format_timedelta(scene['end']),
             "transcript": scene['content'],
             "summary": summary,
             "characters": [speakers],
             "mood": mood,
             "cultural_refs": [cultural_references]
            })
        print(f'--- SCENE {i} {50*"-"}')
        print('summary: \t' + summary)
        print('mood: \t' + mood)
        print('speakers: \t' + speakers)
        print('cultural references: \t' + cultural_references)
        pass
    pass


if __name__ == '__main__':
    run_all()
    pass

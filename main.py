from data_loading import load_srt_from_file, store_json
from model_api import get_summary, get_mood, get_speakers, get_references
from data_processing import combine_subs_into_sentences, concat_by_pauses, format_timedelta, extract_model_response, \
    str_fmt_list, extract_mood

import argparse


def run_all():
    """Main function:

    1. load subtitle data from .srt file
    2. group by full sentences and scenes
    3. Use LLM to get: summary, mood, characters and cultural references
    4. store as .json formatted file
    """
    # parse arguments to get config params -> filename, model, output
    config_args = get_config_arguments()

    # load subtitle data from a .srt
    srt_data = load_srt_from_file(config_args.filename)
    # combine into full sentences
    sentences = combine_subs_into_sentences(srt_data)
    scenes = concat_by_pauses(sentences, pause_length=4)

    # process using a LLM model via API
    constructed_output = []
    for i, scene in enumerate(scenes):
        mood = extract_mood(extract_model_response(get_mood(scene['content'], model=config_args.model)))
        summary = extract_model_response(get_summary(scene['content'], model=config_args.model))
        speakers = str_fmt_list(extract_model_response(get_speakers(scene['content'], model=config_args.model)))
        cultural_references = str_fmt_list(extract_model_response(get_references(scene['content'], model=config_args.model)))
        constructed_output.append(
            {
                "start": format_timedelta(scene['start']),
                "end": format_timedelta(scene['end']),
                "transcript": scene['content'],
                "summary": summary,
                "characters": speakers,
                "mood": mood,
                "cultural_refs": cultural_references
            })
        print(f'--- SCENE {i} {50 * "-"}')
        print('summary:             \t' + str(summary))
        print('mood:                \t' + str(mood))
        print('speakers:            \t' + str(speakers))
        print('cultural references: \t' + str(cultural_references))
        store_json(constructed_output.copy(), exp_filename=config_args.output)
        pass
    pass


def get_config_arguments():
    """Parse arguments for configuration.

    :return: arguments: filename, model, output
    """
    parser = argparse.ArgumentParser(prog='SceneSage',
                                     description='LLM-powered Scene Analyzer')
    parser.add_argument('filename')
    parser.add_argument('-m', '--model')
    parser.add_argument('-o', '--output')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    run_all()
    pass

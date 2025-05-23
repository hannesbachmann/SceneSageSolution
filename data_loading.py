import srt


def load_srt_from_file(filename):
    with open(filename, 'r') as f:
        subs = srt.parse(f.read())
    subtitles = list(subs)
    contained_in_subs = [{'start': sub.start,
                          'end': sub.end,
                          'content': sub.content.replace('\n', ' ')} for sub in subtitles]
    return contained_in_subs


# if __name__ == '__main__':
#     load_srt_from_file('subtitles.srt')
#     pass
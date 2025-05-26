# SceneSageSolution
Programming Challenge: “SceneSage” — LLM-powered Scene Analyzer
_______________________________________________________________

## Description
This program will take a .srt subtitle file as input and group the subtitle snippets into scenes.
Each scene is then analysed using a LLM and extracts the following information. 
1. The dominant mood in the scene out of a defined set of basic moods.
2. Which characters are represented by the subtitles.
3. If there are any cultural references mentioned.
4. A summary of the scene. 

This will then be stored as a .json file together with the start- and end-time 
as well as the complete transcript for each scene. 

## Setup And Run Instruction
Before Starting the application, there are some requirements that need to be installed. \
To use an LLM, you need to download and install **Ollama** [[1]](#1) from the official page: \
https://ollama.com/download

After this is done, the preferred LLM can be pulled. \
I used one of the smaller versions of the **DeepSeek-R1** [[2]](#2) model with 14B parameters. \
This reasoning model from DeepSeek has a strong performance while also 
being free to use via an API. \
To download this model, you first need to open the commandline and type in: 

    ollama pull deepseek-r1:14b

This will download the 9.0GB large model. 

**Note:** \
Larger models like the 32b, 70b and 671b model supposedly give a better response. 
If the computer has problems handling such a large model, 
there are also smaller DeepSeek-R1 models available, like the 1.5b, 7b or 8b versions. \
A complete list of all available DeepSeek-R1 models can be found on: https://ollama.com/library/deepseek-r1

Also download the ollama as well as the srt python libraries. This can be done using pip.  

    pip install ollama
    pip install srt

Next the program can be started by using the command line: 

    python main.py subtitles.srt --model deepseek-r1:14b --output output_scenes.json

This generates a .json file containing the transcript and a summary, its start and end times, 
the dominant mood as well as eventual cultural references for each scene. \
The generated output stored in the defined .json file then looks like this.

    [
        {
        "start": "00:00:22,719", 
        "end": "00:01:24,435", 
        "transcript": "Greetings, my friend. ... from outer space?", 
        "summary": "The scene's speaker ... to uncover hidden truths for justice.", 
        "characters": ["Narrator"], 
        "mood": "Mysterious", 
        "cultural_refs": []
        }
    ]


## References
<a id="1">[1]</a>
Ollama web page: https://ollama.com/ \
Ollama github: https://github.com/ollama/ollama \
<a id="2">[2]</a> 
Guo, Daya, et al. \
Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. \
arXiv preprint arXiv:2501.12948 (2025)

_______________________________________________________________


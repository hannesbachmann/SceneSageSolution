# SceneSageSolution
Programming Challenge: “SceneSage” — LLM-powered Scene Analyzer
_______________________________________________________________

Before Starting the application, there are some requirements that need to be installed.
To use an LLM, you need to download Ollama from the official page: 
https://ollama.com/download

After this is done, the preferred LLM can be loaded.
I used one of the smaller versions of the DeepSeek-R1 model with 14B parameters.
This reasoning model from DeepSeek has a strong performance while also 
being free to use via an API. 
To download this model, you first need to open the commandline and type in: 

    ollama pull deepseek-r1:14b

This will download the 9.0GB large model.
Note: Larger models like the 32b, 70b and 671b model supposedly give a better response.
Also download the ollama as well as the srt python libraries. This can be done using pip. 

    pip install ollama
    pip install srt

Next the program can be started by using the command line:

    python main.py subtitles.srt --model deepseek-r1:14b --output output_scenes.json

This generates a .json file containing the transcript and a summary for each scene, its start and end times, 
the dominant mood as well as eventual cultural references.

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
_______________________________________________________________


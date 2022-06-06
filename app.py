import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_music(animal),
            temperature=0.6,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)



def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.


Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

def generate_music(topic):
    result = "generate a 20 line pop song that rhymes about " + topic

    example = """
    
    Topic: Teenage Dream

    Verse 1:
    You think I'm pretty without any makeup on
    You think I'm funny when I tell the punch line wrong
    I know you get me, so I let my walls come down, down
    Before you met me, I was alright
    But things were kinda heavy, you brought me to life
    Now every February, you'll be my Valentine, Valentine

    Chorus:
    You make me feel like I'm livin' a teenage dream
    The way you turn me on, I can't sleep
    Let's run away and don't ever look back
    Don't ever look back
    
    Verse 2:
    We drove to Cali and got drunk on the beach
    Got a motel and built a fort out of sheets
    I finally found you, my missing puzzle piece, I'm complete
    """

    print(result + "\n" + example)
    return example + "\n" + result
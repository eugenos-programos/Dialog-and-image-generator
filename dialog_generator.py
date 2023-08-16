from gradio_client import Client
from argparse import ArgumentParser
import pyttsx3


arg_parser = ArgumentParser(
    prog="Dialog Generator"
)

arg_parser.add_argument("-l", "--level", type=str, required=True, help="English proficiency level")
arg_parser.add_argument("-n", "--n-person", type=int, default=2, help="N person interacting")
arg_parser.add_argument("--topik", type=str, help="dialog topic")

args = arg_parser.parse_args()
topic = f"aboout {args.topik}" if args.topik is not None else ""
prompt = f"generate a dialog between {args.n_person} person in {args.level} English proficiency level" + topic

client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/")
result = client.predict(
                    prompt,
                    api_name="/chat")
print(result, end='\n__________________________________\n')


from gtts import gTTS

myobj = gTTS(text=result, lang='en', slow=False, tld='ie')
myobj.save("test.mp3")


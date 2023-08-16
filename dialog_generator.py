from gradio_client import Client


client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/")
for _ in range(5):
    result = client.predict(
                    "Generate a dialog between two persons in A1 English level",	# str in 'Message' Textbox component
                    api_name="/chat"
    )
    print(result, end='\n__________________________________\n')
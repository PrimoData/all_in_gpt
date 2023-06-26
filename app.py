import gradio as gr
from llama_index import StorageContext, load_index_from_storage


# Define a function that will process text input
def process_text(input_text):
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    return response


description = """The **"All-In" podcast** features four Silicon Valley investors: [Jason Calacanis](https://twitter.com/Jason) ("_The World's Greatest Moderator_"), 
[Chamath Palihapitiya](https://twitter.com/chamath) ("_The Dictator_"), [David Sacks](https://twitter.com/DavidSacks) ("_Rainman_"), and 
[David Friedberg]([https://twitter.com/friedberg) ("_The Sultan of Science_"), who discuss startups, investing, and current events every week.
The show has gained substantial popularity, featuring a catchy intro, no ads, and heated debates.

<div>
    <p style="margin: 0;">Listen to the podcast:    
        <a href="https://www.youtube.com/playlist?list=PLn5MTSAqaf8peDZQ57QkJBzewJU1aUokl" style="text-decoration: none;">
            <img style="display: inline; align-items: center;" src="https://cdn-icons-png.flaticon.com/16/1384/1384060.png" alt="YouTube icon" style="height: 16px; margin-right: 8px;">
        </a>
        <a href="https://podcasts.apple.com/us/podcast/all-in-with-chamath-jason-sacks-friedberg/id1502871393" style="text-decoration: none;">
            <img style="display: inline; align-items: center;" src="https://cdn-icons-png.flaticon.com/16/831/831299.png" alt="Apple Podcasts icon" style="height: 16px; margin-right: 8px;">
        </a>
        <a href="https://open.spotify.com/show/2IqXAVFR4e0Bmyjsdc8QzF" style="text-decoration: none;">
            <img style="display: inline; align-items: center;" src="https://cdn-icons-png.flaticon.com/16/174/174872.png" alt="Apple Podcasts icon" style="height: 16px; margin-right: 8px;">
        </a>        
    </p>
</div>
"""


# Create an Interface with a title, text input, and text output
iface = gr.Interface(
    fn=process_text,  # function that processes input
    inputs=gr.inputs.Textbox(
        lines=1,
        label="Ask about any topics they've covered on the pod.",
        placeholder="What's the latest on AI startups?",
    ),
    outputs=gr.inputs.Textbox(
        lines=1,
        label="AI Answer",
    ),
    title="All-In GPT",
    description=description,
    layout="vertical",
    allow_flagging="never",
    theme=gr.themes.Monochrome(),
)

# Launch the app
iface.launch()

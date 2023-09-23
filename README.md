# Interact with Your Documents powered with OpenAI
This project highlights how to leverage a ChromaDB vectorstore in a Langchain pipeline to create a GPT Investment Banker. You can load in a pdf based document and use it alongside an LLM without the need for fine tuning. 

## Startup 🚀
1. Create a virtual environment `python -m venv langchainenv`
2. Activate it: 
   - Windows:`.\langchainenv\Scripts\activate`
   - Mac: `source langchain/bin/activate`
3. Clone this repo `git clone https://github.com/karankk07/GPT-Investment-Banker`
4. Go into the directory `cd GPT-Investment-Banker`
5. Install the required dependencies `pip install -r requirements.txt`
6. Add your OpenAI APIKey to line 22 of `app.py`
7. Start the app `streamlit run app.py`

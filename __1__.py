import os
import pypdf
import requests
import parsel
from langchain_google_genai import ChatGoogleGenerativeAI as lcgai
from shiny import ui, reactive, render, App, run_app
from multiprocessing import Process, freeze_support

cwd = os.getcwd().replace("\\","/")

def _0_(_ip_):
    if(0):
        ...
    elif(_ip_.sip_file_url() == "Text File" and _ip_.ip_file_url().endswith("txt")):
        with open(_ip_.ip_file_url(), 'r') as f:
            ip = f.read()
    elif(_ip_.sip_file_url() == "PDF File" and _ip_.ip_file_url().endswith("pdf")):
        f = pypdf.PdfReader(_ip_.ip_file_url()).pages[:]
        ip = "".join([itr.extract_text() for itr in f])
    elif(_ip_.sip_file_url() == "HTML File [Web : URL]" and (_ip_.ip_file_url().startswith("http") or _ip_.ip_file_url().endswith("html"))):
        f = requests.get(_ip_.ip_file_url()).text
        ip = "".join(parsel.Selector(f, type="html").xpath("//body//text()").getall())
    elif(1):
        ip = None
    return(ip)


def _8_(_ip_, _op_, _p_):
    @_op_
    @render.text
    @reactive.event(_ip_.ip_ab_submit)
    def op_rag():
        ip = _0_(_ip_)
        if(ip != None):
            p = lcgai(google_api_key='Your_Key',model="gemini-pro",max_output_tokens=8888)
            op = p.invoke(f'{_ip_.ip_prompt} : {ip}').content.replace("**","")
        if(ip == None):
            op = "ERROR :: Invalid Input"
        return(op)
    ...

def _1_():
    return \
        ui.page_fluid(
            ui.include_css(f'{cwd}/8/CSC__03/__1__.css'),
            ui.input_select("sip_file_url",label="Select the type of input ::",choices=["Text File","PDF File","HTML File [Web : URL]"],selected="HTML File [Web : URL]"),
            ui.input_text("ip_file_url",label="Enter the file/URL ::",value="https://en.wikipedia.org/wiki/Data_science"),
            ui.input_text("ip_prompt",label="Enter the prompt ::",value="summarize the data"),
            ui.input_action_button("ip_ab_submit","RAG"),
            ui.HTML("<br>"),
            ui.output_text_verbatim("op_rag")
    )
    
_081_ = App(_1_(),_8_)


if __name__ == '__main__':
    freeze_support() # (optional)
    Process(target=run_app('__1__:_081_',reload=True)).start() # (required) ||  < (reload=True) :: for debugging >

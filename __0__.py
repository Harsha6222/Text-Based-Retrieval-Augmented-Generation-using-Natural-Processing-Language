import pypdf
import requests
import parsel
from langchain_google_genai import ChatGoogleGenerativeAI as lcgai


def func__ip():
    print(" = "*20)
    print("{:-^60}".format(" Input "))
    print("Select the type of input ::")
    print("\t1. Text File\n\t2. PDF File\n\t3. HTML File [Web : URL]")
    ip = int(input("[ip] Enter the type of input file [numeric] :: ") or '2')
    print(" - "*20)
    if(0):
        ...
    elif(ip == 1):
        ip = (input("[ip] Enter the path of the text file :: ") or '0/CSC__02/txt_wiki__DataScience.txt')
        with open(ip, 'r') as f:
            _p_ = f.read()
    elif(ip == 2):
        ip = (input("[ip] Enter the path of the pdf file :: ") or '0/CSC__02/pdf_wiki__DataScience.pdf')
        f = pypdf.PdfReader(ip).pages[:]
        _p_ = "".join([itr.extract_text() for itr in f])
    elif(ip == 3):
        ip = (input("[ip] Enter the url of the web page :: ") or 'https://en.wikipedia.org/wiki/Data_science')
        f = requests.get(ip).text
        _p_ = "".join(parsel.Selector(f, type="html").xpath("//body//text()").getall())
    else:
        ...
    print(" = "*20)
    print("{:-^60}".format(" Process "))
    print("[logs] :: `Processing ...`")
    func__op(io=_p_)


def func__p(io=' ',prompt=' '):
    _ip_ = io
    __p__ = lcgai(google_api_key='Your_Key',model="gemini-pro",max_output_tokens=8888)
    _op_ = __p__.invoke(f'{prompt} : {_ip_}')
    return _op_


def func__op(io=' '):
    print(" = "*20)
    print("{:-^60}".format(" Output "))
    ip = ''
    while(ip!='exit'):
        ip = input("[ip] Enter the prompt [`exit` to terminate] :: ") or 'exit'
        print(" - "*20)
        if(ip=='exit'):
            print("[logs] :: `Terminating ...`")
            continue
        _p_ = func__p(io=io,prompt=ip)
        for op in _p_:
            print(op[1])
            break
        print(" *-* "*20)
    print(" = "*20)


if(__name__ == '__main__'):
    func__ip()

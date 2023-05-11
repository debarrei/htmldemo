from dataclasses import dataclass
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)


@dataclass
class Article:
   title: str
   text: str
   image: str
   author: str
   published: str
   link: str
   
@app.route('/')
def index():
    article1=Article(title="TITLE1", text="BLABLABLA", image="https://mdbcdn.b-cdn.net/img/new/standard/city/044.webp", author="Ana Maria Doe", published="31/01/2023", link="https://www.msn.com/es-es/noticias/espana/una-inquilina-descuartiza-a-la-presidenta-de-su-comunidad-a-la-que-no-pagaba-el-alquiler/ar-AA189jY9?ocid=entnewsntp&cvid=4df087f23ab947f3b9b26fa2a5379f05&ei=9")
    article2=Article(title="TITLE2", text="NONOMONOM", image="https://mdbcdn.b-cdn.net/img/new/slides/041.webp", author="John Doe", published="02/05/2022", link="https://www.msn.com/es-es/noticias/espana/una-tuber%C3%ADa-en-badalona-pierde-180-000-litros-de-agua-cada-d%C3%ADa-desde-hace-15-a%C3%B1os/ar-AA189cOF?ocid=entnewsntp&cvid=4df087f23ab947f3b9b26fa2a5379f05&ei=18")
    article3=Article(title="TITLE3", text="LALALALAL", image="https://mdbcdn.b-cdn.net/img/new/fluid/city/055.webp", author="Layla Doe", published="15/11/2019", link="https://www.google.com/doodles")
    return render_template("/index.html", articles=[article1, article2, article3])


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os
load_dotenv()
dato_cms_key = os.getenv("DATOCMS_READ_API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    url = 'https://graphql.datocms.com/'
    query = '''
      query MyQuery {
        inicio {
          tituloHero
          heroDescripcion
        }
      }
    '''
    headers = {
        'Authorization': 'Bearer ' + dato_cms_key
    }
    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()

    return render_template('index.html', data=data["data"]["inicio"])


if __name__ == '__main__':
    app.run(debug=True)

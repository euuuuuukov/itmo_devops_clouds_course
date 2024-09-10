from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def main() -> str:
    return '''
    <html>
        <head>
            <title>itmo_devops_clouds_labs</title>
        </head>
        <body>
            <h1>Второе приложение</h1>
        </body>
    </html>
    '''

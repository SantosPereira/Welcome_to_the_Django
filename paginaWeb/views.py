from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(html)

html = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
    <style>

        @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&display=swap');

        body {
            color: rgb(204, 191, 189);
            background-color: black;
        }
        
        header {
            display: flex;
            flex-direction: row;
            align-content: center;
        }

        header h1 {
            font-family: 'Abril Fatface';
            font-size: 40px;
        }

    </style>
</head>
<body>
    <header>
        <h1>Ganso Rosa</h1>
    </header>
    <section>

    </section>
</body>
</html>
'''
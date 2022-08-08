import sys
sys.path.append("/PegarHtml.py")

header = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    *{
      font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    }
    body{
      background-color: #f6f6f9;
    }
    .container{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 30px
    }
    .container > div{
      font-size: 24px;
      color: #00BFFF;
      padding: 10px;
      text-align: center;
      height: 200px;
      border-radius: 20px;
      box-shadow: 0 2rem 3rem rgba(132, 139, 200, 0.38);
    }
    .container > div > h1{
      color: black;
    }
  </style>
</head>
<body>
"""

html_inicio = """
<div class="container">
"""
html_fim = """
</div>
<p>OBS: Os valores acima são considerados apenas para compra aprovadas</p>
</body>
</html>
"""
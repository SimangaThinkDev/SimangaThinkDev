from markdown import markdown
from click import secho
from pathlib import Path

with open( "README.md", "r" ) as f:
    readme = f.read()

content = markdown( readme )

secho( content, fg="green" )

with open( "index.html", "w" ) as page:
    page.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SimangaThinkDev</title>
</head>
<body>
{content}
</body>
</html>""")
    
    
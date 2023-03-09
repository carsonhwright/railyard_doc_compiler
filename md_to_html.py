import markdown

def main():
    with open('base_markdown.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open("output.html", 'w') as g:
        g.write(html)
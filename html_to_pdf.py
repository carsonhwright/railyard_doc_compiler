# import jinja2
import pdfkit
# from wkhtmltopdf.main import WKhtmlToPdf
from datetime import datetime


# my_name = "Frank Andrade"
# item1 = "TV"
# item2 = "Couch"
# item3 = "Washing Machine"
# today_date = datetime.today().strftime("%d %b, %Y")

# context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
#            'today_date': today_date}

# template_loader = jinja2.FileSystemLoader('./')
# template_env = jinja2.Environment(loader=template_loader)
# template = template_env.get_template("test.html")
# output text is the raw html we need to convert to pdf
# output_text = template.render(context)
# with open('output.html', 'w') as f:
#     f.write(output_text)
def main():
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_file("output.html", "output.pdf", configuration=config)


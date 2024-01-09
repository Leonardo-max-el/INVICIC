from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from html2docx import html2docx


# def render_to_pdf(tempplate_src,context_dict={}):
#     template = get_template(tempplate_src)
#     html=template.render(context_dict)
#     result=BytesIO()
#     pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(),content_type='application/pdf')
#     return None

def render_to_word(template_path, context):
    template = get_template(template_path)
    html_content = template.render(context)

    # Convertir HTML a Word
    word_file = BytesIO()
    html2docx(html_content, word_file)

    return word_file.getvalue()
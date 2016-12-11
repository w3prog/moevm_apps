# coding=utf-8
# from django.template.loader import get_template, Context
# import cStringIO
# import sx.pisa3 as pisa
#
#
# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html = template.render(context)
#     result = cStringIO.StringIO()
#     pdf = pisa.pisaDocument(cStringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='UTF-8')
#     if not pdf.err:
#         return result.getvalue()
#     return False

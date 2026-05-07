from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def generate_pdf(score, skills, suggestions):
    file_path = "report.pdf"
    doc = SimpleDocTemplate(file_path)

    content = []

    content.append(Paragraph(f"ATS Score: {score}%",))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Skills Found:",))
    content.append(Paragraph(", ".join(skills)))
    content.append(Spacer(1, 10))

    content.append(Paragraph("Suggestions:",))
    for s in suggestions:
        content.append(Paragraph(s))

    doc.build(content)

    return file_path

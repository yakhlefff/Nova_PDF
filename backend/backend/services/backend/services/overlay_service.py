import fitz

def add_text_overlay(input_pdf, output_pdf, text, x, y):
    doc = fitz.open(input_pdf)

    page = doc[0]

    page.insert_text(
        (x, y),
        text,
        fontsize=12
    )

    doc.save(output_pdf)

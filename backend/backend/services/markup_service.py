import fitz

def highlight_text(input_pdf, output_pdf, text):
    doc = fitz.open(input_pdf)

    for page in doc:
        text_instances = page.search_for(text)

        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.update()

    doc.save(output_pdf)

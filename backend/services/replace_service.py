import fitz

def replace_text(input_pdf, output_pdf, old_text, new_text):
    doc = fitz.open(input_pdf)

    for page in doc:
        text_instances = page.search_for(old_text)

        for inst in text_instances:
            page.add_redact_annot(inst)
            page.apply_redactions()
            page.insert_text(inst.tl, new_text)

    doc.save(output_pdf)

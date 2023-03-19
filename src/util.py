import xml.etree.ElementTree as ET
import zipfile
import regex as re

def get_skills(doc):
        myset = set()
        for ent in doc.ents:
            if ent.label_ == "SKILL":
                myset.add(ent.text)
        return myset

def doc2text(PATH: str):

    doc_zip = zipfile.ZipFile(PATH).read('word/document.xml')
    root = ET.fromstring(doc_zip)

    # Microsoft's XML makes heavy use of XML namespaces
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    body = root.find('w:body', ns)  # find the XML "body" tag
    p_sections = body.findall('w:p', ns)  # under the body tag, find all the paragraph sections

    # Extract all the text elements and append them to a list.
    doc_lines = []
    for p in p_sections:
        text_elems = p.findall('.//w:t', ns)
        doc_lines.append(''.join([t.text for t in text_elems]))

    # Merge all text elements into a string
    text_raw = '\n'.join(doc_lines)

    return text_raw

def clean(text_raw: str) -> str:
    text_clean = re.sub(
        r'[^\w\s]',
        ' ',
        text_raw,
    )
    text_clean = text_clean.lower()

    return text_clean

def compare(required_skills, input_resume):
        req_skills = [skill.lower() for skill in required_skills]
        resume_skills = get_skills(input_resume)
        score = 0
        for x in req_skills:
            if x in resume_skills:
                score += 1
        req_skills_len = len(req_skills)
        match = round(score / req_skills_len * 100, 1)

        return match
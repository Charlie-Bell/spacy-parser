import spacy
from src.util import doc2text, clean, compare


if __name__=="__main__":

    nlp = spacy.load('en_core_web_sm')

    ### Input the required skills and the resume path here:
    required_skills = ['Data Science','Data','SQL','NLP','Machine Learning','Pandas','Numpy']
    PATH = 'Charlie Bell CV.docx'
    ###

    # Create entity ruler
    ruler = nlp.add_pipe("entity_ruler")
    ruler.from_disk("jobzilla.jsonl")
    print("Entity ruler created.")

    # Preprocessing
    doc_raw = doc2text(PATH)
    doc_clean = clean(doc_raw)
    print("Data loaded and cleaned.")

    # Create the document object
    doc = nlp(doc_clean)
    print("Document object created.")
    
    # Compare the skills list to the resume document object
    input_resume = doc   
    match = compare(required_skills, input_resume)

    print(f"The current Resume is {match}% matched to your requirements")




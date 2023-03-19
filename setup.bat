py -3.10 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -U pip setuptools wheel
pip install -r requirements.txt
python -m spacy download en_core_web_sm
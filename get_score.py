import math
import re
from collections import Counter
import PyPDF2, pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# CV = 'Sivaranjini - Splunk Engineer.pdf'
# CV_File=open(CV,'rb')
def cv_to_text(CV_File):
    Script=PyPDF2.PdfReader(CV_File)
    pages=len(Script.pages)
    Script = []
    with pdfplumber.open(CV_File) as pdf:
        for i in range (0,pages):
            page=pdf.pages[i]
            text=page.extract_text()
            Script.append(text)
    return Script

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def get_match(CV_text, JD_text):
    vector1 = text_to_vector(CV_text[0])
    vector2 = text_to_vector(JD_text)

    cosine = get_cosine(vector1, vector2)
    cosine = round(cosine * 100)

    return cosine
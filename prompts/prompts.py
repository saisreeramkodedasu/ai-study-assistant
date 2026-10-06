def create_summary_prompt(pdf_text):
    
    return f"""
You are an AI Study Assistant.

Read the study material below and create a useful
study summary.

Give TWO sections:

SECTION 1: SHORT SUMMARY

Give 5 to 8 important bullet points.

SECTION 2: DETAILED SUMMARY

Explain the important concepts using:
- Headings
- Bullet points
- Simple explanations
- Important key points

Make the explanation useful for exam preparation.

Do not add information that is not present
in the uploaded document.

STUDY MATERIAL:

{pdf_text}
"""


def create_question_prompt(pdf_text, question):

    return f"""
You are an AI Study Assistant.

Answer the student's question using ONLY the
uploaded study material.

Explain the answer clearly and in a
student-friendly way.

If the answer cannot be found in the uploaded
study material, say:

"The information is not available in the uploaded PDF."

Do not invent or assume information.

STUDY MATERIAL:

{pdf_text}

STUDENT QUESTION:

{question}
"""


def create_voice_question_prompt(pdf_text, question):

    return f"""
You are an AI Study Assistant.

Answer the following question using ONLY the
uploaded PDF study material.

Give a clear and student-friendly explanation.

If the answer is not available in the PDF, say:

"The information is not available in the uploaded PDF."

Do not invent information.

STUDY MATERIAL:

{pdf_text}

QUESTION:

{question}
"""
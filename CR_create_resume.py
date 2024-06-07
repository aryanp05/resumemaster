from docx import Document
from docx.shared import Pt, Cm, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from CR_add_funcs import add_contact_info, add_education, add_experience, add_projects, add_sectionheader, add_technical_skills

para_spacing = 6
line_spacing = 14



def create_resume(input):
    document = Document()

    # Set margins
    left_marg = right_marg = 0.5
    document.sections[0].top_margin = Cm(1.11)
    document.sections[0].bottom_margin = Cm(0.73)
    document.sections[0].left_margin = Inches(left_marg)
    document.sections[0].right_margin = Inches(right_marg)
    
    # Set font size, font, and alignment for the name
    name_paragraph = document.add_paragraph()
    name_run = name_paragraph.add_run(input[0])
    name_run.bold = True
    name_run.font.size = Pt(24)
    name_run.font.name = 'Garamond'
    name_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    name_paragraph.paragraph_format.space_after = Pt(0)  # Remove space after paragraph
    

    add_contact_info(document, input[1])
  
    for sections in input[2]:
        add_sectionheader(document, sections[0])
        for parts in sections[2]:
            if sections[0] == "EDUCATION":
                sections[1](document, parts[0], parts[1], parts[2], parts[3], parts[4])
            if sections[0] == "EXPERIENCE":
                sections[1](document, parts[0], parts[1], parts[2], parts[3], parts[4])
            if sections[0] == "PROJECTS":
                sections[1](document, parts[0], parts[1], parts[2])
            if sections[0] == "TECHNICAL SKILLS":
                 sections[1](document, parts)
    
    document.save("JakeCV.docx")
    print("Resume created successfully!")




resume_array = [["Aryan Patel"], 
                ["aryan.patel2@uwaterloo.ca", "(437) 339-5154", "github.com/aryanp05", "linkedin.com/in/aryanpatel05"],
                [
                    [
                        "EDUCATION",
                        add_education,
                        [
                            ["The University of Waterloo", "April 2028", 
                            "Bachelors of Computer Science and Bachelors of Business Administration with 4.0 GPA", "Waterloo, ON", 
                            ["Relevant Coursework: Function Programing, Tools for Software Dev, Algorithm Design & Data Abstraction",
                            "Extracurricular: Hackathon Executive, Computer Science Club, Data Science Club"]]
                        ]
                    ],
                    [
                        "EXPERIENCE",
                        add_experience,
                        [
                            ["Software Developer & LLM Engineer", "A.P.U.G. Club", "Waterloo, ON",
                            "Sep. 2023 – March 2024", [
                            "Developed LooLearnAI  (), a student-focus AI software that assists in academics by answering content-specific questions using course conventions and generating practise material using OpenAI API, Milvus, and Python",
                            "Implemented sophisticated Natural Language Processing (NLP) techniques for semantic search and data vectorization, ensuring intuitive query understanding and resource discovery, to increase retrieval speed by 25%.",
                            "Employed streamlined deployment and consistent application performance using the tool Docker.",
                            "Used advanced Prompt Engineering to refine the AI insights into user queries and generating solutions and developed target algorithms including R.A.G. & R.S.E. to increase LooLearnAI answer accuracy from 78% to 93%"]],
                            
                            ["Software Developer", "Neonic Wraps", "Toronto, Ontarior",
                            "Sep. 2020 – Nov. 2021", [
                            "Designed and developed a fully functional and attractive e-commerce website using HTML, CSS, and JavaScript to increase customer conversion by 80%",
                            "Managed online inventory and performed database queries using SQL on MongoDB to effectively track items and orders",
                            "Operated an e-commerce business selling a diverse range of tech products, achieving $10k+ in sales."]]
                        
                        ]
                    ],
                    [
                        "PROJECTS",
                        add_projects,
                        [
                            ["Wildfire Path Predictor", "May 2024 – June 2024", [
                            "Engineered the Wildfire Path Predictor for the Wildfire AI Hackathon 2024, utilizing PyTorch and Torchvision to create a hybrid model combining CNNs and LSTMs, accurately predicting wildfire spread by processing spatial and temporal data from satellite imagery and climate variables.",
                            "Leveraged satellite data from MODIS, VIIRS, and IBAND to train AI models, incorporating fire weather data, enhancing wildfire prediction accuracy."]],
                            
                            ["GetTrash Garbage Identifier", "May 2024 – May 2024", [
                            "Created GetTrash, a web app leveraging Python, TensorFlow, and Streamlit for real-time waste sorting through live video scanning and image captioning, achieving third place at the Google Developer SC-hosted Hack With AI event.",
                            "Created a robust garbage classification model using TensorFlow, trained a CNN architecture and leveraging large online data sets of over 16,000+ photos to identify trash to a high accuracy"]],
                            
                            ["Meerkat ASL", "April 2024 – May 2024", [
                            "Developed a sign language interpreter with machine learning techniques and Scikit-Learn leveraging OpenCV to capture a dataset of over 40,000 images",
                            "Implemented a preprocessing pipeline to extract and preprocess hand landmarks using Mediapipe achieving efficient representation of sign language gestures for input into a neural network model"]]
                        ]
                    ],
                    [
                        "TECHNICAL SKILLS",
                        add_technical_skills,
                        [
                            ["Programming Languages", "Python, C++, C, HTML, CSS, JavaScript, Bash, Git, Racket, SQL"],
                            ["Technologies", "Flask, OpenCV, Tensorflow, PyTorch, Docker, Kubernetes, Git, Milvus, Rasterio, Streamlit"]
                        ]
                    ]

                ]
            ]

create_resume(resume_array)
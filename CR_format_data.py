from CR_create_resume import create_resume
from CR_add_funcs import add_education, add_experience, add_projects, add_sectionheader, add_technical_skills

def format_resume(person_name, contact_info, education, experience, projects, skills):
    resume = []
    resume.append([person_name, "Garamond", 24])
    resume.append(contact_info)
    resume_info = []
    section_info = []
    part_info = []


    section_info.append(["EDUCATION", "Garamond", [12, 11, 10]])
    section_info.append(add_education)
    for edu in education:
        part_info.append(edu[:4] + [edu[4:]])
    section_info.append(part_info)
    resume_info.append(section_info)
    section_info = []
    part_info = []

    section_info.append(["EXPERIENCE", "Garamond", [12, 11, 10]])
    section_info.append(add_experience)
    for exp in experience:
        part_info.append(exp[:4] + [exp[4:]])
    section_info.append(part_info)
    resume_info.append(section_info)
    section_info = []
    part_info = []

    section_info.append(["PROJECTS", "Garamond", [12, 11, 10]])
    section_info.append(add_projects)
    for pro in projects:
        part_info.append(pro[:2] + [pro[2:]])
    section_info.append(part_info)
    resume_info.append(section_info)
    section_info = []
    part_info = []

    section_info.append(["TECHNICAL SKILLS", "Garamond", [12, 11, 10]])
    section_info.append(add_technical_skills)
    for skill in skills:
        part_info.append(skill)
    section_info.append(part_info)
    resume_info.append(section_info)
    section_info = []
    part_info = []

    resume_info.append
    resume.append(resume_info)
    print(resume)
    create_resume(resume)


def skill_gap(skills):

    required = [
        "Python",
        "SQL",
        "Tableau",
        "Power BI"
    ]

    missing = []

    for skill in required:
        if skill not in skills:
            missing.append(skill)

    return missing
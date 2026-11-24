class Student():
    def __init__(self, name, section, spanish_grade, english_grade, social_studies_grade, science_grade):
        self.name = name
        self.section = section
        self.spanish_grade=spanish_grade
        self.english_grade=english_grade
        self.social_studies_grade=social_studies_grade
        self.science_grade=science_grade

    def get_average(self):
        return (self.spanish_grade+self.english_grade+self.social_studies_grade+self.science_grade)/4


    def to_dict(self):
        return {
            "name": self.name,
            "class": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_studies_grade": self.social_studies_grade,
            "science_grade": self.science_grade,
            }

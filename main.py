class ResumeAnalyzer:

    REQUIRED_SKILLS = {
        "python": 25,
        "git": 15,
        "github": 10,
        "ai": 25,
        "api": 15,
        "sql": 10
    }

    def __init__(self):
        self.score = 0
        self.detected_skills = []
        self.missing_skills = []

    def analyze_skills(self, skills):

        for skill, points in self.REQUIRED_SKILLS.items():

            if skill in skills:
                self.score += points
                self.detected_skills.append(skill)

            else:
                self.missing_skills.append(skill)

    def analyze_projects(self, projects):

        if projects >= 10:
            self.score += 25

        elif projects >= 5:
            self.score += 15

        elif projects >= 1:
            self.score += 5

    def get_level(self):

        if self.score >= 90:
            return "EXPERT"

        elif self.score >= 70:
            return "ADVANCED"

        elif self.score >= 50:
            return "INTERMEDIATE"

        return "BEGINNER"

    def get_recommendation(self):

        if self.score >= 90:
            return "Ready for internships, freelance work and startup projects."

        elif self.score >= 70:
            return "Strong profile. Build more projects and improve portfolio."

        elif self.score >= 50:
            return "Keep learning and increase project count."

        return "Focus on Python, Git, GitHub and project building."

    def generate_report(self, name, skills, projects):

        print("\n" + "=" * 60)
        print("AI RESUME ANALYSIS REPORT")
        print("=" * 60)

        print(f"Candidate Name : {name}")
        print(f"Projects Built : {projects}")
        print(f"ATS Score      : {self.score}/100")
        print(f"Level          : {self.get_level()}")

        print("\nDETECTED SKILLS")
        print("-" * 60)

        if self.detected_skills:
            for skill in self.detected_skills:
                print(f"✅ {skill.title()}")

        print("\nMISSING SKILLS")
        print("-" * 60)

        if self.missing_skills:
            for skill in self.missing_skills:
                print(f"❌ {skill.title()}")

        print("\nRECOMMENDATION")
        print("-" * 60)
        print(self.get_recommendation())

        print("=" * 60)


def get_user_input():

    print("=" * 60)
    print("AI Resume Analyzer Pro")
    print("=" * 60)

    name = input("Enter your name: ")

    skills = input(
        "Enter skills (comma separated): "
    ).lower()

    skills = [skill.strip() for skill in skills.split(",")]

    while True:

        try:
            projects = int(
                input("How many projects have you built? ")
            )

            if projects < 0:
                print("Projects cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    return name, skills, projects


def main():

    name, skills, projects = get_user_input()

    analyzer = ResumeAnalyzer()

    analyzer.analyze_skills(skills)

    analyzer.analyze_projects(projects)

    analyzer.generate_report(
        name,
        skills,
        projects
    )


if __name__ == "__main__":
    main()
print("=== AI Resume Analyzer V3 ===")

name = input("Enter your name: ")
skills = input("Enter your skills (comma separated): ")
projects = int(input("How many projects have you built? "))

print("\nResume Analysis")
print("----------------")

score = 0

if "python" in skills.lower():
    score += 35

if "git" in skills.lower():
    score += 30

if "ai" in skills.lower():
    score += 35

if projects >= 5:
    score += 20
elif projects >= 2:
    score += 10

print(f"Candidate: {name}")
print(f"Resume Score: {score}/120")

if score >= 90:
    print("🏆 Advanced")
elif score >= 60:
    print("🚀 Intermediate")
else:
    print("📚 Beginner")

print("\nRecommendations:")

if "python" not in skills.lower():
    print("- Learn Python")

if "git" not in skills.lower():
    print("- Learn Git")

if "ai" not in skills.lower():
    print("- Learn AI Fundamentals")

if projects < 5:
    print("- Build more projects")

print("\nAnalysis Complete!")
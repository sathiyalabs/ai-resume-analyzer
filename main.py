print("=== AI Resume Analyzer ===")

name = input("Enter your name: ")
skills = input("Enter your skills (comma separated): ")

print("\nResume Analysis")
print("----------------")
print(f"Candidate: {name}")
print(f"Skills: {skills}")

if "python" in skills.lower():
    print("✅ Python skill detected")
else:
    print("❌ Add Python to improve opportunities")

print("Analysis Complete!")
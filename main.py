print("=== AI Resume Analyzer V2 ===")

name = input("Enter your name: ")
skills = input("Enter your skills (comma separated): ")

print("\nResume Analysis")
print("----------------")

print(f"Candidate: {name}")
print(f"Skills: {skills}")

score = 0

if "python" in skills.lower():
    print("✅ Python skill detected")
    score += 35
else:
    print("❌ Add Python to improve opportunities")

if "git" in skills.lower():
    print("✅ Git skill detected")
    score += 30
else:
    print("❌ Learn Git")

if "ai" in skills.lower():
    print("✅ AI skill detected")
    score += 35
else:
    print("❌ Learn AI fundamentals")

print(f"\nResume Score: {score}/100")

if score >= 80:
    print("🏆 Level: Advanced")
elif score >= 50:
    print("🚀 Level: Intermediate")
else:
    print("📚 Level: Beginner")

print("\nAnalysis Complete!")
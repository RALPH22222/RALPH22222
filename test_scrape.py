import urllib.request
import re

USERNAME = 'RALPH22222'

# 1. Test Streak Stats
try:
    req = urllib.request.Request(f"https://streak-stats.demolab.com?user={USERNAME}", headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    print("Streak Stats length:", len(html))
    numbers = re.findall(r'>([\d,]+)<', html)
    print("All numbers found in Streak:", numbers)
except Exception as e:
    print("Error streaks:", e)

# 2. Test Lines of Code
try:
    req2 = urllib.request.Request(f"https://github-readme-stats.vercel.app/api?username={USERNAME}&show=lines_of_code", headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req2) as response:
        html2 = response.read().decode('utf-8')
    print("Readme stats length:", len(html2))
    
    # Try finding lines of code string
    text_tags = re.findall(r'>([^<]+)<', html2)
    clean_tags = [t.strip() for t in text_tags if t.strip()]
    print("Readme stats tags:", clean_tags)
except Exception as e:
    print("Error LOC:", e)

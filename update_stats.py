import os
import requests
from lxml import etree

# Ensure GitHub token is available
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
USERNAME = 'RALPH22222'

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set.")
    exit(1)

HEADERS = {'Authorization': f'bearer {GITHUB_TOKEN}'}

def fetch_github_stats():
    """Fetches user stats and calculates streaks using GitHub GraphQL API"""
    query = """
    query {
        viewer {
            followers { totalCount }
            repositories(first: 1, ownerAffiliations: OWNER, isFork: false) {
                totalCount
            }
            repositoriesContributedTo(first: 1, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) {
                totalCount
            }
            contributionsCollection {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            contributionCount
                            date
                        }
                    }
                }
            }
        }
    }
    """
    
    response = requests.post(
        'https://api.github.com/graphql', 
        json={'query': query}, 
        headers=HEADERS
    )
    
    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code}. {response.text}")
        
    json_response = response.json()
    if 'errors' in json_response:
        raise Exception(f"GraphQL returned errors: {json_response['errors']}")
        
    data = json_response['data']['viewer']
    
    # Calculate totals
    followers = data['followers']['totalCount']
    repos = data['repositories']['totalCount']
    contributed = data['repositoriesContributedTo']['totalCount']
    calendar = data['contributionsCollection']['contributionCalendar']
    commits = calendar['totalContributions']
    
    # Calculate streaks natively
    import datetime
    current_streak = 0
    longest_streak = 0
    current_streak_temp = 0
    
    today = datetime.datetime.now().date()
    
    # Flatten days
    all_days = []
    for week in calendar['weeks']:
        for day in week['contributionDays']:
            all_days.append(day)
            
    # Calculate longest streak
    for day in all_days:
        if day['contributionCount'] > 0:
            current_streak_temp += 1
            if current_streak_temp > longest_streak:
                longest_streak = current_streak_temp
        else:
            current_streak_temp = 0
            
    # Calculate current streak (counting backwards from today or yesterday)
    all_days.reverse()
    found_today = False
    for day in all_days:
        day_date = datetime.datetime.strptime(day['date'], "%Y-%m-%d").date()
        if day_date > today:
            continue
        
        # If today has 0, we check yesterday. If yesterday has 0, streak is 0.
        if day_date == today and day['contributionCount'] == 0:
            continue
            
        if day['contributionCount'] > 0:
            current_streak += 1
        else:
            break
    
    return {
        'followers_data': f"{followers:,}",
        'repos_data': f"{repos:,}",
        'contributed_data': f"{contributed:,}",
        'commits_data': f"{commits:,}",
        'current_streak_data': str(current_streak),
        'longest_streak_data': str(longest_streak)
    }

def fetch_external_stats(stats):
    """Scrapes Profile Views, Streak Stats, and Lines of Code"""
    import re
    # Profile Views
    try:
        r = requests.get(f"https://komarev.com/ghpvc/?username={USERNAME}")
        matches = re.findall(r'>([\d,]+)<', r.text)
        if matches:
            stats['views_data'] = matches[-1]
    except:
        stats['views_data'] = "N/A"

        
    return stats

def update_svg(filename, stats):
    """Updates the SVG file with the provided stats"""
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found.")
        return
        
    tree = etree.parse(filename)
    root = tree.getroot()
    
    for key, value in stats.items():
        element = root.find(f".//*[@id='{key}']")
        if element is not None:
            element.text = value
            
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Updated {filename} successfully.")

if __name__ == "__main__":
    try:
        print("Fetching stats from GitHub...")
        stats = fetch_github_stats()
        stats = fetch_external_stats(stats)
        print(f"Stats fetched: {stats}")
        
        update_svg('light_mode.svg', stats)
        update_svg('dark_mode.svg', stats)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

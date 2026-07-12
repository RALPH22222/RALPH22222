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
    """Fetches user stats using GitHub GraphQL API"""
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
    commits = data['contributionsCollection']['contributionCalendar']['totalContributions']
    
    return {
        'followers_data': f"{followers:,}",
        'repos_data': f"{repos:,}",
        'contributed_data': f"{contributed:,}",
        'commits_data': f"{commits:,}"
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

    # Streaks
    try:
        r = requests.get(f"https://streak-stats.demolab.com?user={USERNAME}")
        matches = re.findall(r'<text.*?class="stat.*?>([\d,]+)</text>', r.text)
        if len(matches) >= 3:
            stats['current_streak_data'] = matches[1]
            stats['longest_streak_data'] = matches[2]
        else:
            # Fallback if class changes
            numbers = re.findall(r'>([\d,]+)<', r.text)
            # Filter out years or small elements if any, but usually the 3 big stats are here
            numbers = [n for n in numbers if len(n) < 10]
            if len(numbers) >= 3:
                stats['current_streak_data'] = numbers[1]
                stats['longest_streak_data'] = numbers[2]
            else:
                stats['current_streak_data'] = "N/A"
                stats['longest_streak_data'] = "N/A"
    except:
        stats['current_streak_data'] = "N/A"
        stats['longest_streak_data'] = "N/A"

    # Lines of Code
    try:
        r = requests.get(f"https://github-readme-stats.vercel.app/api?username={USERNAME}&show=lines_of_code")
        # Try finding LOC next to its label
        matches = re.search(r'Lines of Code.*?([\d,]+)', r.text, re.IGNORECASE | re.DOTALL)
        if matches:
            stats['loc_data'] = matches.group(1)
        else:
            # Fallback: github-readme-stats usually has numbers in text tags
            numbers = re.findall(r'>([\d,]+)<', r.text)
            if numbers:
                # the highest number is usually lines of code if included
                stats['loc_data'] = sorted(numbers, key=lambda x: int(x.replace(',', '')))[-1]
    except:
        stats['loc_data'] = "N/A"
        
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

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
    query($login: String!) {
        user(login: $login) {
            followers { totalCount }
            repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
                totalCount
                nodes {
                    stargazers { totalCount }
                }
            }
            contributionsCollection {
                contributionCalendar {
                    totalContributions
                }
            }
        }
    }
    """
    
    variables = {'login': USERNAME}
    
    response = requests.post(
        'https://api.github.com/graphql', 
        json={'query': query, 'variables': variables}, 
        headers=HEADERS
    )
    
    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code}. {response.text}")
        
    data = response.json()['data']['user']
    
    # Calculate totals
    followers = data['followers']['totalCount']
    repos = data['repositories']['totalCount']
    commits = data['contributionsCollection']['contributionCalendar']['totalContributions']
    
    # Sum up stars from all repositories
    stars = sum(node['stargazers']['totalCount'] for node in data['repositories']['nodes'])
    
    return {
        'followers_data': f"{followers:,}",
        'repos_data': f"{repos:,}",
        'commits_data': f"{commits:,}",
        'stars_data': f"{stars:,}"
    }

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
        print(f"Stats fetched: {stats}")
        
        update_svg('light_mode.svg', stats)
        update_svg('dark_mode.svg', stats)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

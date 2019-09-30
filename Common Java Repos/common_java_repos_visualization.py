import requests
from plotly import offline
from plotly.graph_objs import Bar


url = "https://api.github.com/search/repositories?q=language:java&sort=stars"

# Get a request object, store it in r
r = requests.get(url)
# Put the response object into a json format -- dictionary in python
response_dicts = r.json()
# Get a dictionary of items
repo_dicts = response_dicts['items']

repo_name, owners, stars, git_url = [], [], [], []
for repo_dict in repo_dicts:
    # Get the name, stars, owner, and url to the repo.
    name = repo_dict['name']
    owner = repo_dict['owner']['login']
    starred = repo_dict['stargazers_count']
    repo_url = repo_dict['html_url']
    repos_url = f"<a href='{repo_url}'>{name}</a>"

    repo_name.append(name)
    owners.append(owner)
    stars.append(starred)
    git_url.append(repos_url)

# Customizes how the chart will look
data = [{
    'type': 'bar',
    'hovertext': repo_name,
    'x': git_url,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 60, 60)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
}]

# Sets the layout for the plot
my_layout = {
    'title': 'Most-Starred Java Projects on GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='java_repos.html')


import requests
response = requests.get("https://api.github.com/users/avielb/repos")
result = []
#List of repositories in git hub

result = [repo["ssh_url"] for repo in response.json()]
print(result)
repo_with_first = [repo["full_name"] for repo in response.json() if "first" in repo["full_name"]]
print(f"Only first:\n{repo_with_first}")
private_repo = [repo["full_name"] for repo in response.json() if False == repo["private"]]
print(f"Private repo:\n{private_repo}")

dict_repo = [{"name": repo["full_name"], "tags": repo["git_tags_url"]} for repo in response.json()]
print(f"Git tags url:\n{dict_repo}")




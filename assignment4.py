"""
    Student Name: Limor Segal Shevah
    Assignment: No. 4
"""
import requests
import names
from selenium import webdriver

REST_API_SUCCESS_RESPONSE = 200
REPOS_URL = "https://api.github.com/users/avielb/repos"
WORLD_UNIVERSITIES_URL = "http://universities.hipolabs.com/search?country="
Y_COMBINATOR_URL = "https://www.ycombinator.com/"
HUB_DOCKER_URL = "https://hub.docker.com"

# API Testing
# Ex .1 (Testing Github API)


def check_repos_num_exists(num_of_repos):
    try:
        repo_response = requests.get(REPOS_URL)
        if REST_API_SUCCESS_RESPONSE == repo_response.status_code:
            assert len(repo_response.json()) >= num_of_repos
            print(f"At  least {num_of_repos} git repositories exists in {REPOS_URL}")
    except TypeError as e1:
        print(f"Type Error Exception occurred (wrong parameter type), see more details here: {e1.args}")


check_repos_num_exists(5)


# Ex .2 (Testing agify API)
legal_age_range = range(0, 120)
for i in range(3):
    response = requests.get(f"https://api.agify.io/?name={names.get_first_name()}")
    if REST_API_SUCCESS_RESPONSE == response.status_code:
        res_json_object = response.json()
        print(f"Name: {res_json_object['name']}, Age: {res_json_object['age']}")
        assert res_json_object['age'] in legal_age_range


# Ex .3 (Testing universities API)
def check_country_universities_num_exists(num_of_universities, country):
    try:
        universities_response = requests.get(f"{WORLD_UNIVERSITIES_URL}{country}")
        if REST_API_SUCCESS_RESPONSE == universities_response.status_code:
            assert len(universities_response.json()) >= num_of_universities
            print(f"At  least {num_of_universities} universities exists in {WORLD_UNIVERSITIES_URL}{country}")
    except TypeError as e:
        print(f"Type Error Exception occurred (wrong parameter type), see more details here: {e.args}")


check_country_universities_num_exists(5, "Israel")


# UI Testing 4 + 5
def check_web_title(url, expected_result):
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    actual_result = my_driver.title
    my_driver.close()
    assert actual_result == expected_result


check_web_title(Y_COMBINATOR_URL, "Y Combinator")
# The real value is:'Docker Hub Container Image Library | App Containerization'
check_web_title(HUB_DOCKER_URL, "Container Image Library | App Containerization")

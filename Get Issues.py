#from jira import JIRA
from atlassian import Jira
from credentials import username, password

# Jira server URL and credentials
jira_server = "https://planday.atlassian.net"


# Connect to Jira
#jira = Jira(url=jira_server, basic_auth=(username, password))


jira = Jira(
    url=jira_server,
    username=username,
    password=password,
    cloud=True)

jql_request = 'project = AGIL AND status NOT IN (DONE, Rejected) ORDER BY issuekey'
issues = jira.jql(jql_request)

print(type(issues))
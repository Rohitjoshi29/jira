
from jira import JIRA
from credentials import username, password

# Jira server URL and credentials
jira_server = "https://planday.atlassian.net"

# Hardcoded list of board IDs  -- Team Agile - 321,
board_ids = [224, 343, 387, 388, 384, 233, 428, 514, 471]  # Replace with your board IDs

sprint_list = [] 

# Connect to Jira
jira = JIRA(server=jira_server, basic_auth=(username, password))

# Function to get active sprints for a board by ID
def get_active_sprints(board_id):
    sprints = jira.sprints(board_id=board_id, state='active')
    return sprints

# Iterate through the list of board IDs
for board_id in board_ids:
    if board_id is not None:
        # Get the active sprints for the board
        sprints = get_active_sprints(board_id)
        
        # Check if there are active sprints
        if sprints:
            # Print header row
            # print("Sprint Name, Sprint Goal")
            
            for sprint in sprints:
                sprint_id = sprint.id
                sprint_goal = sprint.goal
                sprint_name = sprint.name
                print(f"{sprint_name}\n{sprint_goal}\n\n")
                #print(f"{sprint_name}| {sprint_goal}")

                sprint_info = jira.sprint_info (board_id, sprint_id)

                sprint_list.append(sprint_id)
                #print (sprint_info)
        else:
            print("No active sprints found.")
    else:
        print(f"No board found with the ID '{board_id}'")

sprint_list = list(set(sprint_list))

print(sprint_list)
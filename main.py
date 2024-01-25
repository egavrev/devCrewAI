from crewai import Crew
from devCrewAIAgents import devCrewAIAgents
from devCrewAITasks import devCrewTasks

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

#from dotenv import load_dotenv
#load_dotenv()


class devCrewRun:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = devCrewAIAgents()
        tasks = devCrewTasks()

        # Definitions of agents
        POAgent = agents.ProductManager(var1)
        BAAgent = agents.BusinessAnalyst(var1)
        UIUXAgent = agents.UI_UX_Designer(var1)
        DBAAgent = agents.DatabaseAdministrator(var1)
        TAAgent = agents.TechnicalArchitect(var1)
        DevAgent = agents.Developer(var1)

        # Definition of tasks using previously defined functions
        POTask = tasks.create_Product_Owner_requirements(
            POAgent,
            var1,  # Assuming var1 and var2 are accessible in this scope
            var2,
        )

        BATask = tasks.create_BA_user_stories(
            BAAgent,
            var1,
            var2,
        )

        UIUXTAsk = tasks.create_UIUX_Design_specs(
            UIUXAgent,
            var1,
            var2,
        )

        DBATask = tasks.create_DBA_DB_structure(
            DBAAgent,
            var1,
            var2,
        )

        TATask = tasks.create_Technical_Architect_blueprint(
            TAAgent,
            var1,
            var2,
        )

        DevTask = tasks.create_Developer_implementation_plan(
            DevAgent,
            var1,
            var2,
        )

        # Aggregating all agents and their tasks
        agents_list = [POAgent, BAAgent, UIUXAgent, DBAAgent, TAAgent, DevAgent]
        tasks_list = [POTask, BATask, UIUXTAsk, DBATask, TATask, DevTask]

        # Define your custom crew here, encapsulating all roles and tasks
        crew = Crew(
            agents=agents_list,
            tasks=tasks_list,
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    
    var1= "create an tool for story telling"
    var2="it shoudld wirte sotry for kids"
    dev_crew = devCrewRun(var1, var2)
    result = dev_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
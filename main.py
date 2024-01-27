from crewai import Crew
from devCrewAIAgents import devCrewAIAgents
from devCrewAITasks import devCrewTasks

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

#from dotenv import load_dotenv
#load_dotenv()

        #tasks : 
        #1. make an flow with definet format of output from all steps:
        #from 1st Requirements, Tech description
        #from ERD DB config and user stores for back and frontend, ux design description
        #from 3rd generate files of code with specific fies
        #save files and run code to see


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
        #define agents fro first step to build requirements and backlog.
        agents_list_1 = [POAgent, BAAgent]
        tasks_list_1 = [POTask, BATask]

        # Define your custom crew here, encapsulating all roles and tasks
        crew_1 = Crew(
            agents=agents_list_1,
            tasks=tasks_list_1,
            verbose=True,
        )

        result_1 = crew_1.kickoff()


        UIUXTAsk = tasks.create_UIUX_Design_specs(
            UIUXAgent,
            var1,
            result_1,
        )


        TATask = tasks.create_Technical_Architect_blueprint(
            TAAgent,
            var1,
            result_1,
        )

        agents_list_2 = [UIUXAgent, TAAgent]
        tasks_list_2 = [UIUXTAsk,  TATask]

        # Define your custom crew here, encapsulating all roles and tasks
        crew_2 = Crew(
            agents=agents_list_2,
            tasks=tasks_list_2,
            verbose=True,
        )

        result_2 = crew_2.kickoff()

        DevTask = tasks.create_Developer_implementation_plan(
            DevAgent,
            result_1,
            result_2,
        )

        DBATask = tasks.create_DBA_DB_structure(
            DBAAgent,
            result_1,
            result_2,
        )
        # Aggregating all agents and their tasks
        agents_list_3 = [ DBAAgent,DevAgent]
        tasks_list_3 = [DBATask,DevTask]

        # Define your custom crew here, encapsulating all roles and tasks
        crew_3 = Crew(
            agents=agents_list_3,
            tasks=tasks_list_3,
            verbose=True,
        )

        result_3 = crew_3.kickoff()
        return result_3


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    
    var1= "Сreate an simple story telling app for kids"
    var2="""it should have just on screen, where you select an topic - whther is about honesty, bravery etc, 
    as well as setup where it is happening - in robo-city in jungle, 
    tool will generate title image and text for kids each time it should try to generate new story
    as AI model you can use OpenAI API"""
    dev_crew = devCrewRun(var1, var2)
    result = dev_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
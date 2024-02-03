from crewai import Crew
from devCrewAIAgents import devCrewAIAgents
from devCrewAITasks import devCrewTasks

if __name__ == "__main__":
    #idea varirable rad from file idea.txt 
    idea = open("idea.txt", "r")
    var1 = idea.read()
    idea.close()
    
    agents = devCrewAIAgents()
    tasks = devCrewTasks()

    # Define your agents and tasks here
    conceptualizer = agents.conceptualizer_agent()
    conceptualizer_task = tasks.task_for_conceptualizer(conceptualizer, var1)
    crew = Crew(agent=[conceptualizer], tasks=[conceptualizer_task], verbose=True)
    result = crew.kickoff()
    
    analyst = agents.analyst_agent()
    analyst_task = tasks.task_for_analyst(analyst, result)
    crew = Crew(agents=[analyst], tasks=[analyst_task], verbose=True)
    result = crew.kickoff()

    architect = agents.architect_agent()
    architect_task = tasks.task_for_architect(architect, result)
    crew = Crew(agents=[architect], tasks=[architect_task], verbose=True)
    result = crew.kickoff()

    planner = agents.planner_agent()
    planner_task = tasks.task_for_planner(planner, result)
    crew = Crew(agents=[planner], tasks=[planner_task], verbose=True)
    result = crew.kickoff()

    backend_builder = agents.builder_agent('Backend')
    backend_builder_task = tasks.task_for_builder(backend_builder, result)
    crew = Crew(agents=[backend_builder], tasks=[backend_builder_task], verbose=True)
    result = crew.kickoff()

    frontend_builder = agents.builder_agent('Frontend')
    frontend_builder_task = tasks.task_for_builder(frontend_builder, result)
    crew = Crew(agents=[frontend_builder], tasks=[frontend_builder_task], verbose=True)
    result = crew.kickoff()

    devops_builder = agents.builder_agent('DevOps')
    devops_builder_task = tasks.task_for_builder(devops_builder, result)
    crew = Crew(agents=[devops_builder], tasks=[devops_builder_task], verbose=True)
    result = crew.kickoff()


    results = dev_crew.run(agent_task_list)

    print("\n\n########################")
    print("## Here are your custom crew run results:")
    print("########################\n")
    for result in results:
        print(result)
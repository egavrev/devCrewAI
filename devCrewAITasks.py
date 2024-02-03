from crewai import Task
from langchain_community.llms import OpenAI
  

class devCrewTasks():
  ### For the Product Owner
    def task_for_conceptualizer(self,agent, idea):
        return Task(
            description=f"Refine and elaborate on this idea to create a clear, innovative software solution concept: {idea}",
            agent=agent
        )

    def task_for_analyst(self,agent, concept_document):
        return Task(
            description=f"Based on the conceptualized solution, create detailed technical specifications and user stories: {concept_document}",
            agent=agent
        )

    def task_for_architect(self, agent, requirements_document):
        return Task(
            description=f"Design the high-level architecture and select the technology stack based on these requirements: {requirements_document}",
            agent=agent
        )

    def task_for_planner(self, agent, architectural_design):
        return Task(
            description=f"Create a comprehensive project plan, including development roadmap, sprints, and tasks based on: Technical specifications - {architectural_design}",
            agent=agent
        )

    def task_for_builder(self, agent,role_specific_details):
        return Task(
            description=f"Implement the component of the application as outlined in the project plan. Focus on {role_specific_details}",
            agent=agent
        )

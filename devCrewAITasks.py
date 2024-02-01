from crewai import Task
from langchain_community.llms import OpenAI
  

class devCrewTasks():
  ### For the Product Owner
    def task_for_conceptualizer(agent, idea):
        return Task(
            description=f"Refine and elaborate on this idea to create a clear, innovative software solution concept: {idea}",
            agent=agent
        )

    def task_for_analyst(agent, concept_document):
        return Task(
            description=f"Based on the conceptualized solution, create detailed technical specifications and user stories: {concept_document}",
            agent=agent
        )

    def task_for_architect(agent, requirements_document):
        return Task(
            description=f"Design the high-level architecture and select the technology stack based on these requirements: {requirements_document}",
            agent=agent
        )

    def task_for_planner(agent, technical_specifications, architectural_design):
        return Task(
            description=f"Create a comprehensive project plan, including development roadmap, sprints, and tasks based on: Technical specifications - {technical_specifications}, Architectural design - {architectural_design}",
            agent=agent
        )

    def task_for_builder(agent, project_plan, role_specific_details):
        return Task(
            description=f"Implement the component of the application as outlined in the project plan. Focus on {role_specific_details}",
            agent=agent
        )

    def task_for_tester(agent, application_code):
        return Task(
            description="Conduct comprehensive tests on this codebase, identifying any bugs or performance issues",
            agent=agent
        )

    def task_for_reviewer(agent, application_code):
        return Task(
            description="Review the codebase for optimization opportunities and coding standard adherence",
            agent=agent
        )
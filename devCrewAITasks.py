from crewai import Task
from langchain_community.llms import OpenAI
  

class devCrewTasks():
  ### For the Product Owner
    def create_Product_Owner_requirements(self, agent, idea, details):
        return Task(description=f"You need to create clear requirements for {idea} with the following details: {details}", agent=agent)
    ### For the Business Analysts
    def create_BA_user_stories(self, agent, idea, details):
        return Task(description=f"Your goal is to translate {idea} into detailed, actionable user stories and acceptance criteria, considering the following details: {details}", agent=agent)
    ### For the Technical Architect
    def create_Technical_Architect_blueprint(self, agent, idea, details):
        return Task(description=f"Digest {idea}, and architect a coherent and scalable technical framework usi Streamlit for front-end and Python on backend, API and DB to be sql-ligt, considering the following details: {details}. Apply architectural patterns and technology stacks as appropriate.", agent=agent)
    ### For the UI/UX Designer
    def create_UIUX_Design_specs(self, agent, idea, details):
        return Task(description=f"Assess {idea}, exploring its potential UX and UI elements, and define clear design requirements in text form using the following details: {details}", agent=agent)
    ### For the Database Administrator (DBA)
    def create_DBA_DB_structure(self, agent, idea, details):
        return Task(description=f"Evaluate {idea} and develop a comprehensive database structure that supports the application's data requirements, based on: {details}", agent=agent)
    ### For the Developer   
    def create_Developer_implementation_plan(self, agent, idea, details):
        return Task(description=f"""Implement the technical framework and features based on the detailed requirements and architecture provided for {idea}, focusing on the following aspects: {details}. 
        Use coding best practices and relevant technologies. You would need to provide for project backend and front end each file, you can provide it like: 
        API.py
        
        from crewai import Crew
        from devCrewAIAgents import devCrewAIAgents

        class devCrewRun:
            def __init__(self, var1, var2):
                self.var1 = var1
                self.var2 = var2
         """, agent=agent)
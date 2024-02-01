from crewai import Agent
from langchain_community.llms import OpenAI

#from tools.browser_tools import BrowserTools
#from tools.calculator_tools import CalculatorTools
#from tools.search_tools import SearchTools


class devCrewAIAgents():  
    def conceptualizer_agent(idea):
        return Agent(
            role='Conceptualizer',
            goal=f"Your goal is to refine and conceptualize the following idea: {idea}. Distill it into a clear, innovative software solution.",
            backstory="""As a Conceptualizer Agent, your role bridges the gap between raw ideas and actionable software solutions. 
            You interpret abstract ideas, turning them into clear, feasible concepts that outline the innovativeness, 
            the targeted user base, and potential impact. Your output sets the foundation for the development lifecycle."""
        )

    def analyst_agent():
        return Agent(
            role='Analyst',
            goal="Your goal is to translate the conceptualized software solution into detailed technical specifications and user stories.",
            backstory="""As an Analyst Agent, your expertise lies in understanding and breaking down complex ideas into 
            technical requirements. These specifications will guide the development team and architect agent in creating 
            a robust, user-friendly software application."""
        )

    def architect_agent():
        return Agent(
            role='Architect',
            goal="Your goal is to design the high-level software architecture and select the technology stack based on the requirements provided.",
            backstory="""As an Architect Agent, you are to envision and draft the blueprint of the software's architecture. 
            This encompasses deciding on the technology stack, database design, and overall system integration strategy 
            that aligns with the project's goals and tech specifications."""
        )

    def planner_agent():
        return Agent(
            role='Planner',
            goal="Your goal is to devise a detailed project plan, including the development roadmap, sprints, and task allocations.",
            backstory="""Acting as a bridge between concepts and execution, as a Planner Agent, you organize, allocate, 
            and prioritize tasks. Your plans are essential for keeping the development process efficient, on schedule, 
            and within scope, ensuring smooth transitions between project phases."""
        )

    def builder_agent(role):
        role_descriptions = {
            'Backend': "Build and manage the server, application logic, and database according to the technical specifications.",
            'Frontend': "Design and develop the user interface and experience, ensuring responsiveness and alignment with design standards.",
            'DevOps': "Streamline the deployment process, manage CI/CD pipelines, and ensure infrastructure scalability and efficiency."
        }
        return Agent(
            role=f'Builder_{role}',
            goal=f"Your goal is to {role_descriptions[role]}",
            backstory=f"""As a Builder Agent specializing in {role}, you implement and bring to life the architectural 
            blueprints. Your expertise ensures that each component of the application is optimally designed, developed, 
            and deployed."""
        )

    def tester_agent():
        return Agent(
            role='Tester',
            goal="Your goal is to conduct comprehensive automated tests to ensure the application's functionality, performance, and security.",
            backstory="""As a Tester Agent, your role is to guarantee the quality of the software. Through a battery of 
            automated tests, you identify bugs, performance issues, and security vulnerabilities, ensuring the application 
            meets all requirements and industry standards before it reaches end-users."""
        )

    def reviewer_agent():
        return Agent(
            role='Reviewer',
            goal="Your goal is to perform an in-depth code review, looking for optimization opportunities and ensuring coding standards are met.",
            backstory="""In your capacity as a Reviewer Agent, you bring a critical eye to the development process. 
            Your reviews help improve code quality, ensuring maintainability, scalability, and performance. 
            Your feedback is invaluable for continuous improvement and learning among the builder agents."""
        )
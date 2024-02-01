from crewai import Crew
from devCrewAIAgents import devCrewAIAgents
from devCrewAITasks import devCrewTasks

class devCrewRun:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        self.agents = devCrewAIAgents()
        self.tasks = devCrewTasks()

    def run(self, agent_task_list):
        results = []
        for agent, task in agent_task_list:
            crew = Crew(
                agents=[agent],
                tasks=[task],
                verbose=True,
            )
            result = crew.kickoff()
            results.append(result)
        return results

if __name__ == "__main__":
    var1= """As a Product Owner taking on your request for designing an intuitive application for managing a self-development plan, I'll structure the initial input focusing on key aspects such as user experience and functionality, while meticulously outlining details that a Software Architect would require to develop high-level designs and database diagrams. After breaking down your request into actionable pieces, I might also have some clarification questions to ensure a well-rounded understanding of the project needs.

### Concept: Self-Development Planning Application

#### Project Name:
"Self-Growth Organizer"

#### Objective:
To develop an intuitive application enabling users to efficiently plan and track their self-development tasks, categorized into prioritized groups and manageable time slices, with an emphasis on flexibility and user-friendly experiences.

### Initial Input for Product Design:

#### Core Features:

1. **Task Management:**
   - **Functionality**:
     - Users can insert tasks with titles and descriptions.
     - Tasks can be assigned priorities and categorized into groups: Daily, Evening, Weekend.
     - An 'Add' button for new tasks.
     - Filters for viewing tasks by group and priority.
     - Remembering the last-used filter upon switch-back.
     - Display of tasks with details and progress indicators.
   
2. **Calendar View:**
   - **Functionality**:
     - Displays a weekly overview of planned task slices.
     - Allows for task slices (time allocated to tasks) to be added by pressing on free calendar space. No deadline constraints; unlimited slices.
     - Selection of task slice duration, task prioritization, and grouping during addition.
     - Ability to set a task slice as done, mark a full task as completed, or add remarks to a slice in a dialog window when pressing on existing tasks.
   
3. **Reporting:**
   - **Functionality**:
     - Reports on tasks and their associated slices, tracking completed, in-progress, or open tasks.
     - Visualization of how many slices were achieved compared to planned.
     
#### User Interface Requirements:

- **Intuitive Navigation:**
  - Tabs or buttons for switching between Task Management, Calendar View, and Reporting screens.
  
- **Responsive Design:**
  - The application should offer a seamless experience across devices, adjusting UI elements for desktop and mobile usage.

- **Accessibility Features:**
  - Including but not limited to font size options, contrast settings, and keyboard navigation capabilities.
  
### High-Level Architectural Needs:

- **Data Model Considerations:**
  - A database schema that supports tasks with attributes (title, description, priority, group).
  - Relational structures for tasks and time slices, ensuring efficient querying of task statuses and calendar events.
  
- **Technology Stack:**
  - Suggestions on front-end frameworks (e.g., React, Vue.js) that support dynamic UIs and state management.
  - Back-end considerations for scalable databases (e.g., PostgreSQL for relational data storage) and server technologies (e.g., Node.js, Flask).
  
- **API Endpoints:**
  - For task management, calendar updates, and reporting functionalities, ensuring they support CRUD operations and filtering.
  
### Clarification Questions:

1. What prioritization method should be applied to tasks, and how should priorities affect task planning or visibility in the calendar view?
2. Is there a need for user authentication and multi-user support, or will the application serve individual users?
3. Are there specific reporting metrics or insights, besides task progress and time allocation effectiveness, that you believe would benefit the users?
4. Regarding the UI/UX, are there any specific design motifs, themes, or inspirations you envision for the application?
5. How extensive should the remarking feature be for each slice of task—simple textual remarks, or more detailed annotations including attachments?

By answering these clarification questions and considering the detailed initial inputs above, we'll ensure a solid foundation for the Software Architect to design an application that meets user needs and provides a delightful and productive experience.

"""
    var2= "User stories and technical requirements..."

    dev_crew = devCrewRun(var1, var2)

    # Define your agents and tasks here
    POAgent = dev_crew.agents.ProductManager(var1)
    POTask = dev_crew.tasks.create_Product_Owner_requirements(POAgent, var1, var2)

    BAAgent = dev_crew.agents.BusinessAnalyst(var1)
    BATask = dev_crew.tasks.create_BA_user_stories(BAAgent, var1, var2)

    UIUXAgent = dev_crew.agents.UI_UX_Designer(var1)
    UIUXTAsk = dev_crew.tasks.create_UIUX_Design_specs(UIUXAgent, var1, var2)

    TAAgent = dev_crew.agents.TechnicalArchitect(var1)
    TATask = dev_crew.tasks.create_Technical_Architect_blueprint(TAAgent, var1, var2)

    DevAgent = dev_crew.agents.Developer(var1)
    DevTask = dev_crew.tasks.create_Developer_implementation_plan(DevAgent, var1, var2)

    DBAAgent = dev_crew.agents.DatabaseAdministrator(var1)
    DBATask = dev_crew.tasks.create_DBA_DB_structure(DBAAgent, var1, var2)

    # Define the order of agents and tasks here
    agent_task_list = [(POAgent, POTask), (BAAgent, BATask), (UIUXAgent, UIUXTAsk), (TAAgent, TATask), (DevAgent, DevTask), (DBAAgent, DBATask)]

    results = dev_crew.run(agent_task_list)

    print("\n\n########################")
    print("## Here are your custom crew run results:")
    print("########################\n")
    for result in results:
        print(result)
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class MultiAgentProject():
	"""MultiAgentProject crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True
		)

	@agent
	def Performance_Summary_Agent(self) -> Agent:
		return Agent(
			config=self.agents_config['Performance_Summary_Agent'],
			verbose=True
		)

	@agent
	def Comparison_and_Suggestion_Agent(self) -> Agent:
		return Agent(
			config=self.agents_config['Comparison_and_Suggestion_Agent'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_file='report.md'
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@task
	def comparison_task(self) -> Task:
		return Task(
			config=self.tasks_config['comparison_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the MultiAgentProject crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

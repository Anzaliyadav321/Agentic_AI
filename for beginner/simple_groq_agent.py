from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama3-70b-8192")  
)

agent.print_response("which is the most win team in IPL and under which captain")


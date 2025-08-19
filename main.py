from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.openai import OpenAIChat   # You can switch to Anthropic if you want
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
load_dotenv()
# Create the agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),   # or use Claude(id="claude-3-5-sonnet")
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions="Use tables to display stock market data.",
    markdown=True,
)

# Ask your finance question
qn=input("Enter Your Question")
agent.print_response(
f"{qn}",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
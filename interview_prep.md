==========================
DAY 1 - FASTAPI + DATABASE
==========================

Q1. What is a route?
Answer:
A route is an endpoint (URL) in a FastAPI application that maps an HTTP request to a specific Python function.

--------------------------------------------------

Q2. Why do we use FastAPI?
Answer:
FastAPI is used to build high-performance REST APIs quickly. It provides automatic validation, documentation, asynchronous support, and type checking.

--------------------------------------------------

Q3. What is PostgreSQL and why do we need it?
Answer:
PostgreSQL is a relational database used to permanently store application data. It allows structured storage, querying, transactions, and relationships between data.

--------------------------------------------------

Q4. Why do we use Docker?
Answer:
Docker provides an isolated and portable environment so the application runs consistently on any machine. Services like PostgreSQL, Redis, and ChromaDB run inside containers without depending on the host operating system.

--------------------------------------------------

Q5. What is DATABASE_URL?
Answer:
DATABASE_URL is the address of the database. It contains the database type, username, password, host, port, and database name so the application knows where to connect.

--------------------------------------------------

Q6. What is Engine?
Answer:
The Engine is SQLAlchemy's connection manager. It creates and manages connections between the application and the database.

--------------------------------------------------

Q7. What is AsyncSession?
Answer:
AsyncSession is used to execute asynchronous database operations like INSERT, UPDATE, DELETE and SELECT using the Engine.

--------------------------------------------------

Q8. What is a session?
Answer:
A session is a temporary conversation between the application and the database through which queries are executed.

--------------------------------------------------

Q9. Why do we need SQLAlchemy?
Answer:
SQLAlchemy is an ORM that lets us interact with the database using Python classes instead of writing raw SQL.

--------------------------------------------------

Q10. What is a model?
Answer:
A model is a Python class that represents a database table.

--------------------------------------------------

Q11. What is Base?
Answer:
Base is the parent class for all database models. Every model inherits from Base.

--------------------------------------------------

Q12. What is metadata?
Answer:
Metadata stores information about all database tables such as table names, columns, constraints and relationships.

--------------------------------------------------

Q13. What does metadata.create_all() do?
Answer:
It creates all database tables defined by models that inherit from Base if they do not already exist.

--------------------------------------------------

Q14. What is run_sync()?
Answer:
run_sync() executes synchronous SQLAlchemy functions like metadata.create_all() inside an asynchronous environment.

--------------------------------------------------

Q15. Difference between SQLAlchemy Model and Pydantic Model?

Answer:
SQLAlchemy Model represents a database table and interacts with the database.

Pydantic Model validates request and response data before it reaches the database or is returned to the client.

--------------------------------------------------

Q16. Why do we need both User and UserCreate?

Answer:
User is the SQLAlchemy model that creates and manages the users table.

UserCreate is the Pydantic model that validates incoming API request data.

This separates database logic from validation logic and improves modularity.

--------------------------------------------------

Q17. What is Pydantic?

Answer:
Pydantic is a data validation library that validates request and response data using Python type hints.

--------------------------------------------------

Q18. What is a Pydantic Model?

Answer:
A Pydantic model is a Python class used to validate and serialize data before it enters or leaves the application.

--------------------------------------------------

Q19. What is @asynccontextmanager?

Answer:
It creates startup and shutdown logic for FastAPI.

Everything before yield runs during startup.

Everything after yield runs during shutdown.

--------------------------------------------------

Q20. Why do we need lifespan()?

Answer:
It automates startup and shutdown tasks like initializing database connections, caches, models, or cleaning resources without doing them manually.

--------------------------------------------------

Q21. Why do we need the /health endpoint?

Answer:
It checks whether the server is running and healthy before clients send actual API requests.

==========================================================
DAY 2 - LANGGRAPH
==========================================================

Q22. What is LangGraph?

Answer:
LangGraph is a framework for building stateful, graph-based LLM and multi-agent workflows. It manages nodes, edges, routing, loops, and shared state throughout the workflow.

--------------------------------------------------

Q23. Why use LangGraph instead of sequential Python functions?

Answer:
LangGraph breaks large tasks into smaller nodes. Each node performs a specific responsibility, making workflows modular, scalable, debuggable, monitorable, and cost-efficient. Different nodes can even use different models or tools.

--------------------------------------------------

Q24. What is stateful?

Answer:
Stateful means the workflow remembers and carries information from one node to another throughout execution.

--------------------------------------------------

Q25. What is typing?

Answer:
The typing module provides type hints that improve readability, validation, and editor support.

--------------------------------------------------

Q26. What is TypedDict?

Answer:
TypedDict defines the expected structure and data types of a dictionary, providing type safety and catching missing keys or typos.

--------------------------------------------------

Q27. What is GraphState?

Answer:
GraphState is the TypedDict representing the shared state passed between all nodes.

--------------------------------------------------

Q28. What is a node?

Answer:
A node is a function that receives the current state, performs its task, updates the state, and returns the updated state.

--------------------------------------------------

Q29. Why not use a normal dictionary instead of TypedDict?

Answer:
A normal dictionary works, but TypedDict provides type safety, catches missing keys and typos, and makes large workflows easier to maintain.

--------------------------------------------------

Q30. What is StateGraph?

Answer:
StateGraph is the workflow builder used to define nodes, edges, and the shared state for execution.

--------------------------------------------------

Q31. What is START?

Answer:
START marks where workflow execution begins.

--------------------------------------------------

Q32. What is END?

Answer:
END marks where workflow execution finishes and returns the final state.

--------------------------------------------------

Q33. What does add_node() do?

Answer:
It registers a node function inside the workflow with a given node name.

--------------------------------------------------

Q34. What does add_edge() do?

Answer:
It connects two nodes and defines the execution flow between them.

--------------------------------------------------

Q35. What is compile()?

Answer:
compile() converts the graph definition into an executable workflow.

--------------------------------------------------

Q36. What is graph.invoke()?

Answer:
graph.invoke() executes the complete workflow from START to END and returns the final updated state.

--------------------------------------------------

Q37. What is graph.stream()?

Answer:
graph.stream() executes the workflow step by step and returns the output after each node executes, making debugging and monitoring easier.

--------------------------------------------------

Q38. What is the datatype of graph.stream()?

Answer:
graph.stream() returns an iterator (generator) that yields one node's output at a time.

-------------------------------------------------

Q42. Explain graph.invoke() execution flow.

Answer:
1. graph.invoke() receives the initial state.
2. Execution starts from START.
3. The state is passed to the first node.
4. The node updates and returns the state.
5. LangGraph follows the defined edges.
6. Execution reaches END.
7. The final updated state is returned.

--------------------------------------------------

Q43. Why do we need START and END?

Answer:
START defines where execution begins and END defines where execution finishes. LangGraph follows the edges between nodes until END is reached.

--------------------------------------------------

Q44. Difference between a node and the state?

Answer:
The state is the shared data passed between all nodes in the workflow. A node is a function that reads the current state, performs its task, updates the state, and returns it.

--------------------------------------------------

Q45. Why split Planner → Retriever → Synthesizer instead of one large function?

Answer:
Splitting responsibilities improves modularity, scalability, debugging, monitoring, maintainability, and allows different models or tools to be used for different tasks.

--------------------------------------------------

Q46. What happens if a node doesn't return the updated state?

Answer:
The workflow breaks because the next node does not receive the shared state. Returning the updated state is mandatory since it carries information produced by previous nodes to subsequent nodes.

****************************************************
Day -3
***************************************************

# Day 3 - ReAct Agent Interview Questions & Answers

---

## Q1. What is an AI Agent?

**Answer:**

An AI Agent is a system powered by an LLM that can reason, make decisions, use tools, and perform actions to accomplish a task instead of only generating text.

---

## Q2. What is a ReAct Agent?

**Answer:**

A ReAct (Reason + Act) agent is an AI agent that alternates between reasoning and taking actions. It follows the loop:

Thought → Action → Observation → Thought → ... → Final Answer

This allows the LLM to use external tools, observe their outputs, and continue reasoning until it can answer confidently.

---

## Q3. What is LangChain?

**Answer:**

LangChain is a framework for building LLM applications. It provides:

- LLM wrappers
- Tools
- Prompts
- Output parsers
- Memory
- Embeddings
- Vector store integrations

It provides the building blocks for AI applications.

---

## Q4. What is LangGraph?

**Answer:**

LangGraph is a framework built on top of LangChain for creating stateful graph-based AI workflows.

It manages:

- Nodes
- Edges
- State
- Routing
- Loops
- Multi-agent workflows

---

## Q5. What is LangSmith?

**Answer:**

LangSmith is an observability and debugging platform.

It provides:

- Execution traces
- Logs
- Token usage
- Latency
- Monitoring
- Evaluation

It does NOT execute the workflow.

---

## Q6. Difference between LangChain, LangGraph and LangSmith?

**Answer:**

LangChain → Provides LLMs, tools, prompts, memory and integrations.

LangGraph → Controls workflow using nodes, edges and shared state.

LangSmith → Observes, traces and debugs execution.

Analogy:

LangChain = Toolbox

LangGraph = Project Manager

LangSmith = CCTV + Analytics

---

## Q7. What is ChatGroq?

**Answer:**

ChatGroq is a LangChain wrapper around Groq-hosted language models.

It allows LangChain and LangGraph to communicate with Groq APIs.

---

## Q8. What is ChatGoogleGenerativeAI?

**Answer:**

It is the LangChain wrapper used to access Google's Gemini models.

Only the LLM wrapper changes; the LangGraph workflow remains the same.

---

## Q9. What is temperature?

**Answer:**

Temperature controls randomness.

temperature = 0

- deterministic
- repeatable
- ideal for production

Higher temperatures generate more creative and random outputs.

---

## Q10. What is invoke()?

**Answer:**

invoke() executes the complete agent workflow.

It accepts the input, executes all reasoning and tool calls if required, and returns the final conversation state.

---

## Q11. What is HumanMessage?

**Answer:**

HumanMessage represents the user's input.

Agents communicate through messages instead of plain strings.

Common message types are:

- HumanMessage
- AIMessage
- ToolMessage
- SystemMessage

---

## Q12. What is @tool?

**Answer:**

@tool registers a Python function as a tool that LangChain/LangGraph can expose to the LLM.

Without @tool, the framework cannot register or invoke the function as an available tool.

---

## Q13. What is eval()?

**Answer:**

eval() evaluates a Python expression stored as a string.

Example:

eval("25 * 8")

returns

200

---

## Q14. Why do we need both an LLM and tools?

**Answer:**

The LLM provides reasoning and decides whether a tool should be called.

Tools perform external actions such as:

- searching
- calculations
- SQL
- APIs

Without tools, the LLM is limited to its internal knowledge.

Without the LLM, tools cannot decide when or how they should be used.

Think of it as:

LLM = Brain

Tools = Hands

---

## Q15. How does the agent decide which tool to call?

**Answer:**

The user's query, conversation context and available tool descriptions are sent to the LLM.

During the reasoning step, the LLM decides:

- whether a tool is needed
- which tool(s) should be used

It then generates structured tool calls.

---

## Q16. Can a ReAct agent call multiple tools in one iteration?

**Answer:**

Yes.

One reasoning iteration may generate multiple tool calls.

Example:

Thought

↓

web_search()

calculator()

↓

Observations

↓

Final Answer

---

## Q17. What is a ReAct Iteration?

**Answer:**

One reasoning cycle.

Thought

↓

Action

↓

Observation

One AIMessage containing tool_calls equals one iteration.

---

## Q18. What is NOT counted as an iteration?

**Answer:**

Do NOT count:

- HumanMessage
- ToolMessage
- Final AIMessage

Only AIMessage containing tool_calls counts as an iteration.

---

## Q19. What are LLM Calls?

**Answer:**

Every AIMessage is generated by the LLM.

Therefore,

AIMessage with tool_calls

↓

LLM Call

Final AIMessage

↓

Another LLM Call

---

## Q20. Difference between LLM Calls and Iterations?

**Answer:**

Iterations

Only AIMessage containing tool_calls.

LLM Calls

Every AIMessage.

Example:

Human

↓

AIMessage(tool_calls)

↓

Tool

↓

AIMessage(final)

Iterations = 1

LLM Calls = 2

---

## Q21. Runtime execution flow of invoke()

**Answer:**

agent.invoke()

↓

LangGraph starts workflow

↓

LangChain prepares messages and available tools

↓

LLM receives prompt

↓

LLM reasons

↓

LLM generates tool call

↓

LangChain/LangGraph matches the tool

↓

Python interpreter executes the registered function

↓

Result wrapped into ToolMessage

↓

ToolMessage returned to LLM

↓

LLM generates final answer

↓

LangGraph returns final state

↓

print(response)

Meanwhile LangSmith records the entire execution trace.

---

## Q22. Who executes the Python tool?

**Answer:**

LLM decides which tool to call.

LangChain/LangGraph identifies the registered tool.

Python interpreter executes the function.

LangChain wraps the output into ToolMessage.

LangSmith only records the execution.

---

## Q23. What happens if @tool is removed?

**Answer:**

The function is no longer registered as a tool.

When the LLM generates a tool call, LangChain/LangGraph cannot match it to a registered function.

Therefore the tool cannot be executed.

---

## Q24. ReAct Paper

**Problem**

LLMs could either reason or use tools but not effectively combine both.

**Core Idea**

Thought

↓

Action

↓

Observation

↓

Thought

↓

Final Answer

**Advantages**

- Uses external tools
- Reduces hallucinations
- Better multi-step reasoning
- More interpretable
- Better decision making

**Limitations**

- More LLM calls
- Higher latency
- Higher cost
- Depends on tool quality

---

## Q25. Why does ReAct make more LLM calls?

**Answer:**

Every reasoning step is another LLM call.

Example:

Question

↓

LLM Call 1

↓

Tool

↓

Observation

↓

LLM Call 2

↓

Final Answer

More reasoning loops result in more LLM calls.

---

## Q26. Why did the agent retry after a Network Error?

**Answer:**

After observing the ToolMessage containing the network error, the LLM reasoned that it still lacked the required information.

Therefore it initiated another tool call before producing the final answer.

---

## Q27. Execution Trace (Tool Used)

HumanMessage

↓

AIMessage(tool_calls)

↓

ToolMessage

↓

AIMessage(final)

Iterations = 1

LLM Calls = 2

---

## Q28. Execution Trace (No Tool Needed)

HumanMessage

↓

AIMessage(final)

Iterations = 0

LLM Calls = 1

---

## Q29. Example with Retry

Human

↓

AIMessage(tool_calls)

↓

ToolMessage(Network Error)

↓

AIMessage(tool_calls)

↓

ToolMessage(Result)

↓

AIMessage(final)

Iterations = 2

LLM Calls = 3

# Enterprise Multi-Agent System
# Day 4 - Interview Questions & Answers

---

# Q1. Suppose the LLM generates an invalid tool argument.

Example:

```json
{
    "expression": 125
}
```

instead of

```json
{
    "expression": "125"
}
```

Walk through the complete execution flow until the error reaches the agent.

## Answer

Execution Flow:

```
LLM
│
Generates Tool Call
{
    "expression": 125
}
│
▼
LangChain/LangGraph
Receives Tool Call
│
▼
Pydantic (CalculatorInput)
Validates Input
│
├── Valid
│      │
│      ▼
│   Execute Tool
│
└── Invalid
       │
       ▼
ValidationError
       │
       ▼
LangChain/LangGraph
Receives Exception
       │
       ▼
Agent execution fails
(or handles the error if configured)
```

Pydantic validates the LLM-generated tool arguments before the Python tool function is executed. If validation fails, the tool is never executed.

---

# Q2. Suppose we remove only:

```python
args_schema=CalculatorInput
```

while keeping

```python
@tool
def calculator(expression: str):
```

What functionality do we lose? What still works?

## Answer

Removing `args_schema` removes:

- Pydantic input validation
- JSON Schema generation
- Strong guidance for tool calling
- Early detection of invalid inputs

The tool still works because LangChain can infer arguments from the Python function signature.

Without args_schema:

```
LLM
│
Function Signature
│
▼
Tool Execution
```

With args_schema:

```
LLM
│
JSON Schema
│
▼
Pydantic Validation
│
▼
Tool Execution
```

The enterprise benefit is increased reliability and safer tool execution.

---

# Q3. Why is Tool Registry considered an enterprise design pattern rather than just a convenience?

## Answer

A Tool Registry acts as the centralized source of truth for all available tools.

Instead of every agent knowing every tool, the agent only knows the registry.

Benefits:

- Separation of concerns
- Low coupling
- High cohesion
- Modular architecture
- Easier maintenance
- Easier debugging
- Easier testing
- Easy scalability
- Easy reuse
- Multiple agents can share the same registry
- New tools can be added without modifying agent code

Architecture:

```
calculator.py
web_search.py
weather.py
sql.py
email.py
        │
        ▼
registry.py
        │
        ▼
TOOLS
        │
        ▼
react_agent.py
```

---

# Q4. Explain the complete async execution flow from:

```python
await agent.ainvoke(...)
```

until the final answer is returned.

## Answer

Execution Flow:

```
await agent.ainvoke()
        │
        ▼
Event Loop
Schedules coroutine
        │
        ▼
LangGraph
Starts workflow
        │
        ▼
LLM
Reasons
Selects Tool
        │
        ▼
LangChain/LangGraph
Invokes async tool
        │
        ▼
await web_search(...)
        │
        ▼
Current coroutine is suspended
        │
        ▼
Event Loop
Runs other ready coroutines
        │
        ▼
Web search completes
        │
        ▼
LangChain/LangGraph
Wraps result into ToolMessage
        │
        ▼
LLM
Receives ToolMessage
Reasons again
        │
        ▼
Final AIMessage
        │
        ▼
LangGraph
Returns final response
```

Async is beneficial for I/O-bound operations such as APIs, databases, web search, vector databases and external services.

CPU-bound operations such as mathematical calculations generally remain synchronous.

---

# Q5. Why is the following architecture preferred in enterprise systems?

```
app/
│
├── agents/
│      ├── planner.py
│      ├── retriever.py
│      └── synthesizer.py
│
├── tools/
│      ├── calculator.py
│      ├── web_search.py
│      ├── sql.py
│      ├── weather.py
│      ├── email.py
│      ├── schemas.py
│      └── registry.py
```

instead of putting everything inside `react_agent.py`?

## Answer

This architecture separates responsibilities so that each tool, agent and registry has a single purpose.

It promotes:

- High cohesion
- Low coupling
- Easier maintenance
- Easier debugging
- Easier testing
- Better reusability
- Better scalability

Individual teams can work independently on different tools or agents without affecting unrelated modules.

The Tool Registry acts as a centralized source of truth, allowing agents to consume tools without knowing their implementations.

---

# Q6. Why is the following tool much more likely to be selected?

```python
@tool
def search_documents():
    """
    Search HR policies,
    employee handbook,
    leave policies,
    payroll documents.
    """
```

than

```python
@tool
def search():
    """
    Search documents.
    """
```

for the query:

> "How many paid leaves does an employee receive?"

## Answer

The LLM computes which tool best semantically matches the user's intent based on:

- Tool name
- Tool description
- JSON Schema
- User query
- Conversation context

The second tool contains domain-specific terms such as:

- HR policies
- Employee handbook
- Leave policies
- Payroll

These strongly align with the user's question, giving the LLM much higher confidence that this is the correct tool to invoke.

---

# Q7. What transformed your project from a toy AI agent into an enterprise AI agent?

## Answer

The project evolved from a toy AI agent to an enterprise AI agent by introducing architectural separation of concerns.

Key improvements include:

- Independent tool modules
- Independent agent modules
- Tool Registry as a centralized source of truth
- Pydantic schemas for reliable input validation
- JSON Schema generation for accurate tool calling
- Structured outputs for reliable communication between tools, agents, APIs and UIs
- Async execution for I/O-bound operations
- LangSmith tracing for observability, debugging, monitoring and execution visualization

Together, these changes made the system modular, scalable, maintainable, reliable and production-ready rather than a single-file demonstration.

---

# Quick Definitions

## What is Pydantic?

Pydantic is a Python data validation library that validates tool inputs and outputs using Python type hints.

---

## What is a Schema?

A schema defines the expected structure, required fields and data types of data.

---

## What is JSON Schema?

JSON Schema is the machine-readable representation of a Pydantic model that LangChain sends to the LLM during tool calling.

---

## What is a Tool Registry?

A Tool Registry is a centralized module that stores and exposes all available tools, acting as the single source of truth for agents.

---

## What is Structured Output?

Structured output returns data in JSON/dictionary format instead of free text, making it easier for LLMs, APIs, agents and UIs to consume reliably.

---

## Why use Async Tools?

Async tools allow multiple I/O-bound operations to execute concurrently, reducing latency and improving throughput.

---

## What does LangSmith provide?

LangSmith provides observability through:

- Tracing
- Debugging
- Monitoring
- Visualization
- Latency analysis
- Tool execution history
- Agent execution flow
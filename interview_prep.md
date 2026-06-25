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
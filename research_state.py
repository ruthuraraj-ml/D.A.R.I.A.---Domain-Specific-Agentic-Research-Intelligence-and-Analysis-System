class ResearchState(TypedDict):

    # User
    query: str
    thread_id: str

    # Memory
    memory_hit: bool
    memory_similarity: float
    memory_evidence: list

    # Planning
    route: str
    research_plan: list[str]
    information_gaps: list[str]

    # Research
    rag_evidence: list
    rag_sources: list

    web_evidence: list
    web_sources: list

    # Critic
    critic_score: float
    critic_feedback: str

    # Loop
    iteration_count: int
    max_iterations: int

    # Output
    confidence_score: float
    final_response: str
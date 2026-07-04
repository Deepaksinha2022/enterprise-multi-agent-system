import os

from tavily import TavilyClient

from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

class ResearchAgent:

    def search(self, query: str):

        return client.search(
            query=query,
            max_results=5
            )

    async def research(self, query: str):
        
        response = self.search(query)

        structured_results = []

        summaries = []

        for result in response["results"]:
            structured_results.append({
                "title": result["title"],
                "summary": result["content"],
                "source": result["url"]
            })

            summaries.append(result["content"])

        final_summary = " ".join(summaries)

        return {
            "query": query,
            "summary": final_summary,
            "sources": structured_results
        }
Create a langgraph sytate workflow 

1. You have to create one supervisor node.
2. Create one router function
3. Create three more nodes
3.1 llm call (llm node)
3.2 RAG (rag node)
3.3 web crawler(fetch the info in realtime from internet)
4. create one more node after this for validation
5. if validation going to be failed in that case again go to supervioser node and then supervisor node will again decide what needs to be called next
6. once the validation will pass then generate the final output
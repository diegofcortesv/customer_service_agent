"""
Knowledge Base Agent - Searches for solutions in knowledge base
"""
from .agent import knowledge_agent
from .tools import KnowledgeBaseTool

__all__ = ['knowledge_agent', 'KnowledgeBaseTool']
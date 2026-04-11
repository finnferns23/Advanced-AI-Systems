class IdeaMessage:
    def __init__(self, idea: str, source: str):
        self.idea = idea
        self.source = source

    def __repr__(self):
        return f"Idea(from={self.source}, idea={self.idea})"

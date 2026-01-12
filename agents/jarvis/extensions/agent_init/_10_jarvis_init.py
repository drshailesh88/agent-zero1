from python.helpers.extension import Extension


class JarvisInit(Extension):
    """
    Initialize JARVIS agent with proper naming and personality setup.
    """

    async def execute(self, **kwargs):
        # Set the agent name to JARVIS
        self.agent.agent_name = "JARVIS"

        # For subordinate agents, append a designation
        if self.agent.number > 0:
            self.agent.agent_name = f"JARVIS-{self.agent.number}"

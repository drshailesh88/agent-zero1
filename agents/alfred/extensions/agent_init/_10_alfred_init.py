from python.helpers.extension import Extension


class AlfredInit(Extension):
    """
    Initialize ALFRED agent with proper naming and stewardship orientation.
    """

    async def execute(self, **kwargs):
        # Set the agent name to ALFRED
        self.agent.agent_name = "ALFRED"

        # For subordinate agents, maintain the ALFRED identity with designation
        if self.agent.number > 0:
            self.agent.agent_name = f"ALFRED-{self.agent.number}"

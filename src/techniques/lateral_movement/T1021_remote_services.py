from utils.logger import logger
from utils.platform_detection import get_platform


class Technique:
    """
    Simulated lateral movement via remote services.
    This does NOT perform any network actions. Pure simulation.
    """

    def __init__(self):
        self.meta = {
            "id": "T1021",
            "name": "Remote Services (Simulated)",
            "tactic": "lateral_movement",
        }

    def run(self):
        platform = get_platform()
        logger.info("Simulating remote service lateral movement on: %s", platform)

        simulated_hosts = [
            "host-01.internal",
            "host-02.internal",
            "backup-node.internal",
        ]

        logger.info("Simulated connection attempts to %d hosts", len(simulated_hosts))

        return {
            "platform": platform,
            "attempted_hosts": simulated_hosts,
            "status": "simulated_connections_only",
        }

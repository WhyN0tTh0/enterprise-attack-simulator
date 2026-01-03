from utils.logger import logger
from utils.platform_detection import get_platform


class Technique:
    """
    Simulates user enumeration in a *non-destructive* way.
    This is an educational placeholder and does not perform any malicious action.
    """

    def __init__(self):
        self.meta = {
            "id": "T1087",
            "name": "Account Discovery (Simulated)",
            "tactic": "discovery",
        }

    def run(self):
        platform = get_platform()
        logger.info("Simulating account discovery on platform: %s", platform)

        # In a real red team tool, OS commands or APIs would be used.
        # Here we only return static, anonymized data to keep it safe.
        simulated_users = [
            "user01",
            "service_account_app",
            "admin_like_account",
        ]

        logger.info("Discovered %d simulated accounts", len(simulated_users))

        return {
            "platform": platform,
            "discovered_accounts": simulated_users,
        }

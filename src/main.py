import argparse
from core.executor import AttackExecutor
from core.technique_loader import TechniqueLoader
from core.report_generator import ReportGenerator
from utils.logger import logger
from utils.system_checks import ensure_safe_environment


def parse_args():
    parser = argparse.ArgumentParser(
        description="Enterprise Attack Simulator (educational, non-destructive framework)."
    )
    parser.add_argument(
        "--profile",
        required=True,
        help="Path to attack profile YAML file."
    )
    parser.add_argument(
        "--report",
        default="reports/report.json",
        help="Path to output report file."
    )
    return parser.parse_args()


def main():
    args = parse_args()

    logger.info("Starting Enterprise Attack Simulator")

    ensure_safe_environment()

    loader = TechniqueLoader()
    techniques = loader.load_from_profile(args.profile)

    executor = AttackExecutor()
    results = executor.run_techniques(techniques)

    report_generator = ReportGenerator()
    report_generator.generate(results, args.report)

    logger.info("Simulation finished. Report saved at: %s", args.report)


if __name__ == "__main__":
    main()

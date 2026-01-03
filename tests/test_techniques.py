import pytest
from src.techniques.discovery.T1087_list_users import Technique as T1087
from src.techniques.persistence.T1053_scheduled_tasks import Technique as T1053
from src.techniques.lateral_movement.T1021_remote_services import Technique as T1021


@pytest.mark.parametrize("tech_class", [T1087, T1053, T1021])
def test_technique_run_returns_dict(tech_class):
    """
    Ensures each technique runs safely and returns a dictionary.
    All techniques in this framework are simulated and non-destructive.
    """
    technique = tech_class()
    result = technique.run()

    assert isinstance(result, dict), "Technique run() must return a dictionary"
    assert "platform" in result, "Result must include platform information"

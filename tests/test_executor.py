from core.executor import AttackExecutor


class DummyTechnique:
    def __init__(self):
        self.meta = {"id": "TEST", "name": "Dummy Technique"}

    def run(self):
        return {"ok": True}


def test_executor_runs_technique():
    executor = AttackExecutor()
    results = executor.run_techniques([DummyTechnique()])

    assert len(results) == 1
    assert results[0]["status"] == "success"
    assert results[0]["id"] == "TEST"

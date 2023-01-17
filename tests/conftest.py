import json

import pytest


@pytest.fixture(params=["f63ac879-fa7d-4f91-813e-e816cbdf1927"])
def ilcd_data(datafix_dir, request) -> dict:
    return json.loads((datafix_dir / (request.param + ".json")).read_text())


# test_requirements.py


import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from app.agents.requirements import extract_requirements

state = {
    "user_query": (
        "Plan a 7 day trip to Japan for 2 people "
        "under $3000. We love food, temples, and anime."
    )
}

result = extract_requirements(state)

print(result["requirements"])
from src.agents.system_prompt.system_prompt_pdi_agent import SYSTEM_PROMPT_PDI_AGENT
from src.util.current_datetime import current_datetime
from src.settings.openai import client


def pdi_agent(user_prompt, near_doc):
    message = client.responses.create(
        model="gpt-4",
        input=[
            {"role": "developer", "content": f"Data e tempo atual: {current_datetime}"},
            {"role": "developer", "content": SYSTEM_PROMPT_PDI_AGENT},
            {"role": "developer", "content": near_doc},
            {"role": "user", "content": user_prompt},
        ],
    )

    return message.output_text

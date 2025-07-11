from google import genai
from google.genai import types
import base64
import re
import openpyxl
import sys
import importlib
import common.prompts as prompts
import common.file_processing as file_processing


importlib.reload(prompts)
importlib.reload(file_processing)


def gemini_nutritionist(client, model, tokens, temperature, prompt, image_byte):
    try:

        response = client.models.generate_content(
            model=model,
            contents=[
                types.Part.from_bytes(
                    data=image_byte,
                    mime_type='image/jpeg',
                ),
                prompt
            ],
            config=types.GenerateContentConfig(
                temperature=temperature,
                response_mime_type="application/json",
                max_output_tokens=tokens,
            )
        )
        return response.text
    except Exception as e:
        print(f"Error in gemini_serving_size: {e}")
        return None


def gpt_nutritionist(client, model, tokens, temperature, system_prompt, prompt, image_byte):
    image = base64.b64encode(image_byte).decode("utf-8")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=tokens,
            temperature=temperature,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in gpt_nutritionist: {e}")
        return None


def anthropic_nutritionist(client, model, tokens, temperature, system_prompt, prompt, image_byte):
    image = base64.b64encode(image_byte).decode("utf-8")

    response = client.messages.create(
        model=model,
        temperature=temperature,
        max_tokens=tokens,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": f"{image}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    data_text = "".join(
        block.text for block in response.content if block.type == "text"
    )

    return data_text

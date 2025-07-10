import json
import os


def parse_json(text):
    """Parse JSON from model response with better error handling"""
    if not text:
        raise ValueError("Input text is None or empty")

    if not isinstance(text, str):
        raise ValueError(f"Input text is not a string, got {type(text)}")

    # Clean the text
    text = text.strip()

    # Try direct parsing first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try to find JSON between first { and last }
    try:
        start = text.find('{')
        end = text.rfind('}')
        if start != -1 and end != -1 and end > start:
            json_str = text[start:end+1]
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass

    # Try to extract JSON using a more robust regex
    import re
    json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    matches = re.findall(json_pattern, text, re.DOTALL)

    for match in matches:
        try:
            return json.loads(match)
        except json.JSONDecodeError:
            continue

    # If we get here, no valid JSON was found
    raise ValueError(f"No valid JSON found in text: {text[:200]}...")


def count_images(folder_path):
    """Count numbered images"""
    count = 0
    index = 1
    while os.path.exists(os.path.join(folder_path, f"{index}.jpg")):
        count += 1
        index += 1
    return count

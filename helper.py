def strip_json_code_block(text: str) -> str:
    # find the first “{” and the last “}”
    start = text.index("{")
    end   = text.rindex("}") + 1
    text2 = text[start:end]
    
    # Remove opening and closing code block markers
    lines = text2.strip().splitlines()
    cleaned_lines = [line for line in lines if not line.strip().startswith("```")]
    return "\n".join(cleaned_lines)

from tools.hf_vlm_tool import analyze_image

def vlm_agent(image_path, query):

    result = analyze_image(
        image_path,
        query
    )

    return result
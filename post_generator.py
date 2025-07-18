from llm_helper import llm
from few_shot import Few_Shot_Posts

fs = Few_Shot_Posts()




def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 8 lines"
    else:
        return "9 to 12 lines"
    

def get_prompt(length,tag):
    length_str = get_length_str(length)
    example_posts = fs.get_filtered_posts(length, tag)

    prompt = f"""
    Generate a different Linkedin Post using the information , Given Below. No preamble.

    1.Topic: {tag}
    2.Length: {length_str}
    """
    if len(example_posts) > 0:
        prompt += "4.Use the writing style as per the following examples"

        for i, post in enumerate(example_posts):
            post_text = post["text"]
            prompt += f"\n\nExample {i + 1}:\n\n  {post_text}"
            
            if i == 1:
                break
    return prompt


def generate_post(length,tag):
    prompt = get_prompt(length, tag)
    print(prompt)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    post = generate_post("Medium","Digital Summit")
    print(post)

import json
import os
import google.generativeai as genai

def create_tests():
    """
    Creates test files for new problems with 50 test cases each.
    """
    try:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")
    except KeyError:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    with open("data.json", "r") as f:
        challenges = json.load(f)

    for problem in challenges:
        test_file_path = f"tests/test_{problem['title'].lower().replace(' ', '_')}.py"
        # Check if the test file already exists and is not empty
        if not os.path.exists(test_file_path) or os.path.getsize(test_file_path) == 0:
            print(f"Generating tests for: {problem['title']}")
            prompt = f"Provide 50 test cases for the coding challenge: {problem['title']}. The output should be in the format of a python file using the pytest framework. The solution file is located at solutions/solution_{problem['id']}.py"
            try:
                response = model.generate_content(prompt)
                with open(test_file_path, "w") as f:
                    f.write(response.text)
            except Exception as e:
                print(f"Error generating tests for {problem['title']}: {e}")

    print("Test files have been created.")

if __name__ == "__main__":
    create_tests()

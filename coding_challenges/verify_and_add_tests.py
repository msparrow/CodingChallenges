import json
import os
import re
import google.generativeai as genai

def count_test_cases(file_content):
    """Counts the number of test cases in a file."""
    return len(re.findall(r'def\s+test_', file_content))

def verify_and_add_tests(start_id, end_id):
    """
    Verifies the number of test cases for a range of problems and adds more if needed.
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
        problem_id = problem['id']
        if not (start_id <= problem_id <= end_id):
            continue

        test_file_path = f"tests/test_{problem['title'].lower().replace(' ', '_')}.py"
        if not os.path.exists(test_file_path):
            print(f"Test file not found for problem {problem_id}: {test_file_path}")
            # Create the file with a basic structure
            with open(test_file_path, "w") as f:
                f.write(f"import pytest\nfrom solutions.solution_{problem_id} import *\n\n# Add test cases here")
            current_test_count = 0
        else:
            with open(test_file_path, "r") as f:
                content = f.read()
                current_test_count = count_test_cases(content)

        if current_test_count < 20:
            num_to_add = 20 - current_test_count
            print(f"Problem {problem_id}: Found {current_test_count} tests. Adding {num_to_add} more.")

            prompt = f"Provide {num_to_add} additional pytest test cases for the coding challenge: {problem['title']}. The solution file is located at solutions/solution_{problem['id']}.py. The existing test file is:\n\n```python\n{content}\n```\n\nDo not repeat existing test cases. Provide only the new test functions."
            try:
                response = model.generate_content(prompt)
                # Extract the code from the markdown
                new_tests_match = re.search(r'```python\n(.*)```', response.text, re.DOTALL)
                if new_tests_match:
                    new_tests = new_tests_match.group(1)
                    with open(test_file_path, "a") as f:
                        f.write("\n\n" + new_tests)
                    print(f"Added {num_to_add} tests to {test_file_path}")
                else:
                    print(f"Could not extract new tests from the response for problem {problem_id}")

            except Exception as e:
                print(f"Error generating tests for {problem['title']}: {e}")
        else:
            print(f"Problem {problem_id}: Found {current_test_count} tests. No action needed.")

if __name__ == "__main__":
    # For the second batch of 10
    verify_and_add_tests(11, 20)

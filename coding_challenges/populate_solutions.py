

import json
import os
import google.generativeai as genai

def populate_solutions():
    """
    Populates the solutions.json file with solutions for new problems.
    """
    try:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    except KeyError:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    with open("data.json", "r") as f:
        challenges = json.load(f)

    with open("solutions.json", "r+") as f:
        solutions = json.load(f)
        new_problems = [p for p in challenges if str(p['id']) not in solutions]

        for problem in new_problems:
            challenge_id = str(problem["id"])
            print(f"Fetching solution for: {problem['title']}")
            prompt = f'''Provide a Python solution and a detailed explanation for the '{problem["title"]}' problem.\n\nProblem Description:\n{problem["description"]}'''
            try:
                response = model.generate_content(prompt)
                solutions[challenge_id] = response.text
                solution_file_path = f"solutions/solution_{challenge_id}.py"
                with open(solution_file_path, "w") as solution_file:
                    solution_file.write(response.text)
            except Exception as e:
                print(f"Error getting solution for problem {challenge_id}: {e}")

        f.seek(0)
        f.truncate()
        json.dump(solutions, f, indent=2)

    print("solutions.json and solution files have been updated.")

if __name__ == "__main__":
    populate_solutions()


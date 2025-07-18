
import json
import os
import google.generativeai as genai

def add_problems():
    """
    Adds new problems to the data.json file.
    """
    try:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-1.5-flash")
    except KeyError:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    new_problems = [
        {"id": 121, "title": "Best Time to Buy and Sell Stock", "difficulty": "Easy", "category": "Arrays"},
        {"id": 122, "title": "Contains Duplicate", "difficulty": "Easy", "category": "Arrays"},
        {"id": 123, "title": "Reverse String", "difficulty": "Easy", "category": "Strings"},
        {"id": 124, "title": "First Unique Character in a String", "difficulty": "Easy", "category": "Strings"},
        {"id": 125, "title": "Linked List Cycle", "difficulty": "Easy", "category": "Linked Lists"},
        {"id": 126, "title": "Subtree of Another Tree", "difficulty": "Easy", "category": "Trees"},
        {"id": 127, "title": "Binary Search", "difficulty": "Easy", "category": "Arrays"},
        {"id": 128, "title": "Majority Element", "difficulty": "Easy", "category": "Arrays"},
        {"id": 129, "title": "Move Zeroes", "difficulty": "Easy", "category": "Arrays"},
        {"id": 130, "title": "Missing Number", "difficulty": "Easy", "category": "Arrays"},
        {"id": 131, "title": "Intersection of Two Arrays", "difficulty": "Easy", "category": "Arrays"},
        {"id": 132, "title": "Ransom Note", "difficulty": "Easy", "category": "Strings"},
        {"id": 133, "title": "Fizz Buzz", "difficulty": "Easy", "category": "Strings"},
        {"id": 134, "title": "Single Number", "difficulty": "Easy", "category": "Arrays"},
        {"id": 135, "title": "Palindrome Linked List", "difficulty": "Easy", "category": "Linked Lists"},
        {"id": 136, "title": "Diameter of Binary Tree", "difficulty": "Easy", "category": "Trees"},
        {"id": 137, "title": "Invert Binary Tree", "difficulty": "Easy", "category": "Trees"},
        {"id": 138, "title": "Valid Anagram", "difficulty": "Easy", "category": "Strings"},
        {"id": 139, "title": "Two Sum II - Input Array Is Sorted", "difficulty": "Easy", "category": "Arrays"},
        {"id": 140, "title": "Best Time to Buy and Sell Stock II", "difficulty": "Easy", "category": "Arrays"},
        {"id": 141, "title": "Merge Sorted Array", "difficulty": "Easy", "category": "Arrays"},
        {"id": 142, "title": "Pascal's Triangle", "difficulty": "Easy", "category": "Arrays"},
        {"id": 143, "title": "Pascal's Triangle II", "difficulty": "Easy", "category": "Arrays"},
        {"id": 144, "title": "Roman to Integer", "difficulty": "Easy", "category": "Math"},
        {"id": 145, "title": "Valid Palindrome", "difficulty": "Easy", "category": "Strings"},
        {"id": 146, "title": "Implement Queue using Stacks", "difficulty": "Easy", "category": "Stacks"},
        {"id": 147, "title": "Implement Stack using Queues", "difficulty": "Easy", "category": "Queues"},
        {"id": 148, "title": "Power of Two", "difficulty": "Easy", "category": "Bit Manipulation"},
        {"id": 149, "title": "Power of Three", "difficulty": "Easy", "category": "Math"},
        {"id": 150, "title": "Power of Four", "difficulty": "Easy", "category": "Bit Manipulation"}
    ]

    with open("data.json", "r+") as f:
        data = json.load(f)
        existing_ids = {problem['id'] for problem in data}
        problems_to_add = [p for p in new_problems if p['id'] not in existing_ids]

        for problem in problems_to_add:
            print(f"Fetching description for: {problem['title']}")
            prompt = f"Provide a description and optimal solution for the coding challenge: {problem['title']}. The optimal solution should be a brief explanation of the best approach to solve the problem. Format the output as 'Description: ... Optimal Solution: ...'"
            response = model.generate_content(prompt)
            try:
                if "Optimal Solution:" in response.text:
                    parts = response.text.split("Optimal Solution:")
                    description = parts[0].replace("Description:", "").strip()
                    optimal_solution = parts[1].strip()
                else:
                    description = response.text
                    optimal_solution = "Could not be generated."

                problem["description"] = description
                problem["optimal_solution"] = optimal_solution
                data.append(problem)
            except Exception as e:
                print(f"Error processing response for {problem['title']}: {e}")
                problem["description"] = "Error generating description."
                problem["optimal_solution"] = "Error generating optimal solution."
                data.append(problem)

        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=2)

    print("data.json has been updated with new problems.")

if __name__ == "__main__":
    add_problems()

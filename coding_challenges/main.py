import sys
import json
import subprocess
import os
import threading
import signal
import google.generativeai as genai
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QListWidgetItem, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QTextEdit, QLineEdit
)
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont, QKeyEvent
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import Qt

class CodeEditor(QTextEdit):
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Tab:
            self.insertPlainText("    ")
        else:
            super().keyPressEvent(event)

class PythonHighlighter(QSyntaxHighlighter):
    """
    A syntax highlighter for Python code.
    """
    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)

        self.highlightingRules = []

        # Keyword format
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor("#FF79C6"))
        keywordFormat.setFontWeight(QFont.Bold)
        keywords = [
            r'\bbreak\b', r'\bcontinue\b', r'\bdef\b', r'\belif\b',
            r'\belse\b', r'\bexcept\b', r'\bfinally\b', r'\bfor\b',
            r'\bfrom\b', r'\bglobal\b', r'\bif\b', r'\bimport\b',
            r'\bin\b', r'\bis\b', r'\blambda\b', r'\bnonlocal\b',
            r'\bnot\b', r'\bor\b', r'\bpass\b', r'\braise\b',
            r'\breturn\b', r'\btry\b', r'\bwhile\b', r'\bwith\b',
            r'\byield\b', r'\bclass\b', r'\bas\b', r'\band\b',
            r'\bassert\b', r'\bdel\b', r'\bNone\b', r'\bTrue\b',
            r'\bFalse\b'
        ]
        for word in keywords:
            pattern = QRegExp(word)
            self.highlightingRules.append((pattern, keywordFormat))

        # 'self' format
        selfFormat = QTextCharFormat()
        selfFormat.setForeground(QColor("#BD93F9"))
        selfFormat.setFontWeight(QFont.Bold)
        self.highlightingRules.append((QRegExp(r'\bself\b'), selfFormat))

        # Decorator format
        decoratorFormat = QTextCharFormat()
        decoratorFormat.setForeground(QColor("#F1FA8C"))
        self.highlightingRules.append((QRegExp(r'@[A-Za-z0-9_]+'), decoratorFormat))

        # Single-line comment format
        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(QColor("#6272A4"))
        self.highlightingRules.append((QRegExp(r'#[^\n]*'), singleLineCommentFormat))

        # Quotation format for single-line strings
        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(QColor("#50FA7B"))
        self.highlightingRules.append((QRegExp(r'"[^"\\]*"'), quotationFormat))
        self.highlightingRules.append((QRegExp(r"'[^'\\]*'",), quotationFormat))

        # Function and class name format
        functionFormat = QTextCharFormat()
        functionFormat.setForeground(QColor("#8BE9FD"))
        self.highlightingRules.append((QRegExp(r'\b[A-Za-z0-9_]+(?=\()'), functionFormat))

        # Numbers
        numberFormat = QTextCharFormat()
        numberFormat.setForeground(QColor("#FFB86C"))
        self.highlightingRules.append((QRegExp(r'\b[0-9]+\.?[0-9]*\b'), numberFormat))

        # Multi-line strings (triple quotes)
        self.tri_single = (QRegExp(r"'''"), 1, quotationFormat)
        self.tri_double = (QRegExp(r'"""'), 2, quotationFormat)

    def highlightBlock(self, text):
        """
        Applies syntax highlighting to the given block of text.
        """
        # Apply single-line rules
        for pattern, format in self.highlightingRules:
            expression = pattern
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Handle multi-line strings ('''...''')
        self.apply_multiline_rule(text, self.tri_single[0], 1, self.tri_single[2])
        # Handle multi-line strings ("""...")
        self.apply_multiline_rule(text, self.tri_double[0], 2, self.tri_double[2])

    def apply_multiline_rule(self, text, delimiter, state, format):
        """
        Helper function to apply rules for multi-line constructs.
        """
        startIndex = 0
        if self.previousBlockState() != state:
            startIndex = delimiter.indexIn(text)

        while startIndex >= 0:
            endIndex = delimiter.indexIn(text, startIndex + 1)
            if endIndex == -1:
                self.setCurrentBlockState(state)
                length = len(text) - startIndex
            else:
                length = endIndex - startIndex + delimiter.matchedLength()
            
            self.setFormat(startIndex, length, format)
            startIndex = delimiter.indexIn(text, startIndex + length)



class ChallengeStatus:

    NOT_STARTED = "Not Started"
    INCOMPLETE = "Incomplete"
    COMPLETED = "Completed"

class CodingChallengesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coding Challenges")
        self.setGeometry(100, 100, 1200, 800)

        self.setStyleSheet("""
            QWidget { background-color: #2E2E2E; color: #CCCCCC; }
            QComboBox, QLineEdit, QTextEdit { background-color: #3E3E3E; color: #F2F2F2; }
            QPushButton { background-color: #4A4A4A; color: #F2F2F2; border: 1px solid #6E6E6E; }
            QPushButton:hover { background-color: #5A5A5A; border: 1px solid #8E8E8E; }
            QListWidget { background-color: #3E3E3E; border: none; }
            QListWidget::item:selected { background-color: #5A5A5A; }
        """)

        self.challenges = self.load_challenges()
        self.progress = self.load_progress()
        self.challenge_items = {}

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        self.model = None
        try:
            genai.configure(api_key=os.environ["GEMINI_API_KEY"])
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        except KeyError:
            pass

        self.setup_left_panel()
        self.setup_right_panel()

        if not self.model:
            self.test_results.setText("Error: GEMINI_API_KEY environment variable not set.")

    def load_challenges(self):
        with open("data.json", "r") as f:
            return json.load(f)

    def load_progress(self):
        try:
            with open("progress.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_progress(self):
        with open("progress.json", "w") as f:
            json.dump(self.progress, f)

    def setup_left_panel(self):
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        filter_layout = QHBoxLayout()
        self.difficulty_filter = QComboBox()
        self.difficulty_filter.addItems(["All", "Easy", "Medium", "Hard"])
        self.difficulty_filter.currentTextChanged.connect(self.filter_challenges)
        filter_layout.addWidget(QLabel("Difficulty:"))
        filter_layout.addWidget(self.difficulty_filter)

        self.category_filter = QComboBox()
        self.category_filter.addItems(["All"] + sorted(list(set(c["category"] for c in self.challenges))))
        self.category_filter.currentTextChanged.connect(self.filter_challenges)
        filter_layout.addWidget(QLabel("Category:"))
        filter_layout.addWidget(self.category_filter)

        self.status_filter = QComboBox()
        self.status_filter.addItems(["All", "Not Started", "Incomplete", "Completed"])
        self.status_filter.currentTextChanged.connect(self.filter_challenges)
        filter_layout.addWidget(QLabel("Status:"))
        filter_layout.addWidget(self.status_filter)

        left_layout.addLayout(filter_layout)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search by name...")
        self.search_bar.textChanged.connect(self.filter_challenges)
        left_layout.addWidget(self.search_bar)

        self.challenge_list = QListWidget()
        self.challenge_list.currentRowChanged.connect(self.display_challenge)
        left_layout.addWidget(self.challenge_list)

        self.layout.addWidget(left_panel, 1)
        self.populate_challenge_list()

    def setup_right_panel(self):
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        self.challenge_title = QLabel("Select a Challenge")
        right_layout.addWidget(self.challenge_title)

        self.challenge_description = QTextEdit()
        self.challenge_description.setReadOnly(True)
        right_layout.addWidget(self.challenge_description)

        self.code_editor = CodeEditor()
        self.highlighter = PythonHighlighter(self.code_editor.document())
        right_layout.addWidget(self.code_editor)

        button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run Tests")
        self.run_button.clicked.connect(self.run_tests)
        button_layout.addWidget(self.run_button)

        self.analyze_button = QPushButton("Analyze with Gemini")
        self.analyze_button.clicked.connect(self.analyze_with_gemini)
        button_layout.addWidget(self.analyze_button)

        self.solution_button = QPushButton("Show Solution")
        self.solution_button.clicked.connect(self.ask_gemini_for_solution)
        button_layout.addWidget(self.solution_button)

        self.hint_button = QPushButton("Show Hint")
        self.hint_button.clicked.connect(self.ask_gemini_for_hint)
        button_layout.addWidget(self.hint_button)

        right_layout.addLayout(button_layout)

        self.test_results = QTextEdit()
        self.test_results.setReadOnly(True)
        right_layout.addWidget(self.test_results)

        self.layout.addWidget(right_panel, 2)

    def populate_challenge_list(self):
        self.challenge_list.clear()
        self.challenge_items.clear()
        for challenge in self.challenges:
            self.add_challenge_to_list(challenge)

    def add_challenge_to_list(self, challenge):
        status = self.progress.get(str(challenge["id"]), ChallengeStatus.NOT_STARTED)
        difficulty = challenge["difficulty"]
        color = "green" if difficulty == "Easy" else "orange" if difficulty == "Medium" else "red"

        title = challenge["title"]
        if status == ChallengeStatus.COMPLETED:
            title += " ✅"

        item_widget = QLabel(f'{title} - {status} - <font color=\'{color}\'>{difficulty}</font>')
        item = QListWidgetItem(self.challenge_list)
        item.setData(1, challenge)
        self.challenge_list.addItem(item)
        self.challenge_list.setItemWidget(item, item_widget)
        item.setSizeHint(item_widget.sizeHint())
        self.challenge_items[challenge["id"]] = item

    def filter_challenges(self):
        self.challenge_list.clear()
        for challenge in self.challenges:
            challenge_status = self.progress.get(str(challenge["id"]), ChallengeStatus.NOT_STARTED)
            difficulty = challenge["difficulty"]
            difficulty_filter_val = self.difficulty_filter.currentText()
            category_filter_val = self.category_filter.currentText()
            status_filter_val = self.status_filter.currentText()
            search_text = self.search_bar.text().lower()

            if (difficulty_filter_val == "All" or difficulty == difficulty_filter_val) and \
               (category_filter_val == "All" or challenge["category"] == category_filter_val) and \
               (status_filter_val == "All" or challenge_status == status_filter_val) and \
               (search_text in challenge["title"].lower()):
                self.add_challenge_to_list(challenge)

    def display_challenge(self, row):
        item = self.challenge_list.item(row)
        if not item:
            return

        challenge = item.data(1)
        self.challenge_title.setText(challenge["title"])
        self.challenge_description.setText(challenge["description"])
        try:
            with open(f'solutions/solution_{challenge["id"]}.py', "r") as f:
                self.code_editor.setPlainText(f.read())
        except FileNotFoundError:
            self.code_editor.clear()

    def run_tests(self):
        self.test_results.clear()
        current_item = self.challenge_list.currentItem()
        if not current_item:
            return

        challenge = current_item.data(1)
        solution_code = self.code_editor.toPlainText()

        solution_file_path = f'solutions/solution_{challenge["id"]}.py'
        with open(solution_file_path, "w") as f:
            f.write(solution_code)

        test_file_path = f'tests/test_{challenge["title"].lower().replace(" ", "_")}.py'
        result = subprocess.run([sys.executable, "-m", "pytest", test_file_path], capture_output=True, text=True)

        self.test_results.setText(result.stdout + result.stderr)

        new_status = ChallengeStatus.INCOMPLETE
        if result.returncode == 0:
            new_status = ChallengeStatus.COMPLETED
        elif not solution_code.strip():
            new_status = ChallengeStatus.NOT_STARTED

        self.progress[str(challenge["id"])] = new_status
        self.save_progress()
        self.update_challenge_list_item(challenge)

    def analyze_with_gemini(self):
        self.test_results.clear()
        current_item = self.challenge_list.currentItem()
        if not current_item:
            return

        challenge = current_item.data(1)
        solution_code = self.code_editor.toPlainText()

        test_file_path = f'tests/test_{challenge["title"].lower().replace(" ", "_")}.py'
        result = subprocess.run([sys.executable, "-m", "pytest", test_file_path], capture_output=True, text=True)

        if result.returncode == 0:
            self.analyze_solution(challenge, solution_code, True)
        else:
            self.analyze_solution(challenge, solution_code, False)

    def analyze_solution(self, challenge, solution_code, is_correct):
        if not self.model:
            self.test_results.setText("Gemini API not configured. Please set the GEMINI_API_KEY environment variable.")
            return

        if is_correct:
            prompt = f'''Analyze the time and space complexity of the following Python solution for the '{challenge["title"]}' problem.\n\nProblem Description:\n{challenge["description"]}\n\nSolution:\n```python\n{solution_code}```\n\nFinally, provide a judgement on whether this is an optimal solution to the problem and why.'''
        else:
            prompt = f'''The following Python solution for the '{challenge["title"]}' problem is incorrect. Please provide a subtle hint to guide the user toward the correct solution without giving away the answer.\n\nProblem Description:\n{challenge["description"]}\n\nIncorrect Solution:\n```python\n{solution_code}```'''

        try:
            response = self.model.generate_content(prompt)
            self.test_results.setText(response.text)
        except Exception as e:
            self.test_results.setText(f"Error analyzing solution: {e}")

    def ask_gemini_for_solution(self):
        self.test_results.clear()
        current_item = self.challenge_list.currentItem()
        if not current_item:
            return

        challenge = current_item.data(1)
        challenge_id = str(challenge["id"])

        with open("solutions.json", "r") as f:
            solutions = json.load(f)

        if challenge_id in solutions:
            self.test_results.setText(solutions[challenge_id])
        else:
            self.test_results.setText("Solution not found.")

    def ask_gemini_for_hint(self):
        self.test_results.clear()
        current_item = self.challenge_list.currentItem()
        if not current_item:
            return

        challenge = current_item.data(1)
        challenge_id = str(challenge["id"])

        try:
            with open("hints.json", "r") as f:
                hints = json.load(f)
        except FileNotFoundError:
            hints = {}

        if challenge_id in hints:
            self.test_results.setText(hints[challenge_id])
            return

        if not self.model:
            self.test_results.setText("Gemini API not configured. Please set the GEMINI_API_KEY environment variable.")
            return

        prompt = f'''Provide a subtle hint for the following Python problem:\n\nProblem Description:\n{challenge["description"]}'''

        try:
            response = self.model.generate_content(prompt)
            hint_text = f"{response.text}\n"
            hints[challenge_id] = hint_text
            with open("hints.json", "w") as f:
                json.dump(hints, f, indent=4)
            self.test_results.setText(hint_text)
        except Exception as e:
            self.test_results.setText(f"Error generating hint: {e}")

    def update_challenge_list_item(self, challenge):
        item = self.challenge_items.get(challenge["id"])
        if not item:
            return

        status = self.progress.get(str(challenge["id"]), ChallengeStatus.NOT_STARTED)
        difficulty = challenge["difficulty"]
        color = "green" if difficulty == "Easy" else "orange" if difficulty == "Medium" else "red"

        title = challenge["title"]
        if status == ChallengeStatus.COMPLETED:
            title += " ✅"

        item_widget = QLabel(f"{title} - {status} - <font color='{color}'>{difficulty}</font>")
        self.challenge_list.setItemWidget(item, item_widget)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    main_app = CodingChallengesApp()
    main_app.show()
    sys.exit(app.exec_())
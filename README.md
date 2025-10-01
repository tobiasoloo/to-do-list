# To-Do List with AI Suggestions

This is a simple command-line **to-do list manager** written in Python. It allows you to add, list, and complete tasks, while also providing **AI-powered task suggestions** using OpenAI's API.  

## Features  
- ✅ Add tasks with a description  
- 📋 List all tasks with completion status  
- ✔️ Mark tasks as completed  
- 🤖 Get AI suggestions on which task to do next (using OpenAI)  

## Requirements  
- Python 3.8+  
- [OpenAI Python SDK](https://github.com/openai/openai-python)  

Install dependencies:  
```bash
pip install openai
```

## Setup  
1. Clone or download this repository.  
2. Install dependencies as shown above.  
3. Set your OpenAI API key as an environment variable:  
   ```bash
   export OPENAI_API_KEY="your_api_key_here"   # Linux/Mac
   setx OPENAI_API_KEY "your_api_key_here"     # Windows PowerShell
   ```

## Usage  
Run the script:  
```bash
python eb8a4316-e896-4568-914f-97ab7d0eac69.py
```

You’ll see the main menu:  
```
Options: [1] Add [2] List [3] Complete [4] Suggest [0] Exit
```

---

## Example Workflow  

### 1. Add a Task  
```
Options: [1] Add [2] List [3] Complete [4] Suggest [0] Exit
Enter choice: 1
Enter task description: Finish project report
Task 1 added: Finish project report
```

### 2. List Tasks  
```
Options: [1] Add [2] List [3] Complete [4] Suggest [0] Exit
Enter choice: 2
1. Finish project report [❌]
```

### 3. Mark a Task as Completed  
```
Options: [1] Add [2] List [3] Complete [4] Suggest [0] Exit
Enter choice: 3
Enter task id to complete: 1
Task 1 marked done.
```

### 4. Get AI Suggestion  
```
Options: [1] Add [2] List [3] Complete [4] Suggest [0] Exit
Enter choice: 4
Suggestion from AI:
You should prioritize writing your research notes first, since it will help structure the final report.
```

### 5. Exit the Program  
```
Options: [1] Add [2] List [3] Complete [4] Suggest [0] Exit
Enter choice: 0
Goodbye!
```

---

## Notes  
- The **AI suggestion feature** requires an active OpenAI API key.  
- If no tasks are available, suggestions will not work.  
- The model used is `gpt-4o-mini` for efficiency and speed.  


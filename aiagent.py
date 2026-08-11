from database import DBHelper
from config import gemini_client
import datetime


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

db_helper = DBHelper()
db_helper.select_collection(collection_name="tasks")


# ============================================================
# SAVE TASK TO MONGODB
# ============================================================

def save_task(task):
    """
    Save a task to MongoDB Atlas.
    """

    # Add system fields
    task["status"] = "pending"
    task["created_at"] = datetime.datetime.now()

    # Save task
    db_helper.save(task)

    # Confirmation message
    return (
        "Task saved successfully as **pending**\n\n"
        f"**Action:** {task.get('action', '')}\n\n"
        f"**Title:** {task.get('title', '')}\n\n"
        f"**Contact Name:** {task.get('name', '')}\n\n"
        f"**Description:** {task.get('description', '')}\n"
    )


# ============================================================
# GEMINI FUNCTION DEFINITION
# ============================================================

tools = [
    {
        "name": "save_task",
        "description": (
            "Save a task in MongoDB Atlas. "
            "Use this when the user wants to create a task, "
            "reminder, call, email, message, or other action."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Short title of the task."
                },
                "description": {
                    "type": "string",
                    "description": "Detailed description of the task."
                },
                "name": {
                    "type": "string",
                    "description": "Name of the contact person if provided."
                },
                "action": {
                    "type": "string",
                    "enum": [
                        "call",
                        "email",
                        "message",
                        "other"
                    ],
                    "description": "Action that needs to be performed."
                }
            },
            "required": [
                "title",
                "description",
                "action"
            ]
        }
    }
]


# ============================================================
# EXTRACT USER TEXT
# ============================================================

def extract_user_text(input_list):
    """
    Converts different input formats into plain text.

    Supported examples:

    1.
    [
        {
            "role": "user",
            "content": "Call Jashan tomorrow"
        }
    ]

    2.
    "Call Jashan tomorrow"

    3.
    [
        "Call Jashan tomorrow"
    ]
    """

    # If input is already a string
    if isinstance(input_list, str):
        return input_list.strip()

    # If input is a list
    if isinstance(input_list, list):

        messages = []

        for item in input_list:

            # Dictionary message
            if isinstance(item, dict):

                content = item.get("content")

                if content is not None:
                    messages.append(str(content))

            # Plain text item
            else:
                messages.append(str(item))

        return "\n".join(messages).strip()

    # Any other type
    return str(input_list).strip()


# ============================================================
# MAIN AGENTIC SAVE FUNCTION
# ============================================================

def agentic_save(input_list):
    """
    Main AI agent for the Save Task page.

    Receives user input, sends it to Gemini,
    handles the function call, and saves the task.
    """

    # --------------------------------------------------------
    # Convert input into normal text
    # --------------------------------------------------------

    user_text = extract_user_text(input_list)

    if not user_text:
        return "Please enter a task."


    # --------------------------------------------------------
    # Gemini prompt
    # --------------------------------------------------------

    prompt = f"""
You are Veltrix AI, an intelligent task-saving assistant.

Your job is to understand the user's request and create a task.

When the user wants to create a task, reminder, call,
email, message, or other action, ALWAYS use the save_task function.

Extract these fields:

- title
- description
- name
- action

The action MUST be exactly one of:

call
email
message
other

Rules:

1. Do not invent information.
2. If a contact name is provided, put it in name.
3. If a phone number is provided, preserve it in description.
4. Keep the user's requested task meaning intact.
5. Create a short and useful title.
6. Put the complete task details in description.
7. If no contact name is provided, leave name empty.
8. Use "other" when the requested action is not a call,
   email, or message.

User's request:

{user_text}
"""


    # --------------------------------------------------------
    # Call Gemini
    # --------------------------------------------------------

    try:

        response = gemini_client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config={
                "tools": [
                    {
                        "function_declarations": tools
                    }
                ]
            }
        )

    except Exception as e:

        return (
            "Gemini API error:\n\n"
            f"{str(e)}"
        )


    # --------------------------------------------------------
    # Check response
    # --------------------------------------------------------

    if not response or not response.candidates:
        return "Sorry, I could not process your request."


    # --------------------------------------------------------
    # Find function call
    # --------------------------------------------------------

    for candidate in response.candidates:

        if not candidate.content:
            continue

        if not candidate.content.parts:
            continue

        for part in candidate.content.parts:

            # Check whether Gemini called a function
            if part.function_call:

                function_name = part.function_call.name

                # Convert Gemini arguments to Python dictionary
                arguments = dict(part.function_call.args)


                # ====================================================
                # SAVE TASK
                # ====================================================

                if function_name == "save_task":

                    # Preserve original user request
                    arguments["user_original_text"] = user_text

                    # Make sure optional name exists
                    if "name" not in arguments:
                        arguments["name"] = ""

                    # Save to MongoDB
                    return save_task(arguments)


                # ====================================================
                # FUTURE FUNCTIONS
                # ====================================================

                elif function_name == "update_task":

                    return (
                        "Update task functionality "
                        "is not implemented yet."
                    )


                elif function_name == "delete_task":

                    return (
                        "Delete task functionality "
                        "is not implemented yet."
                    )


                elif function_name == "list_tasks":

                    return (
                        "List tasks functionality "
                        "is not implemented yet."
                    )


    # --------------------------------------------------------
    # No function call
    # --------------------------------------------------------

    try:

        if response.text:
            return response.text

    except Exception:
        pass


    return "Sorry, I could not understand the task."


import panel as pn
pn.extension()

# Predefined question-answer pairs
qa_pairs = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there!",
    "how are you": "I'm doing great, thanks!",
    "what is your name": "I'm a simple chatbot created by you.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "who created you": "I was built by a kind developer!",
    "what can you do": "I can answer simple questions you ask me!"
}

# GUI Widgets
inp = pn.widgets.TextInput(placeholder="Ask me something...")
button_conversation = pn.widgets.Button(name="Ask!")
context = []

# Simple rule-based response generator
def get_response(user_input):
    user_input = user_input.lower().strip()
    for question in qa_pairs:
        if question in user_input:
            return qa_pairs[question]
    return "Sorry, I didn't understand that. Try asking something else."

# Event function
def collect_messages(event):
    user_input = inp.value
    bot_response = get_response(user_input)

    context.append({'role': 'user', 'content': user_input})
    context.append({'role': 'bot', 'content': bot_response})
    
    inp.value = ""

    conversation = "\n\n".join([f"**{msg['role'].capitalize()}**: {msg['content']}" for msg in context])
    return pn.pane.Markdown(conversation)

# Bind button click
interactive_conversation = pn.bind(collect_messages, button_conversation)

# Layout
dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True)
)

# Serve the app
pn.serve(dashboard, show=True)

import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize chatbot
chatbot = ChatBot(
    'StudyHelper',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///:memory:',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.85,
            'default_response': "I'm not sure how to help with that. Can you ask in another way?"
        }
    ],
    read_only=True
)

# Dynamically scale conversation pairs using templates
subjects = ["math", "science", "history", "biology", "chemistry", "English"]
topics = ["homework", "projects", "quizzes", "studying", "reading"]
actions = ["study", "prepare", "focus", "understand", "memorize"]
greetings = ["Hi", "Hello", "Hey", "Yo", "Greetings", "Good morning", "Good evening"]

focused_data = []

# Generate conversational pairs for greetings
for greet in greetings:
    focused_data.append(greet)
    focused_data.append(random.choice([
        "Hi there! Ready to learn?",
        "Hey! What subject are you working on?",
        "Hello! Let’s crush some homework.",
        "Welcome! Ask me anything."
    ]))

# Generate academic help templates
for subject in subjects:
    for action in actions:
        focused_data.append(f"How do I {action} for {subject}?")
        focused_data.append(f"To {action} for {subject}, set clear goals and break it into small tasks.")
        focused_data.append(f"I struggle with {subject}")
        focused_data.append(f"Let's tackle {subject} step-by-step. Want tips?")

# Add question variations
question_words = ["Why", "What", "Who", "How"]
for word in question_words:
    for _ in range(30):
        focused_data.append(word)
        focused_data.append(f"Good question! Could you give me a bit more info to help with that '{word}'?")

# Add filler small talk and generic help paths
for _ in range(100):
    focused_data.append("Can you help me?")
    focused_data.append("Absolutely! What do you need help with?")
    focused_data.append("I’m confused")
    focused_data.append("That's okay — let’s walk through it together.")
    focused_data.append("I’m bored")
    focused_data.append("Want a fun science fact or a quick brain teaser?")
    focused_data.append("Tell me something cool")
    focused_data.append("Did you know octopuses have three hearts?")

# Add follow-up encouragement
for _ in range(100):
    focused_data.append("Thanks")
    focused_data.append("Anytime! Keep up the great work.")
    focused_data.append("That helped")
    focused_data.append("I’m glad! Want to explore another topic?")
    focused_data.append("Goodbye")
    focused_data.append("Take care! You’ve got this.")

# Add specialized school issue conversations
school_issues = [
    ("I forgot my homework", "It happens! Let’s plan how to stay on top of things next time."),
    ("I didn’t study for my test", "Let’s focus on learning from this. Want tips for quick review methods?"),
    ("I failed a quiz", "That’s okay. Failing is part of learning. Want help reviewing the material?"),
    ("My teacher is too strict", "That’s tough. Let’s talk about how you can still succeed in their class."),
    ("I get nervous when called on", "Many students do! Want strategies to feel more confident in class?"),
    ("I don’t have time to study", "Let’s find small windows in your day to fit in learning."),
    ("My grades are dropping", "Let’s find out why and work together on a plan to bring them up."),
    ("I hate group projects", "You’re not alone. Want advice on how to handle them better?"),
    ("I feel like school is too much", "You’re not alone. Let’s talk about how to reduce the pressure."),
    ("I’m always tired at school", "Let’s think about your sleep and energy habits. Want tips?"),
    ("I can't focus in class", "That’s frustrating. Want to try some focus techniques that might help?")
]

for issue, response in school_issues:
    focused_data.append(issue)
    focused_data.append(response)

# Train the bot
trainer = ListTrainer(chatbot)
# Add contextual follow-up responses
follow_ups = [
    ("Yes", "Great! Let's get started."),
    ("No", "No worries. Let me know if you change your mind."),
    ("Maybe", "Take your time — I'm here whenever you're ready."),
    ("Math", "Let's tackle math step-by-step. Want help with addition, algebra, or geometry?"),
    ("Science", "Science is full of cool stuff! Want to explore biology, physics, or chemistry?"),
    ("What is 1 + 1", "1 + 1 is 2."),
    ("What is 2 + 2", "2 + 2 is 4."),
    ("What is 3 x 4", "3 times 4 is 12."),
    ("What is 10 divided by 2", "10 divided by 2 is 5."),
    ("Tell me a joke", "Why did the student eat his homework? Because the teacher told him it was a piece of cake!"),
    ("That's funny", "Glad you liked it! Want another one?"),
    ("Yes please", "Okay! What did one pencil say to the other? You're looking sharp today!")
]

for q, a in follow_ups:
    focused_data.append(q)
    focused_data.append(a)

# Add subject-specific tutoring prompts
subject_questions = [
    ("What is the quadratic formula?", "The quadratic formula is x = (-b ± √(b² - 4ac)) / 2a."),
    ("What is the Pythagorean theorem?", "The Pythagorean theorem states that a² + b² = c² for right triangles."),
    ("Who discovered gravity?", "Isaac Newton is credited with discovering gravity when he saw an apple fall."),
    ("What is photosynthesis?", "Photosynthesis is the process plants use to convert sunlight into energy."),
    ("What is the water cycle?", "The water cycle includes evaporation, condensation, precipitation, and collection."),
    ("Who wrote Romeo and Juliet?", "William Shakespeare wrote Romeo and Juliet."),
    ("What is a metaphor?", "A metaphor is a figure of speech that directly compares two unrelated things."),
    ("What is a noun?", "A noun is a person, place, thing, or idea."),
    ("What is 5 squared?", "5 squared is 25."),
    ("What is 7 x 6?", "7 times 6 is 42."),
    ("Define osmosis", "Osmosis is the diffusion of water across a semipermeable membrane."),
    ("Explain photosynthesis in simple terms", "Plants use sunlight, water, and carbon dioxide to make their food and release oxygen."),
    ("What is an atom?", "An atom is the smallest unit of ordinary matter."),
    ("How do you find area of a rectangle?", "Area = length × width."),
    ("Explain supply and demand", "Supply is how much is available, demand is how much people want it. Price is affected by both.")
]

for q, a in subject_questions:
    focused_data.append(q)
    focused_data.append(a)

# Add advanced subjects and expanded basic knowledge
advanced_topics = [
    ("What is supply chain management?", "Supply chain management involves managing the flow of goods, data, and finances related to a product or service."),
    ("What is an algorithm?", "An algorithm is a set of rules or instructions designed to perform a task or solve a problem."),
    ("What is object-oriented programming?", "OOP is a programming paradigm based on the concept of objects, which contain data and methods."),
    ("What is a sonnet?", "A sonnet is a 14-line poem written in iambic pentameter, often exploring themes of love or philosophy."),
    ("What is a haiku?", "A haiku is a three-line poem with a 5-7-5 syllable structure, often about nature."),
    ("Who was Ada Lovelace?", "Ada Lovelace was a 19th-century mathematician known as the first computer programmer."),
    ("What is an economy?", "An economy is a system for producing, distributing, and consuming goods and services."),
    ("Define inflation", "Inflation is the rate at which the general level of prices for goods and services rises."),
    ("What is a variable in programming?", "A variable stores data values that can change when the program runs."),
    ("What is recursion?", "Recursion is when a function calls itself to solve smaller instances of a problem."),
    ("What is GDP?", "GDP stands for Gross Domestic Product, the total value of goods and services produced in a country."),
    ("Define democracy", "Democracy is a system of government where the citizens exercise power by voting."),
    ("What is a thesis statement?", "A thesis statement summarizes the main point or claim of an essay or paper."),
    ("How do you write a conclusion?", "Summarize your key points and restate the thesis in a new way to wrap up your argument."),
    ("What is the scientific method?", "A systematic process for asking and answering questions through observation and experiment.")
]

for q, a in advanced_topics:
    focused_data.append(q)
    focused_data.append(a)

# Add deeper contextual connections and follow-ups
conversational_flows = [
    ("Addition", "Sure! Let's start with simple sums like 1 + 1 = 2. Want to try a problem?"),
    ("Algebra", "Algebra is about solving equations with variables. Want to try a basic one?"),
    ("Geometry", "Geometry deals with shapes, angles, and areas. Want help finding the area of a shape?"),
    ("Biology", "Biology is the study of living things. Want to talk about cells or organisms?"),
    ("Chemistry", "Chemistry explains matter and reactions. Interested in atoms or the periodic table?"),
    ("Physics", "Physics explores motion, energy, and forces. Want a quick example?"),
    ("What about it", "Let’s go deeper! Are you asking for a definition, example, or fun fact?"),
    ("What about science", "Science is a huge field. Are you asking about biology, chemistry, or physics?"),
    ("Tell me more", "Sure! Do you want more detail, an example, or a practice question?"),
    ("Give me an example", "Okay! Would you like math, science, or grammar examples?")
]

for q, a in conversational_flows:
    focused_data.append(q)
    focused_data.append(a)

# Add natural question variations and clarifications
clarifying_questions = [
    ("What do you mean?", "I mean, would you like a definition, a fun fact, or a specific example?"),
    ("Can you explain that more?", "Sure! Want a simpler explanation or an example?"),
    ("What else?", "I can share more! Would you prefer a practice question or another fact?"),
    ("Can you give me more?", "Of course. Would a quiz, example, or fact help more?"),
    ("I don't get it", "No problem! Let's try a simpler example or rephrase it."),
    ("That doesn’t help", "Let's approach it differently. Want a basic breakdown or new example?"),
    ("Explain more", "Sure! Would you like to go deeper with facts or examples?")
]

for q, a in clarifying_questions:
    focused_data.append(q)
    focused_data.append(a)

trainer.train(focused_data)

# Simulate basic context memory
user_preferences = {}
last_topic = None

# Start interactive chat
print("\n📚 Study Helper Chatbot is ready! Type 'exit' to quit.\n")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("StudyBot: Goodbye and good luck with your studies!")
            break
        # Context memory logic
        # Fuzzy keyword and pattern routing to fix phrasing issues
        simplified_input = user_input.lower().strip().replace("?", "").replace("what about", "").replace("tell me", "").replace("can you", "").replace("explain", "").replace("more about", "").strip()

        # Direct redirect for simplified known topics
        topic_map = {
            "science": "Science",
            "math": "Math",
            "biology": "Biology",
            "algebra": "Algebra",
            "addition": "Addition",
            "geometry": "Geometry",
            "chemistry": "Chemistry",
            "physics": "Physics",
            "english": "English",
            "history": "History",
        }

        chat_input = topic_map[simplified_input] if simplified_input in topic_map else user_input

        response = chatbot.get_response(chat_input)

        # Fallback suggestions for low-confidence replies
        if hasattr(response, 'confidence') and response.confidence < 0.4:
            suggestions = [topic.title() for topic in topic_map.keys() if topic in user_input.lower() or topic[:4] in user_input.lower()]
            if suggestions:
                suggestion_text = ", ".join(suggestions)
                print(f"StudyBot: I'm not sure how to help with that. Did you mean one of these topics? {suggestion_text}?")
                continue
        # Fallback suggestions for unmatched input
        if response.confidence < 0.4:
            suggestions = [topic.title() for topic in topic_map.keys() if topic in user_input.lower() or topic[:4] in user_input.lower()]
            if suggestions:
                suggestion_text = ", ".join(suggestions)
                print(f"StudyBot: I'm not sure how to help with that. Did you mean one of these topics? {suggestion_text}?")
                continue

        # Track preferences
        if user_input.lower().startswith("i like"):
            preference = user_input.lower().replace("i like", "").strip()
            user_preferences[preference] = user_preferences.get(preference, 0) + 1
            print(f"StudyBot: Got it! I'll try to include more about {preference} when possible.")
            continue

        if user_input.lower().startswith("my favorite subject is"):
            preference = user_input.lower().replace("my favorite subject is", "").strip()
            user_preferences[preference] = user_preferences.get(preference, 0) + 1
            print(f"StudyBot: Awesome! I’ll remember that you like {preference}.")
            continue

        if user_input.lower() == "what do i like":
            if user_preferences:
                prefs = ", ".join([f"{k} ({v})" for k, v in user_preferences.items()])
                print(f"StudyBot: You’ve mentioned liking: {prefs}.")
            else:
                print("StudyBot: I’m not sure yet — tell me what you like!")
            continue
        if last_topic and user_input.lower() in ["yes", "sure", "okay"]:
            print(f"StudyBot: Great! Let's keep going with {last_topic}.")
            continue
        if any(keyword in user_input.lower() for keyword in subjects):
            last_topic = user_input.lower()

        response = chatbot.get_response(user_input)
        print(f"StudyBot: {response}")
    except (KeyboardInterrupt, EOFError):
        print("\nStudyBot: Session ended.")
        break

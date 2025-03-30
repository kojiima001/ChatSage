# Simple Chatbot with JSON Knowledge Base

This is a Python-based chatbot that retrieves answers from a JSON file. If the answer is not found, it informs the user. The bot also supports learning by updating the knowledge base.

## Features
- Answers user questions based on `knowledge_base.json`
- Supports adding new knowledge
- Simple and lightweight

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/chatbot-project.git
   cd chatbot-project
   ```

2. Ensure you have Python installed (Python 3.x recommended).

## Running the Chatbot

1. Run the chatbot:
   ```sh
   python chatbot.py
   ```

2. The chatbot will prompt you to ask questions. If the answer is found in `knowledge_base.json`, it will be displayed.

## Testing the Chatbot

To test the bot separately, run:
```sh
python chatbot_test.py
```

## Adding New Knowledge

If the chatbot doesn't know an answer, modify `knowledge_base.json` manually or add functionality to let it learn dynamically.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is open-source under the MIT License.

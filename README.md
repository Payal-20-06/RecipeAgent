# 🍳 RecipeAgent — AI-Powered Recipe Finder

RecipeAgent is a Python-based AI agent built with **LangChain, Google Gemini, and Tavily Search**. It analyzes an image of food ingredients, identifies ingredients that may be present, searches the web for suitable recipes, and returns a recipe recommendation.

## ✨ Features

- **Image-based ingredient identification:** Select an image from your computer to identify visible ingredients.
- **AI-powered recipe recommendations:** Uses Google Gemini to understand the image and choose a suitable recipe.
- **Web search integration:** Uses Tavily Search to find recipes and relevant cooking information online.
- **Ingredient matching:** Finds recipes based on ingredients identified in the image.
- **Recipe instructions:** Presents recipe recommendations and cooking information in a readable format.
- **Local image selection:** Choose images from different folders on your computer.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Agent creation and tool orchestration |
| Google Gemini | Image understanding and recipe reasoning |
| Tavily Search | Web-based recipe discovery |
| `uv` | Python dependency and environment management |
| `python-dotenv` | Loading API credentials from environment variables |

## 📁 Project Structure

```text
RecipeAgent/
├── src/
│   └── recipeagent/
│       ├── __init__.py
│       ├── main.py
│       ├── prompt.py
│       ├── tools.py
│       └── photo_decoder.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## ⚙️ Prerequisites

Before running RecipeAgent, make sure you have:

- Python compatible with your project's dependencies
- [uv](https://docs.astral.sh/uv/)
- A Google Gemini API key
- A Tavily API key

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Payal-20-06/RecipeAgent.git
cd RecipeAgent
```

### 2. Install dependencies

If `uv.lock` is included in the repository:

```bash
uv sync
```

This creates or updates the project's virtual environment and installs the dependencies declared in `pyproject.toml`.

### 3. Configure environment variables

Create a `.env` file in the project root:

```dotenv
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the placeholders with your own credentials.

Get your credentials from:

- Google AI Studio: https://aistudio.google.com/
- Tavily: https://tavily.com/

**Security:** Never commit your `.env` file or expose API keys in your source code.

### 4. Run the application

From the project root, execute:

```bash
uv run python -m recipeagent.main
```

The application opens an image-selection dialog. Select a supported image file from your computer to begin the recipe discovery process.

## 🔄 How It Works

1. **Image selection:** The user chooses an image from their computer.
2. **Image processing:** The application reads the image and encodes it for the model request.
3. **Ingredient analysis:** Google Gemini analyzes the image and identifies possible ingredients.
4. **Recipe discovery:** The agent invokes the Tavily search tool to search for relevant recipes.
5. **Recipe selection:** The agent evaluates the search results and selects a suitable recipe.
6. **Final response:** The agent returns the recipe recommendation and cooking information.

## 🧩 Core Components

### `main.py`

Initializes the LangChain agent, selects an image, builds the user message, invokes the agent, and prints the final response.

### `prompt.py`

Defines the user prompt and system instructions that guide ingredient identification, web search, recipe selection, and response formatting.

### `tools.py`

Defines the Tavily-powered `web_search` tool used by the agent to retrieve recipe information from the web.

### `photo_decoder.py`

Handles local image selection, image validation, Base64 encoding, and construction of the image message.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key for Google Gemini |
| `TAVILY_API_KEY` | API key for Tavily Search |

Keep credentials private and use environment variables for configuration.

## 🛣️ Future Improvements

Potential enhancements for future versions include:

- Structured recipe output using Pydantic schemas
- Better recipe source attribution and ingredient matching
- Improved error handling and retry strategies
- Support for additional image formats
- A web interface for image uploads and recipe results
- Automated tests for image processing and search tools
- Recipe filtering by dietary preferences, cooking time, and available ingredients

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.

## 📄 License

No license has been specified yet. Add a license file before presenting the project as open source.

---

**Built with Python, LangChain, Google Gemini, and Tavily.**
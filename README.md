# Speak with PDF

Chat with multiple PDFs using AI-powered embeddings and conversational memory.

## 🚀 Vision
A smart AI assistant for students and professionals to extract insights from college textbooks, exam papers, and research documents, providing accurate answers with an interactive chat interface.

## 📌 Features
- Upload multiple PDF files and extract text
- Chunk text for efficient retrieval
- Use FAISS for vector-based search
- Leverage Google's Gemini AI for intelligent responses
- Maintain conversation history for better context
- Optimized for educational and research purposes

## 🛠️ Tech Stack
- **Python** (Core logic)
- **Streamlit** (Frontend UI)
- **FAISS** (Vector database for fast search)
- **Google Generative AI** (LLM and embeddings)
- **LangChain** (Efficient AI pipeline management)
- **PyPDF2** (PDF text extraction)

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/your-username/speak-with-pdf.git
cd speak-with-pdf

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## 🔑 Environment Variables
Create a `.env` file and add your Google API key:
```plaintext
GOOGLE_API_KEY=your_google_api_key
```

## 🚀 Running the Application
```bash
streamlit run app.py
```

## 🖼️ Usage Guide
1. Upload one or more PDF files from the sidebar.
2. Click on the **Process** button to extract and analyze text.
3. Ask questions about the content and receive intelligent responses.

## 🤖 How It Works
1. **Extract PDF text** using `PyPDF2`.
2. **Chunk text** into manageable pieces for better search performance.
3. **Create embeddings** using Google's Generative AI.
4. **Store vectors** in FAISS for quick retrieval.
5. **Enable conversation** with memory using Gemini AI.

## 📌 Future Enhancements
- Add support for other document types (DOCX, TXT, etc.).
- Improve UI with better visualization.
- Deploy on cloud platforms (Streamlit Sharing, AWS, or GCP).
- Integrate speech-to-text for voice-based interaction.
- Enhance AI model for better context understanding.

## 📜 License
MIT License

## 🤝 Contributing
Pull requests are welcome! If you have suggestions or improvements, feel free to fork the repo and submit a PR.

## 🌟 Acknowledgments
- **LangChain** for efficient LLM-based workflows.
- **Streamlit** for an easy-to-use UI.
- **Google Generative AI** for embeddings and chat capabilities.


# Physical AI Book Backend

FastAPI backend for the Physical AI Book chatbot.

## 🚀 Deploy to Render

1. Push this folder to GitHub as a separate repo
2. Go to https://render.com
3. Click **New** → **Web Service**
4. Connect your GitHub repo
5. Configure:
   - **Build Command**: `pip install -r requirements_simple.txt`
   - **Start Command**: `uvicorn main_simple:app --host 0.0.0.0 --port $PORT`
6. Add Environment Variable:
   - `OPENAI_API_KEY` = your OpenAI API key
7. Click **Create Web Service**

## 📝 Get Your Backend URL

After deployment, copy the URL (e.g., `https://your-backend.onrender.com`)

## 🔗 Connect to Frontend

Update `static/chatbot-widget-v2.js` in the frontend repo:

```javascript
const API_URL = 'https://your-backend.onrender.com';
```

## 🧪 Test Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `POST /query` - Ask questions

Example:
```bash
curl -X POST https://your-backend.onrender.com/query \
  -H "Content-Type: application/json" \
  -d '{"question":"What is Physical AI?"}'
```

## 🛠️ Local Development

```bash
# Install dependencies
pip install -r requirements_simple.txt

# Set environment variable
export OPENAI_API_KEY=your_key_here

# Run server
uvicorn main_simple:app --reload
```

Visit http://localhost:8000/docs for API documentation.

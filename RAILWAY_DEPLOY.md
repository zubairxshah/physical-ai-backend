# Deploy Backend on Railway.app

Railway is a modern deployment platform with excellent FastAPI support.

## 🚀 Quick Deploy

### Method 1: Deploy from GitHub (Recommended)

1. **Push to GitHub** (if not already done):
```bash
cd d:\PromptEng\hackathon\backend
git init
git add .
git commit -m "Backend for Physical AI Book"
git remote add origin https://github.com/zubairxshah/physical-ai-backend.git
git branch -M main
git push -u origin main
```

2. **Deploy on Railway**:
   - Go to https://railway.app
   - Click **Login** → Sign in with GitHub
   - Click **New Project**
   - Select **Deploy from GitHub repo**
   - Choose `physical-ai-backend` repository
   - Railway will auto-detect Python and deploy

3. **Add Environment Variable**:
   - Click on your service
   - Go to **Variables** tab
   - Click **+ New Variable**
   - Add: `OPENAI_API_KEY` = (your OpenAI API key)
   - Click **Add**

4. **Get Your URL**:
   - Go to **Settings** tab
   - Click **Generate Domain**
   - Copy the URL (e.g., `https://physical-ai-backend-production.up.railway.app`)

5. **Test**:
   - Visit: `https://your-url.up.railway.app/health`
   - Should return: `{"status":"ok","documents":0}`

### Method 2: Deploy with Railway CLI

1. **Install Railway CLI**:
```bash
npm i -g @railway/cli
```

2. **Login**:
```bash
railway login
```

3. **Initialize and Deploy**:
```bash
cd d:\PromptEng\hackathon\backend
railway init
railway up
```

4. **Add Environment Variable**:
```bash
railway variables set OPENAI_API_KEY=your_key_here
```

5. **Open in Browser**:
```bash
railway open
```

## 📝 Configuration Files

Railway uses these files (already created):
- `Procfile` - Defines start command
- `railway.json` - Railway-specific config
- `nixpacks.toml` - Build configuration
- `requirements_simple.txt` - Python dependencies

## 🔧 Update Frontend

After deployment, update your frontend:

1. Copy the Railway URL
2. Edit `static/chatbot-widget-v2.js` line 8:
```javascript
const API_URL = 'https://your-railway-url.up.railway.app';
```

3. Uncomment chatbot in `docusaurus.config.ts`:
```typescript
scripts: [
  {
    src: '/chatbot-widget-v2.js',
    async: true,
  },
],
```

4. Push frontend changes

## 💰 Pricing

- **Free Trial**: $5 credit (no credit card required initially)
- **Hobby Plan**: $5/month after trial
- **Usage-based**: Pay only for what you use

## 🐛 Troubleshooting

### Build fails?
- Check build logs in Railway dashboard
- Verify `requirements_simple.txt` exists
- Ensure Python 3.9+ is specified

### App crashes?
- Check runtime logs
- Verify `OPENAI_API_KEY` is set
- Test locally first: `uvicorn main_simple:app --reload`

### Can't access URL?
- Wait 2-3 minutes after deployment
- Check if domain is generated in Settings
- Verify service is running (green status)

## ✅ Advantages of Railway

- ✅ Auto-detects FastAPI
- ✅ Easy GitHub integration
- ✅ Automatic HTTPS
- ✅ Simple environment variables
- ✅ Great free tier
- ✅ Fast deployments

## 🔗 Useful Links

- Railway Dashboard: https://railway.app/dashboard
- Railway Docs: https://docs.railway.app
- Support: https://railway.app/discord

---

**Your backend is ready to deploy on Railway!** 🚀

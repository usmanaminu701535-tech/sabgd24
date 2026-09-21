# បក្សីកីឡា-SB24 Score Bot

A simple Telegram bot to check match scores, fixtures, and results for SB24.

## Features
- /today – Today's scores
- /fixtures – Upcoming matches
- /results – Latest results
- /help – Help message

## Commands
| Command | Description |
|---------|-------------|
| /start | Welcome message |
| /today | Today's scores |
| /fixtures | Upcoming matches |
| /results | Latest results |
| /help | Show help |

## Deployment (Railway)
1. Push this repo to GitHub.
2. Go to [Railway](https://railway.app) → New Project → Deploy from GitHub.
3. Select this repo.
4. In **Variables**, add:
   - `TELEGRAM_TOKEN` = your bot token from @BotFather
5. Railway will auto-detect the `Procfile` and start the worker.

## Updating Scores
Edit `scores.json` and push to GitHub. Railway will redeploy automatically.

## Notes
- No betting, gambling, or money features.
- Data is stored in a simple JSON file.

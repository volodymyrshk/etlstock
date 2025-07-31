# Simple Stock ETL Pipeline

This project is a simple ETL (Extract, Transform, Load) pipeline for stock market data.

## Architecture

The pipeline consists of three main components:

- **Extractor**: Fetches stock data from the Alpha Vantage API.
- **Transformer**: Cleans the data, calculates daily returns and moving averages.
- **Loader**: Loads the transformed data into a SQLite database.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/stock-etl-pipeline.git
   cd stock-etl-pipeline
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API key:**

   - Open `config/config.ini`.
   - Replace `YOUR_API_KEY` with your Alpha Vantage API key.

## Execution

To run the ETL pipeline, execute the following command:

```bash
python main.py
```

This will fetch the latest stock data, transform it, and load it into the `stock_data.db` SQLite database in the `data` directory.

## Automation

This pipeline can be automated using GitHub Actions or a cron job in a Dockerized environment.

### GitHub Actions

A sample GitHub Actions workflow is provided in `.github/workflows/main.yml`.

### Docker

A `Dockerfile` is provided to containerize the application. You can build and run the Docker container using the following commands:

```bash
# Build the Docker image
docker build -t stock-etl .

# Run the Docker container
docker run stock-etl
```

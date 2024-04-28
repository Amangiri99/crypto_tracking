CELERY_BEAT_SCHEDULE = {
    "scrap_data_from_coin_market": {
        "task": "scraper.tasks.scrape_data_from_coin_market",
        "schedule": 5.0,  # Execute every 5 seconds
        "description": "Scrape data from coin market every 5 seconds",
    },
}

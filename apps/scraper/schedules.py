CELERY_BEAT_SCHEDULE = {
    "scrap_data_from_coin_market": {
        "task": "apps.scraper.tasks.scrape_data_from_coin_market",
        "schedule": 60.0,  # Execute every 5 seconds
        "description": "Scrape data from coin market every 5 seconds",
    },
}

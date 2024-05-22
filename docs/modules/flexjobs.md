
```python
    flex_jobs = FlexJobs(search_query, location_query, min_jobs)
```

- Attributes

| Attribute        | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| `search_query`   | The search query to filter job listings.                          |
| `location_query` | The location query to filter job listings (defaults to '').       |
| `min_jobs`       | The maximum number of job listings to retrieve (defaults to 100). |

- Methods

| Method                                 | Description                                                                                                                               |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `get_jobs() -> list`                   | Retrieves job listings from FlexJobs website based on search and location queries. Returns a list of dictionaries containing job details. |
| `scrape_job_info(job_listing) -> dict` | Extracts job details from a job listing HTML element.                                                                                     |

---
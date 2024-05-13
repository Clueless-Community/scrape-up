def stringDecorator(func):
    """
    The stringDecorator function wraps the decorated function and performs the following modifications:
    - If the result of the decorated function is None, it returns the string "NA".
    - it removes any trailing hyphen ('-') from the text.
    - It strips any leading/trailing whitespace from the modified text.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function with the modified behavior.

    Example:
        @stringDecorator
        def getJobTitle(job):
            return job.find("h2", {"class": "jobTitle"})

        title = getJobTitle(job)
        # If the job title is "Software Engineer -", it will be returned as "Software Engineer".
        # If the job title is None, it will be returned as "NA".
        # Any leading/trailing whitespace will be removed from the job title.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result is None:
            return "NA"

        text = result.text

        if text.endswith("-"):
            text = text[:-1]

        # Strip any leading/trailing whitespace and return
        return text.strip()

    return wrapper

import multiprocessing

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Use Uvicorn workers
worker_class = 'uvicorn.workers.UvicornWorker'

# Bind to this socket
bind = "0.0.0.0:8000"

# Timeout for worker processes
timeout = 300  # Increased timeout for processing audio

# Log level
loglevel = 'info'

# Preload the application
preload_app = True

# Reload the workers when code changes (for development)
reload = True
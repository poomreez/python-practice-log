import time

def log_execution_time(func):
    def wrapper():
        print(f"--- Starting task: {func.__name__} ---")
        start = time.time()

        func()

        end = time.time()
        print(f"--- Finished task: {func.__name__} ---")
        print(f"--- Duration: {end - start:.2f} seconds ---")
    return wrapper

@log_execution_time
def process_sales_data():
    print("Processing...")
    time.sleep(3)

@log_execution_time
def clean_customer_table():
    print("Cleaning...")
    time.sleep(1)

process_sales_data()
clean_customer_table()
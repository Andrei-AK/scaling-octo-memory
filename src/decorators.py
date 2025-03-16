def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                result_massage = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "w", encoding="UTF-8") as f:
                        f.write(result_massage)
                else:
                    print(result_massage)
                return result
            except Exception as exc:
                exception_massage = f"{func.__name__} error: {exc}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w", encoding="UTF-8") as f:
                        f.write(exception_massage)
                else:
                    print(exception_massage)

        return wrapper

    return decorator


@log()
def my_function(x, y):
    return x + y


my_function("a", 2)

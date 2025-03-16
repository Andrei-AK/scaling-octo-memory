def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_massage = f"Функция {func.__name__} с аргументами {args}, {kwargs} начала работу\n"
            if filename:
                with open(filename, "w", encoding="UTF-8") as f:
                    f.write(start_massage)
            else:
                print(start_massage)
            try:
                result = func(*args, **kwargs)
                result_massage = f"Функция {func.__name__} закончила работу с резултатом {result}\n"
                if filename:
                    with open(filename, "a", encoding="UTF-8") as f:
                        f.write(result_massage)
                else:
                    print(result_massage)
                return result
            except Exception as exc:
                exception_massage = f"Функция {func.__name__} закончила работу с ошибкой {exc}\n"
                if filename:
                    with open(filename, "a", encoding="UTF-8") as f:
                        f.write(exception_massage)
                else:
                    print(exception_massage)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function("a", 2)

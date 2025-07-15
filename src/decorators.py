from datetime import datetime


def log(filename=None):
    def wrapper(function):
        def func_inner(*args, **kwargs):
            """Функция производит сложение двух числе"""
            result_func = None
            try:
                result_func = function(*args, **kwargs)
                result = f"{function.__name__} ok"
            except Exception as errors:
                result = (
                    f"{function.__name__} "
                    f"error: {type(errors).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
            if filename is None:
                print(result)
                return result_func
            str_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            with open(filename, "a", encoding="utf-8") as file_log:
                file_log.write(str_date + " " + result + "\n")
                return result_func

        return func_inner

    return wrapper


@log("mylog.txt")
@log()
def sum_numbers(x, y):
    return x + y

def write_file(sample_func):
    def execute():
        result_2 = sample_func()
        with open(result_2, "w+") as my_file:
            print(my_file.write("today is a very good day"))

    return execute


def create_file(sample_fuc):
    def execute():
        result = sample_fuc()
        with open(result, "r") as my_file:
            print(my_file.read())
        return result

    return execute


@write_file
@create_file
def filesTest():
    return "Today is a good day.txt"


filesTest()

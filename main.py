def write_file(sample_func):
    def execute():
        result_2 = sample_func()
        with open(result_2,"w+") as my_file:
            print(my_file.write(result_2))
    return execute

def create_file(sample_fuc):
    def execute():
        result = sample_fuc()
        with open(result, "w") as my_file:
            print(my_file.write("file_created"))
        return result
    return execute
@write_file
@create_file
def filesTest():
    return "Today is a good day.txt"

filesTest()

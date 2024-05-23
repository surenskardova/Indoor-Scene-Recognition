import string

import inspect





def is_legal_answer(q: str, n_options: int = 4):

    assert isinstance(q, str), f"The answer should be a string, was {type(q)}."

    q = q.replace(" ", "").replace(",", "")

    for c in q:

        assert c.lower() in string.ascii_lowercase[:n_options], f"Invalid character in answer: '{c}'"





def _format_parameters(fn):

    def _format_parameter(param):

        return param.name + (f"={param.default}" if not param.default == inspect._empty else "")



    return "(" + ", ".join(_format_parameter(p) for p in inspect.signature(fn).parameters.values()) + ")"





def _check_signature(expected, provided):

    assert str(inspect.signature(provided)) == str(inspect.signature(

        expected)), f"Function signature modified! Expected {_format_parameters(expected)} but got {_format_parameters(provided)}."





def signature_unchanged(fn, *args, **kwargs):
    if fn.__name__ == "build_model_1":
        def build_model_1():
            pass
        _check_signature(build_model_1, fn)
    if fn.__name__ == "build_model_2":
        def build_model_2():
            pass
        _check_signature(build_model_2, fn)
    if fn.__name__ == "build_test_generator":
        def build_test_generator(test_data, test_data_dir):
            """ Returns a test generator for the 200 images you just collected
            Keyword arguments:
            test_data -- the DataFrame with the test data
            test_data_dir -- the directory where the test images are stored
            """
            pass
        _check_signature(build_test_generator, fn)
    if fn.__name__ == "evaluate_on_test":
        def evaluate_on_test(test_generator, model_name):
            """ Evaluates the given model on given test data and returns the accuracy
            Keyword arguments:
            test_generator -- the generator for the test data
            model_name -- the name of the model to load
            """
            pass
        _check_signature(evaluate_on_test, fn)

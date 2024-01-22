"""
settings for codegnan app.
"""

from decouple import config

# The number of code server processes to run..
N_CODE_SERVERS = config('N_CODE_SERVERS', default=5, cast=int)

# The server pool port.  This is the server which returns available server
# ports so as to minimize load.  This is some random number where no other
# service is running.  It should be > 1024 and less < 65535 though.
SERVER_POOL_PORT = config('SERVER_POOL_PORT', default=55555, cast=int)

# Server host name
SERVER_HOST_NAME = config('SERVER_HOST_NAME', default='http://localhost')

# Timeout for the code to run in seconds.  This is an integer!
SERVER_TIMEOUT = config('SERVER_TIMEOUT', default=4, cast=int)

# The root of the URL, for example you might be in the situation where you
# are not hosted as host.org/exam/  but as host.org/foo/exam/ for whatever
# reason set this to the root you have to serve at.  In the above example
# host.org/foo/exam set URL_ROOT='/foo'
URL_ROOT = ''

code_evaluators = {
    "python": {
      "standardtestcase":
      "codegnan.python_assertion_evaluator.PythonAssertionEvaluator",
      "stdiobasedtestcase":
      "codegnan.python_stdio_evaluator.PythonStdIOEvaluator",
      "hooktestcase": "codegnan.hook_evaluator.HookEvaluator"
      },
    "c": {"standardtestcase": "codegnan.cpp_code_evaluator.CppCodeEvaluator",
          "stdiobasedtestcase": "codegnan.cpp_stdio_evaluator.CppStdIOEvaluator",
          "hooktestcase": "codegnan.hook_evaluator.HookEvaluator"
          },
    "cpp": {"standardtestcase": "codegnan.cpp_code_evaluator.CppCodeEvaluator",
            "stdiobasedtestcase":
            "codegnan.cpp_stdio_evaluator.CppStdIOEvaluator",
            "hooktestcase": "codegnan.hook_evaluator.HookEvaluator"
            },
    "java": {"standardtestcase": "codegnan.java_code_evaluator.JavaCodeEvaluator",
             "stdiobasedtestcase":
             "codegnan.java_stdio_evaluator.JavaStdIOEvaluator",
             "hooktestcase": "codegnan.hook_evaluator.HookEvaluator"
             },
    "bash": {"standardtestcase": "codegnan.bash_code_evaluator.BashCodeEvaluator",
             "stdiobasedtestcase":
             "codegnan.bash_stdio_evaluator.BashStdIOEvaluator",
             "hooktestcase": "codegnan.hook_evaluator.HookEvaluator"
             },
    "scilab": {
        "standardtestcase": "codegnan.scilab_code_evaluator.ScilabCodeEvaluator",
        "hooktestcase": "codegnan.hook_evaluator.HookEvaluator"
        },
    "r": {
        "standardtestcase": "codegnan.r_code_evaluator.RCodeEvaluator",
        "hooktestcase": "codegnan.hook_evaluator.HookEvaluator"
        },
}

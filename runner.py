# Author : Selva

"""
Test automation begins with this runner file.
End user can specify desired scenario tags and
run the test. Test output is generated in Allure
Format so that the result can be visualised using
Allure Report
"""

from behave import __main__ as runner
if __name__ == "__main__":
    runner.main('./features/ -f allure_behave.formatter:AllureFormatter '
                '-o allure-results --no-capture --no-capture-stderr'
                ' --no-skipped -f plain --tags=@MockTest')

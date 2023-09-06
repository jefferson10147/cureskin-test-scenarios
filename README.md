# Test cases: CureSkin page

<table>
    <tr>
        <td>
            In this project, you may find the test cases for the CureSkin main page and the shop page.
            With the following stack of technologies like Python 3, Selenium, and Behave.
        </td>
    </tr>
</table>

## How to execute this project (UNIX Systems)

1- Clone this project, on your local machine:

```bash
$ git clone https://github.com/jefferson10147/cureskin-test-scenarios.git
```

2- Create a Python virtual environment:

```bash
$ python3 -m venv ./venv
```

3- Activate env:

```bash
$ source your_venv/bin/activate
```

4- Install dependencies:

```bash
$ pip install -r requirements.txt
```

## Examples of execution:

- To run all the test cases from a specific feature file:
```bash
$ behave features/tests/shop_page_test.feature
```

- To run a specific test case from a specific feature file:
```bash
$ behave features/tests/shop_page_test.feature -n 'User can click through the product collections'
```

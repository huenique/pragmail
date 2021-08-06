# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

# Types of Contributions

## Report Bugs

Report bugs at https://github.com/huenique/pragmail/issues.

If you are reporting a bug, please include:

* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

## Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

## Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

## Write Documentation

pragmail could always use more documentation, whether as part of the official pragmail docs, in docstrings, or even on the web in blog posts, articles, and such.

## Submit Feedback

The best way to send feedback is to file an issue at https://github.com/huenique/pragmail/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome

## Get Started

Ready to contribute? Here's how to set up `pragmail` for local development.

1. Fork the `pragmail` repo on GitHub.
2. Clone your fork locally

    ```
    $ git clone git@github.com:huenique/pragmail.git
    ```

3. Install your local copy into a virtualenv. Assuming you have python venv installed, this is how you set up your fork for local development

    ```
    $ cd pragmail/
    $ python3.9 -m venv pragmail-venv
    $ source pragmail-venv/bin/activate
    $ poetry install  # Make sure poetry is installed
    ```

4. Create a branch for local development

    ```
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests

    ```
    $ flake8 pragmail tests
    $ pytest -v
    ```

## Commit Message Guidelines
pragmail uses precise rules over how git commit messages can be formatted. This leads to more readable messages that are easy to follow when looking through the project history. But also, git commit messages are used to generate the change log. For instructions, go to this site: https://www.conventionalcommits.org/en/v1.0.0/.

```
$ git add .
$ git commit -m "<type>(<scope>): <subject>"
$ git push origin name-of-your-bugfix-or-feature
```

## Pull Request Guidelines

Please open an issue before submitting, unless it's just a typo or some other small error.

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.9 and above.

Before making changes to the code, install the development requirements using

```
$ poetry install
```

Before committing, stage your files and run style and linter checks

```
$ git add .
$ pre-commit run
```

pre-commit will unstage any files that do not pass. Fix the issues until all checks pass and commit.

## Tips

To run a subset of tests

```
$ pytest -v tests/test_clients.py
```

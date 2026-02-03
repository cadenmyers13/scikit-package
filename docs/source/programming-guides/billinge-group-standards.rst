
:tocdepth: -1

.. index:: billinge-group-standards

.. _billinge-group-standards:

========================
Billinge Group standards
========================

We present here standards of coding and coding workflows that have been adopted in the Billinge research group over multiple years to make our code more uniform and maintainable by a diverse and shifting team of students and post-docs. They are mostly adopting what we have learned to be standards in the Python community, with some lessons learned along the way. This is not the only way to do things, but since it has taken us lots of trial and error to develop them over time, we share them here in case they are useful to you.

.. _github-commit-issue-practice:

GitHub workflow
---------------

Commit messages and issue titles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For commit messages and issue titles, we add prefixes adopted from https://www.conventionalcommits.org:

.. code-block:: text

    feat: A new feature has been added.
    fix: A bug has been fixed.
    docs: Documentation changes only.
    style: Changes that don't affect code functionality (e.g., formatting, whitespace).
    refactor: Code changes that neither fix a bug nor add a feature.
    perf: Performance improvements.
    test: Adding missing tests or correcting existing ones.
    chore: Updates to the build process or auxiliary tools.
    build: Changes that affect the build artifact or external dependencies.
    ci: Updates to CI configuration files and scripts.
    revert: Reverts a previous commit.
    release: A new package version is being prepared.
    skpkg: Using scikit-package to create a new package or maintain an existing package.

- Example 1: "feat: create a ``DiffractionObject.morph_to()`` method"
- Example 2: "bug: handle divide by zero error in ``DiffractionObject.scale_to``"

Please see an example here: https://github.com/scikit-package/scikit-package/issues. There are a few benefits to adding prefixes to GitHub issue titles. First, it helps us prioritize tasks from the GitHub notifications. Second, it helps reference issues in a comment within an issue or pull request and organize tasks.

.. attention::

    How do I write a good Git commit message?

    A commit message is written for PR reviewers and for debuggers. Avoid verbosity for a quick overview. An ideal commit message communicates file(s) of interest, the reason for the modification, and what modifications were made. e.g., “chore: move all files from docs to doc for scikit-packaging."

.. attention::

    How do I write a good GitHub issue title?

    The issue is where we discuss and determine whether to implement via a pull request. It's much easier for the project maintainer(s) to recall the problem/intended behavior and the technique in that order. Here are some examples:

        e.g., "feat: set custom default prompt values after ``package create <command>`` using hidden config file."

        e.g., "feat: preview rendered documentation in each PR with GitHub Actions"

    If you have a **suggestion**, you can also create an issue with a question mark:

        e.g., "refactor: how can we dynamically retrieve python min/max default Python versions in documentation?"

        e.g., "refactor: can we standarlize the way we write CHANGELOG (news.rst file)?"

Pull request practices
^^^^^^^^^^^^^^^^^^^^^^

#. Have a theme for each PR to reduce cognitive overload for the reviewer.

#. Make PRs small with the possibility of rejection.

#. Write ``closes #<issue-number>`` in the PR comment to automatically close the issue when the PR is merged. See https://github.com/scikit-package/scikit-package/pull/350.

#. A PR should **close an issue** on GitHub. If there is no issue, make one. If the issue is big, consider breaking it down into smaller issues.

#. **Review** your own PR. Start as a draft PR, click :guilabel:`Files changed`, add comments, and then request a review. In-line comments are needed if the changes are not obvious for the reviewer. See https://github.com/scikit-package/scikit-package/pull/310.

#. If **another commit** was pushed after *“@username ready for review”*, write another comment *“@username ready for review after fixing ____”* so that the reviewer is directed to the PR, not the file changes by the new commit.

#. Use the pull request template provided in ``.github/PULL_REQUEST_TEMPLATE``. In the PR comment, **highlight inputs and outputs** of the changes (screenshots/outputs).

#. **Address all** in-line comments made by the reviewer(s) before asking for another round of review. If you have seen a comment and agree with it but no action is needed, a thumbs-up emoji is sufficient.

#. Use ``>`` to quote the reviewer's sentence(s) and write your response below it. If there are multiple comments, tag the reviewer(s) with @username.

#. During PR review, when reviewers propose new ideas or suggestions beyond the scope of the PR, create an issue using the issue template and include a link to the specific PR comment URL (not the PR itself). Then, reply to the reviewer(s) to confirm that the issue has been created.

#. PR from a new branch if it contains a meaningless commit history.

#. Do not force push. Use ``git revert`` to unwind the previous commit.

#. If you've made a mistake but have not used ``git add``, use ``git restore <file-name>``.

#. Before CI is integrated, include local test passing results in each PR to save time for the reviewer.

#. For migrating files from one folder to another folder, use ``git mv``.

#. For deleting files generated by the OS such as ``.DS_Store`` use ``git rm`` instead of ``git add`` to also remove from the Git index (staging area).

#. When a PR is closed for any reason, add a single sentence in the comment explaining why the PR is being closed. If a new PR is created, add the new PR link in the comment.

.. _news-item-practice:

Writing news items for release notes
------------------------------------

.. include:: ../snippets/news-file-format.rst

Writing tutorials
-----------------

#. In general, we want to provide step-by-step instructions, including CLI commands and expected outputs. However, to avoid "reinventing the internet", we should provide recommended workflows and tools. For example, in ``scikit-package``, we recommend using ``Git for Windows`` for Windows users so that everyone, including macOS and Linux users, can also follow the same steps.

Unit tests
----------

Why do we write unit tests?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We write tests to document the intended behavior of the code. When refactoring tests, consider what we “want” to happen, rather writing tweaking the existing test functions to pass.

Group and organize test cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following practices have been developed to ensure consistency in writing tests:

#. Comment starts with a uppercase letter (PEP8 standard) unless it's a name starting with a lowercase letter like a function name.

#. Include a high-level test function comment e.g., ``# Test conversion of q to tth with q and wavelength``

#. Use ``C1: Start with a capital letter...`` or ``Case 1: Start...`` for each condition under ``@pytest.mark.parametrize``.

#. If applicable, group similar test conditions under a single case. Numerate each test condition.

#. Divide a test case comment into two parts: ``x, y, z (conditions), expect...``. Ensure there is a ``expect`` keyword after the test conditions provided.

#. Use descriptive yet concise variable names for expected values (e.g., ``expected_xarrays`` instead of ``expected``)

#. Order test cases from the most general to edge cases. This helps readers understand the basic function behavior first before utilizing or encountering unusual features or behaviors.

#. Consider moving reusable code objects to ``conftest.py``. See warning messages and objects defined in https://github.com/diffpy/diffpy.utils/blob/main/tests/conftest.py available in each test function in https://github.com/diffpy/diffpy.utils/blob/main/tests/test_diffraction_objects.py/

Pytest example 1

.. code-block:: python

  @pytest.mark.parametrize(
      "xtype, expected_xarray",
      [
          # Test whether on_xtype returns the correct xarray values
          # C1: tth to tth, expect no change in xarray value
          # 1. "tth" provided, expect tth
          # 2. "2theta" provided, expect tth
          ("tth", np.array([30, 60])),
          ("2theta", np.array([30, 60])),
          # C2: "q" provided, expect q converted from tth
          ("q", np.array([0.51764, 1])),
          # C3: "d" provided, expect d converted from tth
          ("d", np.array([12.13818, 6.28319])),
      ],
  )
  def test_on_xtype(xtype, expected_xarray, do_minimal_tth):
      pass

Pytest example 2 - multi-line arguments

- Add `# C1:` inside within `( ... )`. More examples `here <https://github.com/diffpy/diffpy.utils/pull/277>`_.

.. code-block:: python

  @pytest.mark.parametrize(
      "do_args_1, do_args_2, expected_equality, wavelength_warning_expected",
      [
          # Test when __eq__ returns True and False
          (  # C1: Identical args, expect equality
              {
                  "name": "same",
                  "scat_quantity": "x-ray",
                  "wavelength": 0.71,
                  "xtype": "q",
                  "xarray": np.array([1.0, 2.0]),
                  "yarray": np.array([100.0, 200.0]),
                  "metadata": {"thing1": 1},
              },
              {
                  "name": "same",
                  "scat_quantity": "x-ray",
                  "wavelength": 0.71,
                  "xtype": "q",
                  "xarray": np.array([1.0, 2.0]),
                  "yarray": np.array([100.0, 200.0]),
                  "metadata": {"thing1": 1},
              },
              True,
              False,
          ),
          (  # C2: Different names, expect inequality
              {
                  "name": "something",
                  "xtype": "tth",
                  "xarray": np.empty(0),
                  "yarray": np.empty(0),
                  "metadata": {"thing1": 1, "thing2": "thing2"},
              },
              {
                  "name": "something else",
                  "xtype": "tth",
                  "xarray": np.empty(0),
                  "yarray": np.empty(0),
                  "metadata": {"thing1": 1, "thing2": "thing2"},
              },
              False,
              True,
          ),
      ],
  )
  def test_equality(do_args_1, do_args_2, expected_equality, wavelength_warning_expected):
      pass


Comment starts with a uppercase letter (PEP8 standard) unless it's a name starting with a lowercase letter like a function name.

Docstrings
----------

Please bookmark the following:

    PEP257: https://peps.python.org/pep-0257

    PEP8: https://peps.python.org/pep-0008/

    NumPy document style guide: https://numpydoc.readthedocs.io/en/latest/format.html

In the group, we follow the NumPy standard:

#. A one-line summary that does not use variable names or the function name is added before a full description.

#. Use "Return a dict" instead of "Returns a dict". Comments are instructions.

#. "The" is used for the starting description of attribute/parameter/return.

#. Full docstrings are not required for private functions.

For examples, please refer to https://github.com/diffpy/diffpy.utils/blob/main/src/diffpy/utils/diffraction_objects.py.

.. _file-folder-naming-convention:

Naming conventions
------------------

When should we use hyphens ``-`` or underscores ``_`` in file and folder names?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use hyphens ``-`` for project names, package names, GitHub repositories, folder names, branch names, and static files like ``.rst``, ``.md``, ``.yml``, and ``.png``. For CLI, also use hyphens ``-`` for args like ``gh pr list --author "@sbillinge"`` Check an example documentation of ``scikit-package`` here: https://github.com/scikit-package/scikit-package/tree/main/docs/source.

Use underscores ``_`` in the following two cases:

#. Python files, e.g., ``tests/test_diffraction_objects.py``.

#. Project directory names, e.g., ``src/<project_directory_name>``. Modules and packages are imported with spaces replaced by underscores, like ``import bg_mpl_stylesheets``. Here is an example project: https://github.com/scikit-package/bg-mpl-stylesheets/tree/main/src/bg_mpl_stylesheets.

.. note::

  ``scikit-package`` automatically creates a folder with underscores ``_`` for the project directory name and ``.py`` files. We recommend using a single word for folder names that contain Python scripts, e.g., ``src/example_package/parsers``, so that it can be imported as ``from example_package.parsers import <module>``. This follows Python conventions.

.. warning::

    There are still cases where we do not strictly follow the above conventions, typically for configuration files. In such cases, we adhere to the naming conventions of the respective tool. For example, ``.codespell/ignore_lines.txt`` is a configuration file for the ``codespell`` tool. ``.github/ISSUE_TEMPLATE`` is the designated folder for storing GitHub issue templates. If you are unsure, please feel free to open an issue in the ``scikit-package`` GitHub repository.

Error message
-------------

Divide an error message into two sections: (1) reason for error, (2) what to do to fix it. Ex) "Both release and pre-release specified. Please re-run the command specifying either release or pre_release.” Error messages are for users. Consider users without programming knowledge.

Deprecating functions
---------------------

Over time, code bases and standards change and a method or function
may have a name or location change. In this case, we want to warn
users that the function or method is being changed and that it will break
their code in the future. The process of warning users is called **deprecating**.

Below is a step-by-step guide for deprecating an old method or class
using the ``@deprecated`` decorator.

Locate the method or function to be deprecated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, you will have to a locate method or function that needs to be
deprecated. For this example, we will be deprecating the ``loadData()``
method from ``diffpy.utils.parsers.loaddata``. This will be changed to
``load_data()`` from ``diffpy.utils.tools``.

Get necessary imports from ``diffpy.utils``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python now includes a built-in decorator for Python versions ``>=3.13``. For
packages that have support for Python ``<=3.13``, we have to use our own
deprecator. The syntax is the same for both our deprecator and the
built-in Python one. To get ours and a useful helper function, run

::

   from diffpy.utils._deprecator import deprecated, deprecation_message

The function ``deprecation_message`` is used to make the deprecation
methods consistent. We want the message to let the user know what is
going to be broken in the future, what version it will be broken in, and
what its new name will be.

Because these changes are API-breaking (i.e. it will break users' scripts),
The removal will be made on a version bump of the first number
(ie. going from version ``3.2.0`` to version ``4.0.0`` or something like that).

This function has the inputs
``base, old_name, new_name, removal_version, new_base=None`` and will
print

::

       f"'{base}.{old_name}' is deprecated and will be "
       "removed in version {removal_version}. Please use"
       "{new_base}.{new_name} instead."

Use the default ``new_base=None`` if the function location is not changing.
Otherwise, define your new location through the base name.

Define your deprecation message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Somewhere near the top of the module, define the deprecation message.
for the ``loadData`` example, this looks like,

::

   base = "diffpy.utils.parsers.loaddata"
   removal_version = "4.0.0"
   loaddata_deprecation_msg = deprecation_message(
       base,
       "loadData",
       "load_data",
       removal_version,
       new_base="diffpy.utils.tools",
   )

Mark as deprecated with ``@deprecated``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the proceeding step, you will begin to change the actual source code
so pay attention.

Directly above the function you are deprecating, add the ``@deprecated``
decorator with the deprecation message inside,

::

   # In loaddata.py

   @deprecated(loaddata_deprecation_msg)
   def loadData(inputs)
      """This is my docstring"""
      outputs = code_doing_something(inputs)
      return outputs

Copy old function to its new location and change the name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Skip to the next step if your function stays in the same file.

Copy and paste your old function to its new location with its new name,

::

   # In tools.py (new location)

   def load_data(inputs)
      """This is my docstring"""
      outputs = code_doing_something(inputs)
      return outputs

::

   # In loaddata.py (old location)

   @deprecated(loaddata_deprecation_msg)
   def loadData(inputs)
      """This is my docstring"""
      outputs = code_doing_something(inputs)
      return outputs

At this point you will have two duplicate functions with different
names.

Copy old function in the same file and change the name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your function is moved to a different file, skip this step but make
sure you do the previous step.

If the function stays in the same file, simply copy and paste the
function directly above and change its name to the new name. You will
now have two functions with different names. If ``loadData()`` stayed in
the same spot, this would look something like,

::

   # In loaddata.py

   def load_data(inputs)
      """This is my docstring"""
      outputs = code_doing_something(inputs)
      return outputs

   @deprecated(loaddata_deprecation_msg)
   def loadData(inputs)
      """This is my docstring"""
      outputs = code_doing_something(inputs)
      return outputs

Point the old function to use the new function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, remove the contents of the old function and have it point to the
new function. If the new function has changed locations, you will have
to import the new function from its new location,

::

   from diffpy.utils.tools import load_data # omit this if your function location hasn't changed

   @deprecated(loaddata_deprecation_msg)
   def loadData(inputs)
      """This is my docstring"""
      outputs = load_data(inputs)
      return outputs

Update the docstring in the old function to warn users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, add a helpful message informing users that the old function is
deprecated and will be removed in the future,

::

   from diffpy.utils.tools import load_data # omit this if your function location hasn't changed

   @deprecated(loaddata_deprecation_msg)
   def loadData(inputs)
      """This function has been deprecated and will be removed in version
      4.0.0.

      Please use diffpy.utils.parsers.load_data instead.
      """
      outputs = load_data(inputs)
      return outputs

Global search the old function name to make sure its been updated everywhere
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do a global search and replace the name of the old function everywhere
you see it, except in the api docs (and where you have marked it as ``@deprecated``).
We will automatically build api docs later.

Test that the deprecation message prints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a fresh environment, locally install your package by running
``pip install .``. Then, create a new scrap file or notebook and try to
run some code using the old function name.

If you are unsure how to run some of the functions, please see the
`example scripts here <https://github.com/diffpy/diffpy.cmi/tree/main/docs/examples>`_.
It is likely that your function is being used in at least one of these scripts.

If everything works accordingly, a
deprecation message will be printed. For example,

::

   from diffpy.utils.parsers.loaddata import loadData

   file_path = "path/to/my/data.gr"
   my_data = loadData(file_path)

The function will still work, but you will now get the following warning
message,

::

       'diffpy.utils.parsers.loaddata.loadData' is deprecated
       and will be removed in version 4.0.0. Please use
       'diffpy.utils.tools.load_data' instead.

Open a Pull Request
^^^^^^^^^^^^^^^^^^^

Once completed and tested, create a PR into the branch of the removal
version (ie, not ``main`` but something like ``v4.0.0``). If that branch
does not exist, reach out to Simon to have the branch made.


Other considerations for maintaining group infrastructure
---------------------------------------------------------

#. Be extremely careful with changes that are visible to users.

#. Try not to pass down technical debt to future members. Do the extra work so that others can save time. Ex) making a PR to the ``scikit-package`` repo once an issue has been identified in a project standardlized with ``scikit-package``.

#. Design code to save developer time in the long run rather than focusing solely on reducing compute time, especially when computing resources are not the primary constraint.

#. It is easier to remove things (e.g., dependencies) we don't want than to add things that are needed in certain circumstances.

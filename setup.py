from distutils.core import setup
setup(name='uc',
      version='1.0',
      py_modules=['uc'],
      author='Anna Pynda',
      author_email='pynda@ucu.edu.ua',
      url="https://github.com/annapynda/Cursova/wiki/",
      download_url="https://github.com/annapynda/CalorieTrack_code",
      classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Development Status :: 4 - Beta",
            "Environment :: Other Environment",
            "Intended Audience :: Users",
            "Operating System :: OS Independent",
            "Topic :: Calories Tracking"],
            long_description = """\
            The program is used to detect the users norma of calories and water,
            to add product to the track and counts how many protein, fat, carbohydrates,
            calories are in N grams.
      This version requires Python 3 or later;
      """
      )
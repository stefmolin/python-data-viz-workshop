# Beyond the Basics: Data Visualization in Python

[![Nbviewer](https://img.shields.io/badge/render-nbviewer-lightgrey?logo=jupyter)](https://nbviewer.jupyter.org/github/stefmolin/python-data-viz-workshop/tree/main/) [![Env Build Workflow Status](https://img.shields.io/github/actions/workflow/status/stefmolin/python-data-viz-workshop/env-checks.yml?label=env%20build&logo=github&logoColor=white)](https://github.com/stefmolin/python-data-viz-workshop/actions/workflows/env-checks.yml) ![GitHub repo size](https://img.shields.io/github/repo-size/stefmolin/python-data-viz-workshop?logo=git&logoColor=white) [![View slides in browser](https://img.shields.io/badge/view-slides-orange?logo=reveal.js&logoColor=white)](https://stefmolin.github.io/python-data-viz-workshop/slides/html/workshop.slides.html#/)

The human brain excels at finding patterns in visual representations, which is why data visualizations are essential to any analysis. Done right, they bridge the gap between those analyzing the data and those consuming the analysis. However, learning to create impactful, aesthetically-pleasing visualizations can often be challenging. This session will equip you with the skills to make customized visualizations for your data using Python.

While there are many plotting libraries to choose from, the prolific Matplotlib library is always a great place to start. Since various Python data science libraries utilize Matplotlib under the hood, familiarity with Matplotlib itself gives you the flexibility to fine tune the resulting visualizations (e.g., add annotations, animate, etc.). This session will also introduce interactive visualizations using HoloViz, which provides a higher-level plotting API capable of using Matplotlib and Bokeh (a Python library for generating interactive, JavaScript-powered visualizations) under the hood.

## Workshop Outline

This is a workshop on data visualization in Python first delivered at [ODSC West 2021](https://odsc.com/speakers/introduction-to-data-visualization-in-python/) and subsequently at [ODSC East 2022](https://odsc.com/speakers/introduction-to-data-visualization-in-python/), [PyCon Italia 2022](https://pycon.it/en/talk/beyond-the-basics-data-visualization-in-python?day=2022-06-03), [ODSC Europe 2022](https://odsc.com/speakers/introduction-to-data-visualization-in-python/), [EuroPython 2022](https://ep2022.europython.eu/session/beyond-the-basics-data-visualization-in-python), [ODSC West 2022](https://odsc.com/speakers/introduction-to-data-visualization-in-python/), the Toronto Machine Learning Summit (TMLS) 2022, [PyCon US 2023](https://us.pycon.org/2023/schedule/presentation/17/), [ODSC East 2023](https://odsc.com/speakers/introduction-to-data-visualization-in-python/), and [PyCon Italia 2023](https://pycon.it/en/event/beyond-the-basics-data-visualization-in-python-2). It's divided into the following sections:

### Section 1: Getting Started With Matplotlib
We will begin by familiarizing ourselves with Matplotlib. Moving beyond the default options, we will explore how to customize various aspects of our visualizations. By the end of this section, you will be able to generate plots using the Matplotlib API directly, as well as customize the plots that libraries like pandas and Seaborn create for you.

### Section 2: Moving Beyond Static Visualizations
Static visualizations are limited in how much information they can show. To move beyond these limitations, we can create animated and/or interactive visualizations. Animations make it possible for our visualizations to tell a story through movement of the plot components (e.g., bars, points, lines). Interactivity makes it possible to explore the data visually by hiding and displaying information based on user interest. In this section, we will focus on creating animated visualizations using Matplotlib before moving on to create interactive visualizations in the next section.

### Section 3: Building Interactive Visualizations for Data Exploration
When exploring our data, interactive visualizations can provide the most value. Without having to create multiple iterations of the same plot, we can use mouse actions (e.g., click, hover, zoom, etc.) to explore different aspects and subsets of the data. In this section, we will learn how to use a few of the libraries in the HoloViz ecosystem to create interactive visualizations for exploring our data utilizing the Bokeh backend.


---

## Prerequisites
You should have basic knowledge of Python and be comfortable working in Jupyter Notebooks. Check out [this notebook](https://github.com/stefmolin/Hands-On-Data-Analysis-with-Pandas-2nd-edition/blob/master/ch_01/python_101.ipynb) for a crash course in Python or work through the [official Python tutorial](https://docs.python.org/3/tutorial/) for a more formal introduction. The environment we will use for this workshop comes with JupyterLab, which is pretty intuitive, but be sure to familiarize yourself [using notebooks in JupyterLab](https://jupyterlab.readthedocs.io/en/latest/user/notebook.html) and [additional functionality in JupyterLab](https://dzone.com/articles/getting-started-with-jupyterlab). In addition, a basic understanding of pandas will be beneficial, but is not required; reviewing the first section of my [pandas workshop](https://github.com/stefmolin/pandas-workshop) will be sufficient.

---

## Setup Instructions

You can work through the notebooks locally or in your browser. Pick the installation option that makes sense for you.

### Local Installation
**Warning**: It is highly recommended that you use your personal laptop for the installation.

0. Install [Anaconda](https://docs.anaconda.com/anaconda/install/)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Mambaforge](https://mamba.readthedocs.io/en/latest/installation.html#fresh-install), if not already installed.
1. Fork this repository:

    ![location of fork button in GitHub](./media/fork_button.png)

2. Navigate to your fork, and click the **Code** button:

    ![location of code button in GitHub](./media/code_button.png)

3. Clone your forked repository using the desired method from the **Local** tab:

    <img width="400px" src="./media/clone_options.png" alt="local cloning options">

4. Create and activate a conda virtual environment (on Windows, these commands should be run in **Anaconda Prompt**):

    ```shell
    $ cd python-data-viz-workshop
    ~/python-data-viz-workshop$ conda env create --file environment.yml
    ~/python-data-viz-workshop$ conda activate data_viz_workshop
    (data_viz_workshop) ~/python-data-viz-workshop$
    ```

    *Note: If you installed Mambaforge or have already installed `mamba` in your base environment, you can change `conda env create` to `mamba env create`.*

5. Launch JupyterLab:

    ```shell
    (data_viz_workshop) ~/python-data-viz-workshop$ jupyter lab
    ```

6. Navigate to the `0-check_your_env.ipynb` notebook in the `notebooks/` folder:

    ![open 0-check_your_env.ipynb](./media/open_env_check_notebook.png)

7. Run the notebook to confirm everything is set up properly:

    ![check env](./media/env_check.png)

### Cloud Options

#### GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/stefmolin/python-data-viz-workshop)

The [GitHub Codespaces](https://github.com/features/codespaces) setup provides a pre-configured machine with Jupyter Notebooks running in [Visual Studio Code](https://code.visualstudio.com/) in your browser. You will need a GitHub account and available quota (all users get more than enough free monthly quota to be able to run this workshop). Note that this will take a while to build. It's recommended that you click the badge above to build the codespace in advance of the workshop and then [stop the codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/stopping-and-starting-a-codespace) until the workshop, at which point you can simply resume and pick up where you left off.

Note that if you want to save your changes, you will need to fork the repository before creating the codespace. You will then be able to commit your changes directly from the codespace. Be sure to create your codespace in advance of the session and resume when we start.

1. Fork this repository:

    ![location of fork button in GitHub](./media/fork_button.png)

2. Navigate to your fork, and click the **Code** button:

    ![location of code button in GitHub](./media/code_button.png)

3. Launch the codespace from your fork by clicking on the **+** or **Create codespace on main** button in the **Codespaces** tab:

    <img width="400px" src="./media/create_codespace.png" alt="location of create codespace button">

4. Stop the codespace until the session starts (click the name to resume).

    <img width="400px" src="./media/edit-codespace.png" alt="ways to modify an existing codespace">

#### Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/stefmolin/python-data-viz-workshop/main?urlpath=lab/tree/notebooks)

Depending on server availability, you can use [this](https://mybinder.org/v2/gh/stefmolin/python-data-viz-workshop/main?urlpath=lab) Binder environment, which does not require the creation of a GitHub account. **There is no guarantee that you will be able to access this during the workshop.**

---

## About the Author
Stefanie Molin ([@stefmolin](https://github.com/stefmolin)) is a software engineer and data scientist at Bloomberg in New York City, where she tackles tough problems in information security, particularly those revolving around data wrangling/visualization, building tools for gathering data, and knowledge sharing. She is also the author of [Hands-On Data Analysis with Pandas](https://www.amazon.com/dp/1800563450/), which is currently in its second edition and has been translated into Korean. She holds a bachelor’s of science degree in operations research from Columbia University's Fu Foundation School of Engineering and Applied Science, as well as a master’s degree in computer science, with a specialization in machine learning, from Georgia Tech. In her free time, she enjoys traveling the world, inventing new recipes, and learning new languages spoken among both people and computers.


## Related Content
All examples herein were developed exclusively for this workshop. [Hands-On Data Analysis with Pandas](https://www.amazon.com/dp/1800563450/) contains additional examples and exercises, as does [this](https://medium.com/@stefaniemolin/how-to-pivot-and-plot-data-with-pandas-9450939fcf8) blog post and [this](https://github.com/stefmolin/pandas-workshop) workshop on pandas.

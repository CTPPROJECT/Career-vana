<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> About The Project</a></li>
    <li><a href="#overview"> Overview</a></li>
    <li><a href="#getting-started"> Getting Started</a></li>
    <li><a href="#setup"> What We Used</a></li>
  </ol>
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify"> 
  It can be challenging to understand how your tech skills might translate into different roles within the tech sector. Our app aims to help you gain insights on where the best jobs for your skill sets are, and what kind of roles you can expect to be competitive for. Furthermore, with the job recommendations we provide, and a .pdf of your resume, we can take the burden of writing individual cover letters for each posting off your plate by generating a tailored cover letter for each posting you choose.
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- OVERVIEW -->
<h2 id="overview"> :cloud: Overview</h2>

<p align="justify"> 
  In order to use our app, one simply enters the tech skills they feel proficient with, or are simply interested in, into the <code>Enter Your Tech Skills</code> text box on the <code>Sector Selector</code> tab. This will output valuable information regarding the skill sets given, as well as some job postings for those skill sets
</p>

<p align="justify"> 
  Next, simply take one of the provided postings and input it into the <code>Job Description</code> text box on the <code>Generate Cover Letter</code> tab along with a .pdf of their resume into the <code>Provide a .PDF of Your Resume</code> box.
</p>

<p align="justify"> 
  Enjoy your custom Cover Letter, and feel free to use this for any outside job postings you may be interested in!
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- GETTING STARTED -->
<h2 id="getting-started"> :book: Getting Started</h2>

<p>Create an Environment:</p>
<pre><code>$ python3 -m venv myenv</code></pre>

<p>Activate the Environment:</p>
<pre><code>$ source myenv/bin/activate</code></pre>

<p>Deactivate Environments:</p>
<pre><code>$ deactivate</code></pre>

<p>Install All Dependencies:</p>
<pre><code>$ pip install -r requirements.txt</code></pre>

<p>Run the App:</p>
<pre><code>$ streamlit run main.py</code></pre>

<p>Add Packages to Requirements.txt File:</p>
<pre><code>$ pip freeze > requirements.txt</code></pre>

<i>Note that all of the commands that appear in this project also appear in <code>commands.txt</code>, for easy copying and pasting.</i>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- SETUP -->
<h2 id="setup"> :floppy_disk: What We Used</h2>

<ul>
  <li><b>[Hugging Face](https://huggingface.co/)</b> - Where all of the search algorithms reside.</li>
  <li><b>Streamlit</b> - Where all of the search-based agents reside.</li>
  <li><b>Jupyter Notebook</b> - The main file that runs Pacman games. This file also describes a Pacman GameState types.</li>
</ul>

<h3>Some of our most valuable references</h3>
<ul>
  <li><b>graphicsDisplay.py</b> - Graphics for Pacman.</li>
</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
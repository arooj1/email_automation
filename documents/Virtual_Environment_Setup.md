
# Setting Up Virtual Environment for Email and WhatsApp Automation Project

## 1. Install Conda
If Conda is not already installed, download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).

---

## 2. Create a New Conda Environment
Run the following command in your terminal to create a new Conda environment:

```bash
conda create --name email_automation_env python=3.9
```

- `email_automation_env`: Name of the environment (you can choose any name).
- `python=3.9`: Specifies the Python version (compatible with Streamlit and other dependencies).

---

## 3. Activate the Environment
Activate the newly created environment:

```bash
conda activate email_automation_env
```

---

## 4. Install Required Packages
Install the required libraries for the project inside the environment:

```bash
conda install pandas -y
conda install -c conda-forge streamlit
conda install -c conda-forge gspread
conda install -c conda-forge oauth2client
conda install -c conda-forge pywhatkit
conda install -c conda-forge smtplib
```

---

## 5. Verify the Environment
To check if all dependencies are installed correctly, run:

```bash
conda list
```

---

## 6. Run the Streamlit App
Navigate to the folder where your `streamlit_app.py` file is located and run:

```bash
streamlit run streamlit_app.py
```

---

## 7. Deactivate the Environment (Optional)
When you're done, deactivate the environment:

```bash
conda deactivate
```

---

## Notes
- Use `conda install` for most packages to ensure compatibility within the Conda environment.
- If you need to export this environment for sharing or later use, run:

```bash
conda env export > environment.yml
```

This will create a file `environment.yml` that can be used to recreate the environment on another machine using:

```bash
conda env create -f environment.yml
```

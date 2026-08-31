# Building the Environment

Ensure Python is installed.

Install latest stable python (should include pip).

Create a folder in Environments, then specify "ProjectName"-Python, like Zabbix-Python
#
In PowerShell, create a virtual environment and activate

    python -m venv "venv"
    ./venv/scripts/activate
#
Confirm pip is installed already, then upgrade and install zabbix_utils

    pip
    py -m pip install --upgrade pip

*Ensure you're in the venv before you pull pip libraries in. Otherwise it'll do you no good to pull into the path.*

    pip install netmiko
Also create an environment requirements file

    pip freeze > requirements.txt
#
Then if someone wants to adopt those requirements to work in the same environment they'd run the commands below

    python -m venv "venv"
    ./venv/scripts/activate
    python -m pip install -r requirements.txt

Then make sure to do any updates it asks for until you can run through all three commands above without error.  

**Never touch venv manually except to delete.**

If you pulled the env to a new machine then re-run the activate command below, but we gitignore so you shouldn't have to.

    ./venv/scripts/activate
#
Also something I noticed on a new Windows machine was I had to disable advanced app aliasing that links apps to microsoft store and then needed to boot the python app manually and restart my vscode window. Weird.


# Import the Repo
If you haven't yet pull this repo into a folder in the same directory as you venv. 
**Not into the venv directory**. If you have already pulled simply move the folder there in your file manager.
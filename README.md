# Google Sheets Writer

A Python project to write data to a Google Sheet using Google Cloud user credentials.

**Note:** This project is intended for development purposes on local machines only. It is not meant to be used in production environments.

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone git@github.com:sajjadsalehicb/google-sheets-writer.git
    cd sheet_writer
    ```

2. **Create a virtual environment and install dependencies:**

    ```sh
    ./setup.sh
    ```

3. **Set up your Google Cloud credentials:**

    - Ensure you have authenticated with the necessary scopes:
    
        ```sh
        gcloud auth application-default login --scopes=https://www.googleapis.com/auth/spreadsheets,https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/cloud-platform
        ```

    - Set your quota project:
    
        ```sh
        gcloud auth application-default set-quota-project YOUR_PROJECT_ID
        ```

4. **Configure environment variables:**

    - Create a `.env` file in the root directory and add the following lines:

        ```
        GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/application_default_credentials.json
        SHEET_ID=your_google_sheet_id
        ```
      The default locations for `application_default_credentials.json` are:
      - **macOS/Linux:** `~/.config/gcloud/application_default_credentials.json`
      - **Windows:** `C:\Users\<Your Username>\AppData\Roaming\gcloud\application_default_credentials.json`

      Replace `/path/to/your/application_default_credentials.json` with the actual path if it differs from the default location.


5. **Run the script:**

    ```sh
    source venv/bin/activate
    python script.py
    ```

## Files

- `script.py`: The main script to write data to the Google Sheet.
- `.env`: Environment variables file (add your own).
- `requirements.txt`: Python dependencies.
- `setup.sh`: Script to set up the project environment.
- `README.md`: Project documentation.

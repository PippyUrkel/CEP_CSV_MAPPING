 # GeoCam Image Processor

 This project allows users to process images containing latitude and longitude data captured by a GeoCam. The extracted GPS coordinates are reverse-geocoded into human-readable addresses, and the results are saved in a CSV file. This CSV file can be directly imported into Google My Maps, automating the process of mapping locations.

 ## Features
 - Extracts latitude and longitude data from images using pytesseract.
 - Reverse-geocodes GPS coordinates to obtain addresses.
 - Generates a CSV file formatted for easy import into Google My Maps.

 ## How to Use

 ### 1. Prerequisites
 - Ensure you have Python installed (>=3.7 recommended).
 ### 2. Setup the Virtual Environment
 1. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
 2. Activate the virtual environment:
    - **Linux/Mac**:
      ```bash
      source .venv/bin/activate
      ```
    - **Windows**:
      ```cmd
      .venv\Scripts\activate
      ```

 3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

 ### 3. Organize Your Images
 - Place your GeoCam images into a folder (e.g., `DADAR`).
 - Update **lines 74 and 75** in `main.py` to match the folder name and desired output CSV file:
   ```python
   image_folder = 'YOUR_FOLDER_NAME'  # Replace with your folder name
   output_csv = 'YOUR_OUTPUT_CSV_NAME.csv'  # Replace with your output CSV file name
   ```

 ### 4. Run the Script
 Execute the script to process the images:
 ```bash
 python main.py
 ```

 ### 5. Import to Google My Maps
 - Open [Google My Maps](https://www.google.com/mymaps).
 - Create a new map or edit an existing one.
 - Import the generated CSV file.
 - Enjoy your automated map with all the locations plotted!

 ## Licensing
 This project is open-source and provided with no license. Feel free to use and modify it as you wish.

 ---

 Happy mapping! 😊

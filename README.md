#  Voice Assistant using Python  

A **simple AI-powered Voice Assistant** that listens to voice commands, processes them, and performs various tasks like opening applications, searching Wikipedia, and telling the time.  

##  Features  
 **Speech Recognition** – Listens to your voice commands  
 **Text-to-Speech (TTS)** – Responds using speech  
 **Wikipedia Search** – Fetches information from Wikipedia  
 **Open Applications** – Opens Notepad, Calculator, or a web browser  
 **Get Current Time** – Tells the current system time  
 **Exit Command** – Stops the assistant  

##  Project Structure  
```bash
Voice_Assistant/
│── main.py # Main execution script 
│── requirements.txt # List of dependencies 
│── modules/ # Core functionality │ 
  │── speech.py # Handles speech recognition & TTS │ 
  │── commands.py # Processes commands 
│── README.md # Project documentation
```

##  Installation & Setup  
### **1 Clone the Repository**  
```bash
git clone https://github.com/Deeksha-Srinivas/Voice-Assistant.git
cd Voice-Assistant
```
### **2️ Install Dependencies**
Make sure you have Python 3.7+ installed. Then run:
```bash
pip install -r requirements.txt
```
If you get pyaudio errors, install it manually:
```bash
pip install pipwin
pipwin install pyaudio
```
### **3 Run the Voice Assistant**
```bash
python main.py
```
## Usage
Once the assistant starts, you can use the following voice commands:
- **Wikipedia Python** → Fetches a summary from Wikipedia
- **What time is it?** → Tells the current time
- **Open Notepad** → Opens Notepad
- **Open browser** → Opens Google Chrome
- **Exit** → Stops the assistant


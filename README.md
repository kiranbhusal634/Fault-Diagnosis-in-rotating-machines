# **⚙️ Motor Fault Diagnosis System: Load Imbalance Detection**

## **Project Overview**

This project focuses on developing a low-cost, real-time prototype system for fault diagnosis in electric motors by analyzing their vibration patterns. Specifically, it targets the detection of **load imbalance faults**, a common yet often overlooked issue that significantly contributes to motor inefficiency, reduced lifespan, and potential damage in industrial settings.

The system leverages an **ADXL345 accelerometer sensor** to collect real-time vibration data from an electric motor. This data is then processed using a suite of statistical and signal processing techniques in Python, including Fast Fourier Transform (FFT), Root Mean Square (RMS) calculation, standard deviation, and peak analysis, culminating in a threshold-based anomaly detection mechanism.

## **🌟 Key Features**

* **Real-time Data Acquisition:** Collects vibration data from an ADXL345 accelerometer via Arduino serial communication.  
* **Comprehensive Data Analysis:** Processes raw vibration data using advanced signal processing techniques to extract meaningful insights.  
* **Statistical Metrics:** Calculates RMS, standard deviation, mean, and peak values for quantitative assessment of vibration.  
* **Frequency Domain Analysis (FFT):** Identifies dominant frequencies in the vibration signature, crucial for pinpointing specific fault types.  
* **Threshold-based Anomaly Detection:** Flags potential load imbalance faults when vibration levels exceed predefined thresholds.  
* **Modular Design:** Separate scripts for data collection and analysis, allowing for flexible workflow.  
* **Low-Cost Hardware:** Utilizes readily available and inexpensive components, making it accessible for prototyping and small-scale deployments.

## **🛠️ Technology Stack**

* **Hardware:**  
  * Arduino (e.g., Uno, Nano)  
  * ADXL345 Accelerometer Sensor  
  * Electric Motor (for testing)  
* **Software:**  
  * Arduino IDE (for sensor interfacing)  
  * Python 3.7  
    * pyserial for serial communication  
    * pandas for data manipulation  
    * matplotlib for data visualization  
    * numpy for numerical operations  
    * scipy.fft for Fast Fourier Transform

## **📊 Methodology & Findings**

### **Data Collection**

Two distinct datasets were recorded:

1. **Healthy Motor Data:** Vibration data collected from a balanced, normally operating electric motor.  
2. **Faulty Motor Data:** Vibration data collected from the same motor with an artificially induced load imbalance.

The Arduino sketch (arduino\_code.ino) reads X, Y, Z axis acceleration from the ADXL345 and calculates a scalar vibration magnitude. This data is then streamed over serial to a Python script (vibrdatacollector.py).

### **Data Analysis & Fault Detection**

The collected CSV data is then analyzed using vibration\_analyzer.py. This script performs:

* **Vibration Waveform Plotting:** Visualizes vibration magnitude over time.  
* **Statistical Analysis:** Calculates Mean, Standard Deviation, Max, Min, and RMS values.  
* **Frequency Analysis (FFT):** Transforms the time-domain signal into the frequency domain to identify characteristic frequencies associated with imbalance. The sampling rate is set to 50 Hz, corresponding to the delay(20) in the Arduino sketch.  
* **Threshold-based Anomaly Detection:** Compares the vibration magnitude against a static threshold (e.g., 1.8g) to identify abnormal activity.

### **Results**

The analysis clearly demonstrated distinguishable vibration signatures between normal and faulty motors. Notably, the **RMS and peak values** showed significant differences. For instance, the motor with induced load imbalance exhibited a substantially higher number of vibration samples exceeding a threshold of 1.8g compared to the healthy motor. The FFT plots also revealed distinct frequency components indicative of imbalance.

## **🚀 Future Work**

This prototype serves as a foundational step. Future enhancements include:

* **Expanded Dataset Collection:** Gathering 100+ labeled datasets from various motor types and fault conditions to improve robustness.  
* **Machine Learning Integration:** Training a supervised machine learning model (e.g., SVM, Random Forest, Neural Networks) on the expanded dataset to generalize fault detection beyond static thresholds.  
* **Real-time Monitoring Dashboard:** Developing a user interface for real-time visualization of motor health and fault alerts.  
* **Wireless Communication:** Implementing Wi-Fi or Bluetooth for remote data transmission.  
* **Integration with Industrial Protocols:** Exploring compatibility with industrial communication standards for seamless integration into existing systems.

This project aims to contribute towards building a smart, low-cost, and real-time condition monitoring system for rotating machinery in diverse industrial environments.

## **🏁 Getting Started**

To set up and run this project locally:

### **Prerequisites**

* Arduino IDE installed.  
* Python 3.7+ installed.  
* Required Python libraries:  
  pip install pyserial pandas matplotlib numpy scipy

### **Hardware Connections**

Connect your ADXL345 sensor to your Arduino:

* ADXL345 VCC ➡️ Arduino 5V (or 3.3V depending on your sensor's operating voltage)  
* ADXL345 GND ➡️ Arduino GND  
* ADXL345 SDA ➡️ Arduino A4 (for Arduino Uno/Nano)  
* ADXL345 SCL ➡️ Arduino A5 (for Arduino Uno/Nano)

### **Instructions**

1. **Upload Arduino Sketch:**  
   * Open arduino\_adxl345\_sketch.ino in Arduino IDE.  
   * Select your Arduino board and the correct serial port under Tools \> Board and Tools \> Port.  
   * Upload the sketch to your Arduino.  
2. **Configure Python Data Collector:**  
   * Open vibration\_data\_collector.py.  
   * **Crucially, change the PORT variable** to match the serial port your Arduino is connected to (e.g., 'COM3' on Windows, '/dev/ttyACM0' on Linux).  
   * Set CSV\_FILE to vibration\_data\_normal\_moter.csv for healthy data, or vibration\_data\_imbalance\_moter.csv for faulty data.  
3. **Run Data Collection:**  
   * Execute the Python script from your terminal:  
     python vibration\_data\_collector.py

   * The script will collect data for the specified DURATION and save it to the CSV file.  
4. **Analyze Data:**  
   * Open vibration\_analyzer.py.  
   * Ensure the df \= pd.read\_csv(...) line points to the CSV file you want to analyze (e.g., vibration\_data\_normal\_moter.csv or vibration\_data\_imbalance\_moter.csv).  
   * Execute the Python script:  
     python vibration\_analyzer.py

   * This will display the vibration waveform, print statistics, and show the frequency spectrum.

## **🤝 Contributing**

Contributions, issues, and feature requests are welcome\!



## **📧 Contact**

**Kiran Bhusal** 

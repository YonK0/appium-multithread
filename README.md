# Set up appium with Simulator

Set up Appium with bluestack ( or any others simulators ) and python : 

1. python set up : 
  - pip install appium packages
  - appium driver install uiautomator2@2.0.1
  - pip install Appium-Python-Client

2. preinstallation for the envirenment : 
  - install android sdk using android studio 
  - install java jdk 
3. set windows envirenment (or linux ) : 
  - add ANDROID_HOME (system and local if that possible) : "C:\Users\Yonk0\AppData\Local\Android\Sdk\"
  - add JAVA_HOME (system variable) : "C:\Program Files\Java\jdk-22\"
  - add platform tools (like adb) in Path ( predifined variable in local ) : "C:\Users\ASUS\AppData\Local\Android\Sdk\platform-tools"

4. install Appium : 
    - install appium gui or run it using terminal to start your server 

5. restart pc (specially if you using Windows)

Optional : 
   - if you want restart appium server before runnig new script and close the old onces : "taskkill /F /IM node.exe"

# Appium multithread
in this example i worked with spotify apk , i may upload another complex scripts in the future.

NB : make sure you opened how much Bluestacks(in my case) instances.
the script will automatically adb connect to the opened bluestacks instances and automatically start appium session to different ports  

I hope this can be helpfull , i know sometimes videos can show better details , i may record a video that cover all the steps together if it necessary . 
Thanks for reading this first Article !



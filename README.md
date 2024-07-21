

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
  - 
  - add JAVA_HOME (system variable) : "C:\Program Files\Java\jdk-22\" (ps : linux don't need)
  - Download cmd tools


4. install Appium : 
    - install appium gui or run it using terminal to start your server 

5. restart pc (specially if you using Windows)

Optional : 
   - if you want restart appium server before runnig new script and close the old onces : "taskkill /F /IM node.exe"

# For linux you need this steps : 

after downloading android sdk cmd tools. 
```bash
  - 
    -mkdir -p ~/android-sdk/cmdline-tools
    export ANDROID_HOME=~/android-sdk
    export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
    export PATH=$PATH:$ANDROID_HOME/platform-tools
    
    
    cd ~/android-sdk/cmdline-tools/latest/bin
    ./sdkmanager --sdk_root=$ANDROID_HOME --update
    ./sdkmanager --sdk_root=$ANDROID_HOME "build-tools;31.0.0"
    
    #check apksigner 
    find $ANDROID_HOME -name "apksigner.jar"



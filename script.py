from appium import webdriver

# Set up desired capabilities
desired_caps = {
    "platformName": "iOS",
    "platformVersion": "17.6.1",  # Example: "15.0"
    "deviceName": "IPhone",  # Example: "iPhone 12"
    "udid": "00008101-001C29941A9B001E",  # You can get this from Xcode (described below)
    "xcodeOrgId": "your-team-id",  # Your Apple Developer team ID (get from Xcode)
    "xcodeSigningId": "iPhone Developer",  # Use iPhone Developer for non-App Store apps
    "app": "/path/to/your.app",  # Path to the .app file for your iOS app
    "automationName": "XCUITest",  # Appium's automation engine for iOS
}

# Start a session with Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Interact with the app
element = driver.find_element_by_accessibility_id("LoginButton")
element.click()

# Quit the session
driver.quit()
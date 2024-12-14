import os
import sys
import site

def get_pyqt_plugin_path():
    """Get the Qt plugin path for PyQt5."""
    try:
        # Get the Python executable directory
        python_executable = sys.executable
        python_directory = os.path.dirname(python_executable)
        print(f"[Debug] Python executable is located at: {python_executable}")
        
        # Try to find the site-packages directory relative to the Python executable
        site_packages_path = os.path.join(python_directory, "Lib", "site-packages")
        
        # If the script was launched using a specific Python executable, check this directory
        if os.path.exists(site_packages_path):
            print(f"[Debug] Searching for plugins in: {site_packages_path}")
            # Define the path to the Qt plugins
            qt_plugins_path = os.path.join(site_packages_path, "PyQt5", "Qt", "plugins", "platforms")
            
            # Check if the path exists
            if os.path.exists(qt_plugins_path):
                return qt_plugins_path
            else:
                print(f"[Error] Qt plugins path not found in: {qt_plugins_path}")
                return None
        else:
            print(f"[Error] site-packages not found in: {site_packages_path}")
            return None

    except Exception as e:
        print(f"[Error] An error occurred: {e}")
        return None

def set_qt_plugin_path():
    """Set the environment variable for Qt plugins."""
    plugin_path = get_pyqt_plugin_path()
    
    if plugin_path:
        # Set the environment variable for Qt plugin path
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path
        print(f"[Success] Qt plugin path set successfully: {plugin_path}")
    else:
        print("[Error] Failed to set Qt plugin path. Please check the path manually.")

def display_guide():
    """Display installation guide for Qt plugin path."""
    guide = """
    How to set the Qt plugin path manually:

    1. First, find the correct path to the PyQt5 plugins (the output of this script).
    2. If the script couldn't find it, you can manually navigate to your Python installation and find the 'platforms' directory in:
    
        <python_installation_path>/Lib/site-packages/PyQt5/Qt/plugins/platforms
    
    3. Set the environment variable QT_QPA_PLATFORM_PLUGIN_PATH to this path:
    
        - On Windows: set QT_QPA_PLATFORM_PLUGIN_PATH=<plugin_path>
        - On Linux/macOS: export QT_QPA_PLATFORM_PLUGIN_PATH=<plugin_path>
        
    4. Restart your application after setting the environment variable.
    """
    print(guide)

def main():
    """Main function to execute the script logic."""
    print("[Progress] Searching for PyQt5 plugin path based on the current Python environment...")
    
    plugin_path = get_pyqt_plugin_path()
    
    if plugin_path:
        print(f"[Success] Found Qt plugin path: {plugin_path}")
        set_qt_plugin_path()
    else:
        print("[Warning] Could not automatically set the Qt plugin path.")
        display_guide()

if __name__ == "__main__":
    main()

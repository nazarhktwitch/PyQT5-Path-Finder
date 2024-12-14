import os
import sys
import site

def get_pyqt_plugin_path():
    """Get the Qt plugin path for PyQt5."""
    try:
        # Get the path to the site-packages
        pyqt_path = site.getsitepackages()[0]  # Returns the first site-package directory
        # Define the path to the Qt plugins
        qt_plugins_path = os.path.join(pyqt_path, "PyQt5", "Qt", "plugins", "platforms")
        
        # Check if the path exists
        if not os.path.exists(qt_plugins_path):
            print(f"[Error] Qt plugins path not found: {qt_plugins_path}")
            return None
        
        return qt_plugins_path
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
    print("[Progress] Searching for PyQt5 plugin path...")
    
    plugin_path = get_pyqt_plugin_path()
    
    if plugin_path:
        print(f"[Success] Found Qt plugin path: {plugin_path}")
        set_qt_plugin_path()
    else:
        print("[Warning] Could not automatically set the Qt plugin path.")
        display_guide()

if __name__ == "__main__":
    main()

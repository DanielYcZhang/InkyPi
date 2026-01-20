# C-04: Debug Detective - Tracing Bugs Through the System

You've learned to trace CORRECT code execution. Now let's practice tracing BROKEN code!

---

## The Broken Plugin System

Someone tried to create a simple plugin system but made several mistakes. Your job: Find the bugs, explain WHY they're broken (connect to architecture concepts), and fix them.

---

## The Broken Code

```python
# File: plugin_loader.py (BROKEN VERSION)
#
# This code is supposed to:
# 1. Discover plugins in a folder
# 2. Load them dynamically
# 3. Call their process() method
# But it has 3 bugs!

import os
import importlib

class PluginLoader:
    def __init__(self, plugin_folder):
        self.plugin_folder = plugin_folder
        self.plugins = []
    
    def discover_plugins(self):
        """Find all .py files in plugin folder"""
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py'):
                # Bug #1 is somewhere in this section
                module_name = filename  # Load the module
                module = importlib.import_module(module_name)
                self.plugins.append(module)
        
        print(f"Loaded {len(self.plugins)} plugins")
    
    def run_all_plugins(self, data):
        """Run all loaded plugins"""
        results = []
        for plugin in self.plugins:
            # Bug #2 is in this section
            result = plugin.process(data)
            results.append(result)
        
        return results

# Usage:
loader = PluginLoader('plugins/')
loader.discover_plugins()

# Bug #3 is in this line:
output = loader.run_all_plugins({'input': 'hello'})
print(output)
```

---

## Step 1: PREDICT - What Will Break?

Before running the code, read it carefully and predict what will go wrong.

**Prediction 1 (Bug #1 - Module Loading)**:
```
I think this will fail because:
_____________

The error message will probably say:
_____________

This is broken because (architecture concept):
_____________
```

**Prediction 2 (Bug #2 - Plugin Execution)**:
```
I think this will fail because:
_____________

The error it causes:
_____________

This violates the principle of:
_____________
```

**Prediction 3 (Bug #3 - Missing Step)**:
```
I think there's a missing step:
_____________

Without it, the system will:
_____________

This shows a lack of:
_____________
```

---

## Step 2: RUN - See What Actually Breaks

Create the broken code and try to run it (or simulate):

```bash
# Create test structure:
mkdir -p test_plugins/plugins
cd test_plugins

# Create broken plugin_loader.py (copy code above)
# Create a sample plugin: plugins/hello_plugin.py
```

Sample plugin to test with:
```python
# plugins/hello_plugin.py
def process(data):
    return f"Hello, {data['input']}!"
```

**What happened when you ran it?**
```
Error message:
_____________

Which line failed:
_____________

Python's error message:
_____________
```

---

## Step 3: LOCATE - Find the Bugs

### Bug #1: Module Import

**Location**: Lines 14-16 in `discover_plugins()`

**The Problem**:
```
Line 15: module_name = filename
```

**Why This is Wrong**:
```
Explanation:
_____________

What it should be:
_____________

How I know (reference to Python module importing):
_____________
```

**Connect to InkyPi**: How does InkyPi's plugin_manager handle module names differently?
```
_____________
```

---

### Bug #2: Calling Plugin Methods

**Location**: Line 26 in `run_all_plugins()`

**The Problem**:
```
Line 26: result = plugin.process(data)
```

**Why This is Wrong**:
```
Explanation:
_____________

The assumption this makes:
_____________

Why this assumption fails:
_____________
```

**Connect to Architecture**: This is a "contract" violation. What contract? How should it be enforced?
```
_____________
```

**Connect to InkyPi**: How does InkyPi solve this problem (ensuring all plugins have the right methods)?
```
_____________
```

---

### Bug #3: Missing Discovery Call

**Location**: Lines 36-40 (usage section)

**The Problem**:
```
What's missing:
_____________

Why it's needed:
_____________

What happens without it:
_____________
```

**Connect to InkyPi**: When does InkyPi discover/load plugins? At startup? On request? Why does timing matter?
```
_____________
```

---

## Step 4: DIAGNOSE - Why Each Bug Exists

For each bug, explain the ROOT CAUSE (not just "it's wrong").

### Bug #1 Root Cause
**Surface problem**: Wrong module name format
**Deeper issue**: _____________
**Architecture lesson**: _____________

### Bug #2 Root Cause
**Surface problem**: Calling method on module not class
**Deeper issue**: _____________  
**Architecture lesson**: _____________

### Bug #3 Root Cause
**Surface problem**: Forgot to call discover
**Deeper issue**: _____________
**Architecture lesson**: _____________

---

## Step 5: FIX - Corrected Version

Write the FIXED version of the code:

```python
# File: plugin_loader.py (FIXED VERSION)

import os
import importlib
import inspect

class PluginLoader:
    def __init__(self, plugin_folder):
        self.plugin_folder = plugin_folder
        self.plugins = []
    
    def discover_plugins(self):
        """Find all .py files in plugin folder and load plugin classes"""
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                # FIX #1: Remove .py extension for module name
                module_name = filename[:-3]  # Remove '.py'
                
                # Import using the correct format
                # (Note: full path handling omitted for brevity)
                module = importlib.import_module(f"plugins.{module_name}")
                
                # FIX #2: Find classes in module that have 'process' method
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and hasattr(obj, 'process'):
                        plugin_instance = obj()  # Create instance
                        self.plugins.append(plugin_instance)
        
        print(f"Loaded {len(self.plugins)} plugins")
    
    def run_all_plugins(self, data):
        """Run all loaded plugins"""
        results = []
        for plugin in self.plugins:
            # Now plugin is an instance, so this works:
            result = plugin.process(data)
            results.append(result)
        
        return results

# Usage (FIXED):
loader = PluginLoader('plugins/')
# FIX #3: Call discover BEFORE running plugins!
loader.discover_plugins()  # Added this line

output = loader.run_all_plugins({'input': 'hello'})
print(output)
```

**Explain each fix**:

**Fix #1**:
```
_____________
```

**Fix #2**:
```
_____________
```

**Fix #3**:
```
_____________
```

---

## Step 6: REFLECT - What Did You Learn?

### Question 1: How would you DEBUG this if you didn't have the answers?
```
Step 1: _____________
Step 2: _____________
Step 3: _____________
```

### Question 2: What's the connection to InkyPi's design?
```
InkyPi avoids these bugs by:
- _____________
- _____________
- _____________
```

### Question 3: What architectural pattern would prevent Bug #2?
```
Pattern name: _____________
How it works: _____________
Example from InkyPi: _____________
```

---

## Success Criteria

Your debug_detective.md is complete when:
- ✅ You predicted all 3 bugs before running code
- ✅ You explained WHY each bug breaks (not just "it's wrong")
- ✅ You connected each bug to architecture concepts (contracts, discovery, etc.)
- ✅ You related fixes back to how InkyPi solves the same problems
- ✅ Your reflection shows systematic debugging thinking

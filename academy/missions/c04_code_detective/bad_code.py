# C-04: Progressive Refactoring Exercise
# From: Hard-Coded System → Configurable Architecture

# CONTEXT:
# You're building a notification system that handles different message types.
# Watch how architecture evolves from rigid to flexible!

# =============================================================================
# STAGE 1: Hard-Coded Notification System (Working but Rigid)
# =============================================================================

print("=== STAGE 1: Hard-Coded Version ===")

# Email notification
def send_email_notification():
    recipient = "user@example.com"  # Hard-coded
    subject = "Alert"  # Hard-coded
    message = "Something happened!"  # Hard-coded
    
    print(f"📧 Email to {recipient}")
    print(f"   Subject: {subject}")
    print(f"   Message: {message}")
    return "Email sent"

# SMS notification
def send_sms_notification():
    phone = "+1234567890"  # Hard-coded
    message = "Alert: Something happened!"  # Hard-coded
    
    print(f"📱 SMS to {phone}")
    print(f"   Message: {message}")
    return "SMS sent"

# Run both
send_email_notification()
send_sms_notification()

# THE PAIN: Everything is hard-coded! Can't customize without editing code.

# =============================================================================
# STAGE 2: Feature Request - "Make Messages Configurable"
# =============================================================================

print("\n=== STAGE 2: Add Configuration (Copy-Paste Approach) ===")

# TODO: Add message parameter to both functions
# Count how many lines you need to change!

def send_email_notification_v2(custom_message):
    recipient = "user@example.com"  # Still hard-coded
    subject = "Alert"
    message = custom_message  # Now configurable!
    
    print(f"📧 Email to {recipient}")
    print(f"   Subject: {subject}")
    print(f"   Message: {message}")
    return "Email sent"

def send_sms_notification_v2(custom_message):
    phone = "+1234567890"  # Still hard-coded
    message = custom_message  # Now configurable!
    
    print(f"📱 SMS to {phone}")
    print(f"   Message: {message}")
    return "SMS sent"

# Use with custom message
send_email_notification_v2("Server is down!")
send_sms_notification_v2("Server is down!")

# THE PAIN: We had to modify BOTH functions. What if we had 10 notification types?

# =============================================================================
# STAGE 3: Refactor with Base Class + Inheritance
# =============================================================================

print("\n=== STAGE 3: Architecture with BaseNotification ===")

class BaseNotification:
    """Base class defining the notification interface"""
    
    def __init__(self, message):
        self.message = message
    
    def send(self):
        """Must be implemented by subclasses"""
        raise NotImplementedError("Subclass must implement send()")
    
    def log(self):
        """Shared logging functionality"""
        print(f"[LOG] Notification sent: {self.message[:30]}...")

class EmailNotification(BaseNotification):
    def __init__(self, message, recipient="user@example.com"):
        super().__init__(message)
        self.recipient = recipient
        self.subject = "Alert"
    
    def send(self):
        print(f"📧 Email to {self.recipient}")
        print(f"   Subject: {self.subject}")
        print(f"   Message: {self.message}")
        self.log()  # Reuse base class method
        return "Email sent"

class SMSNotification(BaseNotification):
    def __init__(self, message, phone="+1234567890"):
        super().__init__(message)
        self.phone = phone
    
    def send(self):
        print(f"📱 SMS to {self.phone}")
        print(f"   Message: {self.message}")
        self.log()  # Reuse base class method
        return "SMS sent"

# Now usage is uniform!
notifs = [
    EmailNotification("Server is down!"),
    SMSNotification("Server is down!")
]

for notif in notifs:
    notif.send()  # Same interface for all!

# THE BENEFIT: Adding log() to base class updates ALL notifications automatically!

# =============================================================================
# STAGE 4: Second Feature Request - "Add Timestamps"
# =============================================================================

print("\n=== STAGE 4: Same Request, Way Easier! ===")

# TODO: Add timestamp to all notifications
# How many lines do you need to change NOW?

from datetime import datetime

class BaseNotification:
    """Enhanced base class"""
    
    def __init__(self, message):
        self.message = message
        self.timestamp = datetime.now()  # ← ONE LINE ADDED
    
    def send(self):
        raise NotImplementedError("Subclass must implement send()")
    
    def log(self):
        # Updated to include timestamp
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG {time_str}] Notification sent: {self.message[:30]}...")

# Email and SMS classes don't need to change!
# They automatically get timestamps through inheritance!

class EmailNotification(BaseNotification):
    def __init__(self, message, recipient="user@example.com"):
        super().__init__(message)  # Calls enhanced base __init__
        self.recipient = recipient
        self.subject = "Alert"
    
    def send(self):
        print(f"📧 Email to {self.recipient}")
        print(f"   Subject: {self.subject}")
        print(f"   Message: {self.message}")
        self.log()  # Now includes timestamp!
        return "Email sent"

class SMSNotification(BaseNotification):
    def __init__(self, message, phone="+1234567890"):
        super().__init__(message)
        self.phone = phone
    
    def send(self):
        print(f"📱 SMS to {self.phone}")
        print(f"   Message: {self.message}")
        self.log()  # Now includes timestamp!
        return "SMS sent"

# Test
notifs = [
    EmailNotification("Database backup complete"),
    SMSNotification("Database backup complete")
]

for notif in notifs:
    notif.send()

# THE VICTORY: Added timestamps with ~3 line changes instead of ~10!

# =============================================================================
# METRICS SUMMARY
# =============================================================================

print("\n=== Improvement Metrics ===")
print("Stage 2 (No Architecture):")
print("  - Modified functions: 2")
print("  - Lines changed: ~8")
print("  - Time: ~10 minutes (find all functions, edit each)")

print("\nStage 4 (With Architecture):")
print("  - Modified classes: 1 (BaseNotification only)")
print("  - Lines changed: ~3")
print("  - Time: ~3 minutes (one change, automatically propagates)")

print("\nImprovement ratio: 2.7:1 (lines)")
print("Time saved: 70%")

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

# 1. ARCHITECTURE PATTERN:
#    - BaseNotification = Contract (interface)
#    - Email/SMS = Implementations
#    - All share common behavior through inheritance

# 2. CODE READING CONNECTION:
#    - When you traced InkyPi, you saw this same pattern!
#    - BasePlugin = Contract
#    - CreatureCard/Clock = Implementations
#    - All share plugin loading behavior

# 3. SCALABILITY:
#    - Hard-coded: Adding 10th notification type = copy-paste nightmare
#    - Architecture: Adding 10th notification type = new class, automatic integration

# 4. WHY THIS MATTERS:
#    - Real systems have 100s of "types" (plugins, notifications, data processors)
#    - Good architecture makes systems GROW without complexity explosion
#    - Bad architecture = complexity grows exponentially with features

import time
import logging
from GPIO.opipc_gpio import OPIGPIO  # Import OPIGPIO from your GPIO folder

logging.basicConfig(level=logging.INFO)

def main():
    gpio = OPIGPIO()
    
    # Setup pin 10 as input for button
    gpio.pinMode(10, 'in')
    
    button_press_count = 0  # Counter for button presses
    prev_button_state = 0   # Previous state of the button
    debounce_time = 0.2     # Debounce time in seconds
    last_pressed_time = 0   # Time when the button was last pressed
    
    try:
        while True:
            # Read button state
            button_state = gpio.digitalRead(10)
            
            # Check for button press (LOW to HIGH transition)
            if button_state == 1 and prev_button_state == 0:
                current_time = time.time()
                
                # Debouncing: Only count if enough time has passed since last press
                if (current_time - last_pressed_time) > debounce_time:
                    # Update the last pressed time
                    last_pressed_time = current_time
                    
                    # Increment counter
                    button_press_count += 1
                
                    logging.info(f"Button pressed {button_press_count} times.")
            
            # Update previous button state
            prev_button_state = button_state
            
            time.sleep(0.05)  # Poll every 50 milliseconds
            
    except KeyboardInterrupt:
        logging.info("Exiting and cleaning up...")
        gpio.unexport(10)

if __name__ == "__main__":
    main()

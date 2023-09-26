import time
import logging
from GPIO.opipc_gpio import OPIGPIO  # Import OPIGPIO from your GPIO folder

logging.basicConfig(level=logging.INFO)


def main():
    gpio = OPIGPIO()

    # Setup pin 10 as input for button
    gpio.pinMode(20, "in")

    button_press_count = 0  # Counter for button presses
    prev_button_state = 0  # Previous state of the button

    try:
        while True:
            # Read button state
            button_state = gpio.digitalRead(20)

            # Check for button press (LOW to HIGH transition)
            if button_state == 1 and prev_button_state == 0:
                # Increment counter
                button_press_count += 1

                logging.info(f"Button pressed {button_press_count} times.")

                # Debouncing: Wait to avoid multiple counts
                time.sleep(0.5)

            # Update previous button state
            prev_button_state = button_state

            time.sleep(0.1)  # Poll every 100 milliseconds

    except KeyboardInterrupt:
        logging.info("Exiting and cleaning up...")
        gpio.unexport(20)


if __name__ == "__main__":
    main()

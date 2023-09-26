import time
import logging
from GPIO.opipc_gpio import OPIGPIO

logging.basicConfig(level=logging.INFO)


def main():
    gpio = OPIGPIO()

    # Setup pin 20 as output for LED
    gpio.pinMode(20, "out")

    # Setup pin 10 as input for button
    gpio.pinMode(10, "in")

    led_state = 0  # LED state (0=OFF, 1=ON)

    try:
        while True:
            # Read button state
            button_state = gpio.digitalRead(10)

            # Check if button is pressed
            if button_state == 1:
                # Toggle LED state
                led_state = 1 - led_state

                # Update LED
                gpio.digitalWrite(20, led_state)
                logging.info(f"LED set to {'ON' if led_state else 'OFF'}")

                # Debouncing: Wait to avoid multiple toggles
                time.sleep(0.5)

            time.sleep(0.1)  # Poll every 100 milliseconds

    except KeyboardInterrupt:
        logging.info("Exiting and cleaning up...")
        gpio.digitalWrite(20, 0)
        gpio.unexport(20)
        gpio.unexport(10)


if __name__ == "__main__":
    main()

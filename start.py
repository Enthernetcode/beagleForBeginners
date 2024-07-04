#import Adafruit_BBIO.GPIO as GPIO
import time

def introduction():
    print("Welcome to the BeagleBone Interactive Learning Script!")
    print("In this script, you'll learn how to use GPIO pins to control an LED and interact with buttons.")
    print("We'll cover setup, coding examples, and provide an interactive shell for practice.")
    print("Let's get started!\n")

def setup_led_blink():
    LED_PIN = "P9_14"
    GPIO.setup(LED_PIN, GPIO.OUT)

    def blink_led():
        while True:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(1)

    print("This section demonstrates how to blink an LED connected to the BeagleBone.")
    print("Press Ctrl+C to stop the blinking.\n")

    try:
        blink_led()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nBlinking stopped and GPIO cleaned up.")

def interactive_shell():
    print("\nInteractive Shell - Practice Your Skills!")
    print("You can run Python commands here to interact with the GPIO pins.")
    print("For example, try: GPIO.output('P9_14', GPIO.HIGH)")
    print("Type 'exit' to quit the interactive shell.\n")

    while True:
        try:
            user_input = input(">>> ")
            if user_input.lower() == 'exit':
                break
            exec(user_input)
        except Exception as e:
            print(f"Error: {e}")

def quiz():
    questions = [
        {
            "question": "What command is used to set up a GPIO pin for output in BeagleBone using the Adafruit_BBIO library?",
            "options": ["GPIO.configure(pin, GPIO.OUT)", "GPIO.setup(pin, GPIO.OUT)", "GPIO.setmode(pin, GPIO.OUT)", "GPIO.initialize(pin, GPIO.OUT)"],
            "answer": 1
        },
        {
            "question": "How do you clean up all GPIO settings to their default state?",
            "options": ["GPIO.reset()", "GPIO.cleanup()", "GPIO.clear()", "GPIO.reset_all()"],
            "answer": 1
        }
    ]

    print("\nQuiz Time!")
    score = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for j, option in enumerate(q["options"]):
            print(f"{j}. {option}")
        answer = int(input("Your answer (number): "))

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print(f"\nYou scored {score} out of {len(questions)}.")

def main():
    introduction()
    setup_led_blink()
    interactive_shell()
    quiz()
    print("\nThank you for using the BeagleBone Interactive Learning Script! Goodbye.")

if __name__ == "__main__":
    main()

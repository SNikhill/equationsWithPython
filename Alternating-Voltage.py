import matplotlib.pyplot as plt
import math


class voltageGraph:
    def __init__(self, frequency, peakVolatge):
        self.frequency = frequency
        self.peakVolatge = peakVolatge

    def voltage(self, atTime):
        return self.peakVolatge * math.sin(((2 * math.pi) / (self.frequency)) * atTime)

    def plot(self, timeStep, limit):
        currentTime = 0
        tillTime = limit
        print(
            "\n\n\nThere might be some precision difference in your calculations and the result\n\n\n"
        )
        timeValues = []
        voltageValues = []
        while currentTime <= tillTime:
            timeValues.append(currentTime)
            voltageValues.append(self.voltage(currentTime))
            currentTime += timeStep

        plt.plot(
            timeValues, voltageValues, color="Orange", label="Variation of Voltage"
        )

        plt.plot(timeValues, [0] * len(timeValues), color="black", label="Time (s)")
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        plt.legend()
        plt.show()


print(
    "\n\n\n\n \033[1m Alternating Voltage.\033[0m\n\nUSE SI UNITS ONLY. (Metre, Newton, Second, Hertz, Volts) \n\n\n\n"
)
v1 = voltageGraph(
    float(input("Enter: Frequency (Hz) => ")),
    float(input("Enter: Peak Volatge (V)=> ")),
)

v1.plot(float(input("Enter: Time Step => ")), float(input("Enter: Time Limit (s)=> ")))


# ==============================================================================
# Project: Fuzzy Logic Controller for Greenhouse Climate Automation
# Description: Custom implementation of a Mamdani Fuzzy Inference System 
#              solving Exercise 1 (UCA). Includes custom trapezoidal/triangular 
#              membership functions, rule evaluation, and centroid defuzzification.
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. Core Mathematical Membership Functions
# ------------------------------------------------------------------------------
def triangular_membership(x, a, b, c):
    """Computes the membership degree for a triangular fuzzy set."""
    cond1 = (x > a) & (x <= b)
    cond2 = (x > b) & (x < c)
    
    result = np.zeros_like(x, dtype=float)
    result[cond1] = (x[cond1] - a) / (b - a)
    result[cond2] = (c - x[cond2]) / (c - b)
    return result

def trapezoidal_membership(x, a, b, c, d):
    """Computes the membership degree for a trapezoidal fuzzy set."""
    cond1 = (x > a) & (x <= b)
    cond2 = (x > b) & (x <= c)
    cond3 = (x > c) & (x < d)
    
    result = np.zeros_like(x, dtype=float)
    if b > a: result[cond1] = (x[cond1] - a) / (b - a)
    else: result[cond1] = 1.0
    result[cond2] = 1.0
    if d > c: result[cond3] = (d - x[cond3]) / (d - c)
    else: result[cond3] = 1.0
    return result

# ------------------------------------------------------------------------------
# 2. Pipeline Execution Class
# ------------------------------------------------------------------------------
class GreenhouseFuzzyController:
    def __init__(self):
        # Universes of discourse
        self.x_temp = np.linspace(0, 40, 1000)
        self.x_hum  = np.linspace(0, 100, 1000)
        self.x_out  = np.linspace(-5, 5, 1000)
        
        # Define membership sets based on assignment parameters
        self.temp_L = trapezoidal_membership(self.x_temp, 0, 10, 20, 25)
        self.temp_N = triangular_membership(self.x_temp, 20, 25, 30)
        self.temp_H = trapezoidal_membership(self.x_temp, 25, 30, 40, 40)

    def plot_temperature_sets(self):
        """Solves Part (a): Graphical representation of Temperature membership functions."""
        plt.figure(figsize=(8, 4))
        plt.plot(self.x_temp, self.temp_L, label='Low (Bajo)', color='blue', lwd=2)
        plt.plot(self.x_temp, self.temp_N, label='Normal', color='green', lwd=2)
        plt.plot(self.x_temp, self.temp_H, label='High (Alto)', color='red', lwd=2)
        plt.title("Exercise 1(a): Temperature Membership Functions")
        plt.xlabel("Temperature (°C)")
        plt.ylabel("Membership Degree μ(x)")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        plt.show()

    def evaluate_inference(self, current_temp, current_hum):
        """Solves Part (b): Mamdani Max-Min Inference & Centroid Defuzzification."""
        # Fuzzification
        mu_temp_L = trapezoidal_membership(np.array([current_temp]), 0, 10, 20, 25)[0]
        mu_temp_N = triangular_membership(np.array([current_temp]), 20, 25, 30)[0]
        mu_temp_H = trapezoidal_membership(np.array([current_temp]), 25, 30, 40, 40)[0]
        
        mu_hum_L = trapezoidal_membership(np.array([current_hum]), 0, 0, 30, 40)[0]
        mu_hum_N = triangular_membership(np.array([current_hum]), 30, 40, 50)[0]
        mu_hum_H = trapezoidal_membership(np.array([current_hum]), 40, 50, 100, 100)[0]

        # Output Set Definitions (Shapes)
        out_Decrease = trapezoidal_membership(self.x_out, -5, -5, -2, 0)
        out_Maintain = triangular_membership(self.x_out, -2, 0, 2)
        out_Increase = trapezoidal_membership(self.x_out, 0, 2, 5, 5)

        # Rule evaluation (Matrix Intersection via Min operator)
        r1 = min(mu_temp_L, mu_hum_L)  # Rule 1 -> Maintain
        r2 = min(mu_temp_L, mu_hum_N)  # Rule 2 -> Increase
        r3 = min(mu_temp_L, mu_hum_H)  # Rule 3 -> Increase
        
        r4 = min(mu_temp_N, mu_hum_L)  # Rule 4 -> Maintain
        r5 = min(mu_temp_N, mu_hum_N)  # Rule 5 -> Maintain
        r6 = min(mu_temp_N, mu_hum_H)  # Rule 6 -> Decrease
        
        r7 = min(mu_temp_H, mu_hum_L)  # Rule 7 -> Maintain
        r8 = min(mu_temp_H, mu_hum_N)  # Rule 8 -> Decrease
        r9 = min(mu_temp_H, mu_hum_H)  # Rule 9 -> Decrease

        # Aggregation via Max operator
        act_Decrease = max(r6, r8, r9)
        act_Maintain = max(r1, r4, r5, r7)
        act_Increase = max(r2, r3)

        # Truncate Output distributions
        out_aggregated = np.maximum(
            np.minimum(act_Decrease, out_Decrease),
            np.maximum(np.minimum(act_Maintain, out_Maintain), 
                       np.minimum(act_Increase, out_Increase))
        )

        # Mathematical Centroid Defuzzification: ∫ x*μ(x) dx / ∫ μ(x) dx
        numerator = np.sum(self.x_out * out_aggregated)
        denominator = np.sum(out_aggregated)
        
        centroid = numerator / denominator if denominator != 0 else 0.0
        return centroid

# ------------------------------------------------------------------------------
# 3. Execution Pipeline
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    controller = GreenhouseFuzzyController()
    
    # Execute Part (a): Plotting curves
    controller.plot_temperature_sets()
    
    # Execute Part (b): Evaluating real sensor targets (Temp: 5°C, Hum: 35%)
    sensor_temp = 5.0
    sensor_hum  = 35.0
    
    output_signal = controller.evaluate_inference(sensor_temp, sensor_hum)
    print(f"\n--- EVALUATION RESULTS FOR EXERCISE 1(b) ---")
    print(f"Input Sensor States -> Temperature: {sensor_temp}°C | Humidity: {sensor_hum}%")
    print(f"Computed Control Output (Centroid Defuzzification): {output_signal:.4f} °C Variation")

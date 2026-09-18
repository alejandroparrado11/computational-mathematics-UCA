# ==============================================================================
# Project: Inverse Transform Method for Stochastic Simulation
# Description: Generating Heavy-Tailed (Pareto) and Short-Tailed (Exponential) 
#              distributions from Uniform pseudo-random numbers.
# ==============================================================================

# 1. Custom Pareto Probability Density & Cumulative Functions
dpareto <- function(x, beta, b) {
  if (beta <= 0 || b <= 0) stop("Parameters beta and b must be strictly positive.")
  ifelse(x < 0, 0, (beta * b^beta) / (x + b)^(beta + 1))
}

rpareto <- function(n, beta, b) {
  u <- runif(n)
  return(b * (1 - u)^(-1 / beta) - b)
}

# 2. Monte Carlo Verification Pipeline
run_pareto_simulation <- function(n = 500, beta = 10, b = 1) {
  cat("\n[+] Executing Pareto Simulation (n =", n, ", beta =", beta, ")\n")
  
  sampled_data <- rpareto(n, beta, b)
  
  # Structural Visualization
  hist(sampled_data, freq = FALSE, breaks = 25, col = "gold",
       main = "Empirical vs Theoretical Pareto Density", xlab = "Values")
  
  # Overlay theoretical mathematical continuous curve
  curve(dpareto(x, beta, b), from = 0, to = max(sampled_data), 
        add = TRUE, col = "darkblue", lwd = 3)
  
  cat("[-] Data range verified between:", min(sampled_data), "and", max(sampled_data), "\n")
}

# Execution Pipeline
par(mfrow = c(1, 1))
run_pareto_simulation()
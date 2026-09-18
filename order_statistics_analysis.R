# ==============================================================================
# Project: Order Statistics and Beta Distribution Asymptotics
# Description: Large-scale Matrix Simulation verifying that the k-th 
#              order statistic of a Uniform sample converges to a Beta distribution.
# ==============================================================================

analyze_order_statistics <- function(simulations = 10000, sample_size = 20) {
  cat("\n[+] Initializing Order Statistics Matrix Optimization...\n")
  
  # Allocate memory for computational matrix efficiency
  sim_matrix <- matrix(data = NA, nrow = simulations, ncol = sample_size)
  
  # Vectorized execution loop
  for (i in 1:simulations) {
    sim_matrix[i, ] <- sort(runif(sample_size))
  }
  
  # Extract the 14th Order Statistic (Expected to match Beta(14, 7))
  k_th_statistic <- sim_matrix[, 14]
  
  # Graphical Grounding
  hist(k_th_statistic, freq = FALSE, col = "lightblue", breaks = 30,
       main = "14th Order Statistic Convergence to Beta(14,7)", xlab = "X_(14)")
  
  curve(dbeta(x, shape1 = 14, shape2 = 7), from = 0, to = 1, 
        add = TRUE, col = "darkred", lwd = 3)
}

# Execution Pipeline
analyze_order_statistics()
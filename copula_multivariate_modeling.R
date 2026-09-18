# ==============================================================================
# Project: Multivariate Risk Modeling using Clayton & FGM Copulas
# Description: Simulation of bivariate and trivariate distributions 
#              with non-linear dependencies and custom marginals.
# ==============================================================================

# Custom library verification and attachment
required_packages <- c("copula", "scatterplot3d")
invisible(lapply(required_packages, function(pkg) {
  if (!require(pkg, character.only = TRUE)) install.packages(pkg, dependencies = TRUE)
  library(pkg, character.only = TRUE)
}))

# ------------------------------------------------------------------------------
# 1. Bivariate Clayton Copula Simulation
# ------------------------------------------------------------------------------
simulate_clayton_dependency <- function(theta = 6, sample_size = 4700) {
  cat("\n[+] Generating Clayton Copula with Theta =", theta, "\n")
  
  clayton_copula <- claytonCopula(param = theta, dim = 2)
  copula_sample  <- rCopula(n = sample_size, copula = clayton_copula)
  
  # Plot statistical dependencies
  plot(copula_sample, main = paste("Clayton Copula Matrix (Theta =", theta, ")"),
       xlab = "U1", ylab = "U2", col = rgb(0, 0, 0.5, 0.2), pch = 19)
  
  linear_corr <- cor(copula_sample[, 1], copula_sample[, 2], method = "pearson")
  cat("[-] Computed Pearson Correlation:", round(linear_corr, 4), "\n")
  return(copula_sample)
}

# ------------------------------------------------------------------------------
# 2. Multivariate Distribution with Exponential Marginals (Financial Risk Analogy)
# ------------------------------------------------------------------------------
simulate_multivariate_exponential <- function() {
  cat("\n[+] Modeling Bivariate Exponential Distribution via Clayton Copula\n")
  
  # Marginals: Asset A (rate = 1/3), Asset B (rate = 10)
  mvdc_model <- mvdc(
    copula   = claytonCopula(param = 6, dim = 2),
    margins  = c("exp", "exp"),
    paramMargins = list(list(rate = 1/3), list(rate = 10))
  )
  
  simulated_data <- rMvdc(n = 500, mvdc = mvdc_model)
  
  plot(simulated_data, main = "Bivariate Exponential Returns Map",
       xlab = "Asset X Risk Profile", ylab = "Asset Y Risk Profile", 
       col = "darkblue", pch = 20)
}

# Execution Pipeline
par(mfrow = c(1, 2))
clayton_data <- simulate_clayton_dependency(theta = 6)
simulate_multivariate_exponential()
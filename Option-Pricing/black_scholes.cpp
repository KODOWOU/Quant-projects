#include <iostream>
#include <cmath>
#include <random>

// Normal CDF using approximation
double normal_cdf(double x) {
    return 0.5 * erfc(-x * M_SQRT1_2);
}

// Black-Scholes formula for European Call
double black_scholes_call(double S, double K, double T, double r, double sigma) {
    double d1 = (log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrt(T));
    double d2 = d1 - sigma * sqrt(T);

    return S * normal_cdf(d1) - K * exp(-r * T) * normal_cdf(d2);
}

// Black-Scholes formula for European Put
double black_scholes_put(double S, double K, double T, double r, double sigma) {
    double d1 = (log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * sqrt(T));
    double d2 = d1 - sigma * sqrt(T);

    return K * exp(-r * T) * normal_cdf(-d2) - S * normal_cdf(-d1);
}

// Monte Carlo pricing for European Call
double monte_carlo_call(double S, double K, double T, double r, double sigma, int n_simulations) {
    std::mt19937 gen(42);
    std::normal_distribution<> d(0.0, 1.0);

    double payoff_sum = 0.0;

    for (int i = 0; i < n_simulations; ++i) {
        double Z = d(gen);
        double ST = S * exp((r - 0.5 * sigma * sigma) * T + sigma * sqrt(T) * Z);
        payoff_sum += std::max(ST - K, 0.0);
    }

    return exp(-r * T) * (payoff_sum / n_simulations);
}

int main() {

    // Parameters
    double S = 100.0;    // Spot price
    double K = 100.0;    // Strike
    double T = 1.0;      // Time to maturity (years)
    double r = 0.05;     // Risk-free rate
    double sigma = 0.2;  // Volatility

    int n_simulations = 100000;

    // Analytical pricing
    double call_price = black_scholes_call(S, K, T, r, sigma);
    double put_price  = black_scholes_put(S, K, T, r, sigma);

    // Monte Carlo pricing
    double mc_price = monte_carlo_call(S, K, T, r, sigma, n_simulations);

    std::cout << "Black-Scholes Call Price: " << call_price << std::endl;
    std::cout << "Black-Scholes Put Price:  " << put_price << std::endl;
    std::cout << "Monte Carlo Call Price:   " << mc_price << std::endl;

    return 0;
}

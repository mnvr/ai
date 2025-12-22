# ML related math symbols

| Symbol       | Name / Pron.               | tldr                            | Notes                                                                                                                                        |
| ------------ | -------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Δ**        | Uppercase delta            | A finite, discrete change       | The actual difference, `Δx = x₂-x₁`, "Delta x", measuring how much x actually changed.                                                       |
| **δ**        | Lowercase delta            |                                 |
| **d**        | Latin d "dee"              | An infinitesimally small change | The calculus version. `df/dx = lim(Δx→0) Δf/Δx`                                                                                              |
| **∂**        | Curly d "partial" or "del" | Partial derivative              | Rate of change w.r.t. one variable (others kept constant). `∂f/∂x` "del f del x" derivative of f w.r.t. x, holding other variables constant. |
| **∇**        | Nabla, "del", gradient     | Vector of all partial derivates |                                                                                                                                              |
| **Σ**        | Sigma                      | Summation                       |                                                                                                                                              |
| **Π**        | Pi                         | Product                         |                                                                                                                                              |
| **θ**        | Theta                      | Model parameters (weights)      |                                                                                                                                              |
| **α**, **η** | Alpha, Eta                 | Learning rate                   |                                                                                                                                              |
| **ε**        | Epsilon                    |                                 | Small constant for numerical stability                                                                                                       |
| **‖x‖**      | Norm                       | "size"/"length" of a vector     |                                                                                                                                              |
| **x̂**, **ŷ** | x hat, y hat               | Prediction / estimate           |
| **x\***      | x star                     | Optimal value                   |                                                                                                                                              |

**Chain rule** - the heart of backprop

```
∂x/∂y = (∂x/∂z) (∂z/∂y)
```

**Core update rule**

```
θ ← θ - α . ∂L/∂θ
```

Update parameters by subtracting learning rate times the gradient of loss with respect to parameters.

In vector form

```
θ ← θ - α . ∇L(θ)
```

### Jacobian

The gradient ∇ is a special case - the transpose of the 1×n Jacobian **J** when the output is scalar.

**Gradient ∇** - For `f: ℝⁿ → ℝ` (many inputs, one output)

```
∇f =
| ∂f/∂x₁ |
| ∂f/∂x₂ |
| ...    |
| ∂f/∂xₙ |
```

**Jacobian J** - For `f: ℝⁿ → ℝᵐ` (many inputs, many outputs)

```
J = | ∂f₁/∂x₁  ∂f₁/∂x₂  ...  ∂f₁/∂xₙ |
    | ∂f₂/∂x₁  ∂f₂/∂x₂  ...  ∂f₂/∂xₙ |
    | ...                            |
    | ∂fₘ/∂x₁  ∂fₘ/∂x₂  ...  ∂fₘ/∂xₙ |
```

This matrix of ratios tells how a small change in inputs propagates to outputs. Each element is a multiplier - how many units of output change per unit of input change. It's a rate, like a slope. So `∂f₁/∂x₁ = 2` means `Δf₁ ≈ 2 . Δx₁`.

The Jacobian is thus a linear approximation of a nonlinear function at a point - the multivariable generalization of "slope". If we nudge the input by a tiny vector `δ`, the output changes by approx `δ_out = J . δ_inp`.

In a backprop context, we mostly deal with gradients because loss is scalar.

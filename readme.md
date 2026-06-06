Dataset:

    Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220. RRID:SCR_007345.


# Critical Scale Invariance in a Healthy Human Heart Rate

## The Physical Idea

<p align="center">
  <img src="heartbeat.jpg" alt="heartbeat">
</p>

A healthy heart is **not a metronome**. Its beat-to-beat intervals fluctuate in a structured, non-random way. The paper by Kiyono et al. argues this fluctuation has a **fractal, scale-free structure** - the same statistical signature we see in systems sitting at a **critical point** (like water at exactly 100°C, or a magnet at its Curie temperature). This is not trivial: it means the heart's regulatory system is continuously tuned to operate near criticality, which is associated with maximum adaptability and sensitivity.

---

## Step by Step

### 1. From RR intervals to b(i)
We measure the time between consecutive R-peaks (the big spike in an ECG). That gives us a sequence of intervals - say 0.82s, 0.79s, 0.85s, ... We then **normalise** it:

$$b(i) = \frac{RR(i) - \mu}{\sigma}$$

This removes the mean heart rate and units, leaving only the *fluctuation structure*.

---

### 2. The cumulative series B(i)
We sum b(i) to get:

$$B(i) = \sum_{j=1}^{i} b(j)$$

This turns the heartbeat series into a **random walk**. Why? Because integration amplifies long-range correlations and makes them easier to detect. A purely random heartbeat would give a standard Brownian walk. A correlated one gives a different kind of walk - described by the Hurst exponent.

---

### 3. Polynomial detrending (DFA)
We chop B(i) into windows of size *s* and fit a polynomial to each window. The **residuals** are the fluctuations after removing local trends. This is the core of **Detrended Fluctuation Analysis (DFA)** - it lets us study correlations without being fooled by slow drifts (like the subject gradually relaxing).

The RMS of those residuals is F(s). If:

$$F(s) \sim s^H$$

then *H* is the **Hurst exponent**. For healthy hearts, H ≈ 1.0, meaning the fluctuations are **1/f noise** - long-range correlated, not random (H=0.5 would be white noise).

---

### 4. The PDF and fat tails
At each scale *s*, we compute lag increments:

$$\Delta B(s, i) = B(i+s) - B(i)$$

and build a histogram. The key finding: **this is not Gaussian**. The tails are much fatter - large fluctuations happen far more often than a Gaussian predicts.

The right fit is a **q-Gaussian** (from Tsallis non-extensive statistics):

$$p(x) \propto \left[1 - (1-q)\beta x^2\right]^{\frac{1}{1-q}}$$

When q=1 this reduces to a Gaussian. When q>1 we get power-law tails. A healthy heart gives q ≈ 1.5, meaning extreme heart rate changes are significantly more probable than classical statistics would predict - the heart is built to handle (and produce) surprises.

---

### 5. The collapse plot - the smoking gun
This is the key test for **scale invariance**. We compute the PDF at many different scales s = 16, 32, 64, 128, 256 beats. Each PDF has a different width. We then rescale:

- x-axis: divide by $s^H$
- y-axis: multiply by $s^H$ (to conserve probability)

If the system is truly scale-invariant, **all curves collapse onto one master curve**. This is exactly what happens for a healthy heart - and it's what we'd expect from a system at a critical point, where there is no preferred length (or time) scale.

---

## The Big Picture

| Property | Random heart | Healthy heart |
|---|---|---|
| Hurst H | 0.5 (white noise) | ~1.0 (1/f, long-range correlated) |
| PDF shape | Gaussian | q-Gaussian, fat tails |
| Scale invariance | No collapse | Clean collapse |

The healthy heart sits in a **critical state** - not by accident, but because it's continuously regulated there. This gives it maximum dynamic range and the ability to respond rapidly to wildly different demands. A diseased heart (e.g. congestive heart failure) loses these correlations and becomes either more random or more periodic - both are worse.
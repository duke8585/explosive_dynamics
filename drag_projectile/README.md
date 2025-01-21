# calculating projectile velocity loss due to drag coefficient

`python drag_projectile.py`

via drag equation and newtons 2nd law, [using chatgpt pro 4o](https://chatgpt.com/share/e/678fc590-1c20-800d-8d57-4f64b2d7dad6)

## Derivation of the Velocity-Time Formula for a Projectile with Drag

The velocity-time formula for a projectile subjected to drag can be derived using Newton's second law and the drag equation. Below is the detailed step-by-step derivation.

---

## Step 1: Newton's Second Law
Newton's second law states:
\[
m a = F_{\text{net}}
\]
For a projectile subjected only to drag force (neglecting gravity for simplicity):
\[
m \frac{dv}{dt} = -F_d
\]

---

## Step 2: Drag Force
The drag force is given by:
\[
F_d = \frac{1}{2} \rho C_d A v^2
\]
where:
- \( \rho \): Air (or medium) density \((\text{kg/m}^3)\)
- \( C_d \): Drag coefficient (dimensionless)
- \( A \): Projected area of the projectile \((\text{m}^2)\)
- \( v \): Velocity \((\text{m/s})\)

Substituting the drag force into the equation:
\[
m \frac{dv}{dt} = -\frac{1}{2} \rho C_d A v^2
\]

---

## Step 3: Simplify and Isolate \( \frac{dv}{dt} \)
Rearrange to:
\[
\frac{dv}{dt} = -\frac{\rho C_d A}{2m} v^2
\]
Define a constant \( k \):
\[
k = \frac{\rho C_d A}{2m}
\]
This simplifies the equation to:
\[
\frac{dv}{dt} = -k v^2
\]

---

## Step 4: Separate Variables
Rearrange to separate variables:
\[
\frac{dv}{v^2} = -k \, dt
\]

---

## Step 5: Integrate Both Sides
The integral of \( \frac{1}{v^2} \) with respect to \( v \):
\[
\int \frac{1}{v^2} \, dv = -\int k \, dt
\]
\[
-\frac{1}{v} = -kt + C
\]

Simplify:
\[
\frac{1}{v} = kt + C
\]

---

## Step 6: Solve for \( v \)
Rearrange to solve for \( v \):
\[
v = \frac{1}{kt + C}
\]

---

## Step 7: Apply Initial Condition
At \( t = 0 \), the velocity is \( v_0 \):
\[
v_0 = \frac{1}{C}
\]
\[
C = \frac{1}{v_0}
\]

Substitute \( C \) back into the equation:
\[
v(t) = \frac{1}{kt + \frac{1}{v_0}}
\]

Simplify:
\[
v(t) = \frac{v_0}{1 + v_0 k t}
\]

---

## Final Formula
The velocity of the projectile as a function of time is:
\[
v(t) = \frac{v_0}{1 + \frac{\rho C_d A v_0}{2m} t}
\]

---

## Parameters:
- \( v_0 \): Initial velocity \((\text{m/s})\)
- \( \rho \): Air (or medium) density \((\text{kg/m}^3)\)
- \( C_d \): Drag coefficient (dimensionless)
- \( A \): Projected area of the projectile \((\text{m}^2)\)
- \( m \): Mass of the projectile \((\text{kg})\)
- \( t \): Time \((\text{s})\)

---

This formula describes how velocity decreases over time due to drag acting on the projectile.

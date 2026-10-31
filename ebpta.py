import numpy as np

# Training dataset
X = np.array([
    [2, 50],
    [3, 55],
    [4, 60],
    [5, 70],
    [6, 75],
    [7, 85]
], dtype=float)

Y = np.array([[0], [0], [0], [1], [1], [1]], dtype=float)

# Normalize input values
X = X / np.array([7, 100])

# Initialize weights and biases
np.random.seed(1)

W1 = np.random.randn(2, 4) * 0.5
B1 = np.zeros((1, 4))

W2 = np.random.randn(4, 1) * 0.5
B2 = np.zeros((1, 1))

learning_rate = 0.8
epochs = 20000


# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# EBPTA Training
for epoch in range(epochs):

    # 1. Forward Pass
    H = sigmoid(np.dot(X, W1) + B1)
    O = sigmoid(np.dot(H, W2) + B2)

    # 2. Calculate output delta
    delta_output = (Y - O) * O * (1 - O)

    # 3. Backpropagation to hidden layer
    delta_hidden = np.dot(delta_output, W2.T) * H * (1 - H)

    # 4. Update weights and biases
    W2 += learning_rate * np.dot(H.T, delta_output) / len(X)
    B2 += learning_rate * np.mean(delta_output, axis=0, keepdims=True)

    W1 += learning_rate * np.dot(X.T, delta_hidden) / len(X)
    B1 += learning_rate * np.mean(delta_hidden, axis=0, keepdims=True)


# Prediction function
def predict(hours, attendance):
    x = np.array([[hours / 7, attendance / 100]])

    hidden = sigmoid(np.dot(x, W1) + B1)
    output = sigmoid(np.dot(hidden, W2) + B2)

    return output[0][0]


# Check training data
print("\nTraining Completed!")
print("\nChecking Training Data:\n")

for i in range(len(X)):
    output = predict(
        X[i][0] * 7,
        X[i][1] * 100
    )

    actual = "Pass" if Y[i][0] == 1 else "Fail"
    predicted = "Pass" if output >= 0.5 else "Fail"

    print(
        "Hours:", int(X[i][0] * 7),
        "Attendance:", int(X[i][1] * 100),
        "Actual:", actual,
        "Predicted:", predicted
    )


# Test new student
print("\n----------------------------------")
print("TEST THE TRAINED EBPTA SYSTEM")
print("----------------------------------")

hours = float(input("Enter Hours Studied: "))
attendance = float(input("Enter Attendance (%): "))
target = int(input("Enter Expected Target (0 = Fail, 1 = Pass): "))

output = predict(hours, attendance)

if output >= 0.5:
    result = "Pass"
else:
    result = "Fail"

print("\nEBPTA Prediction:", result)
print("Output Value:", round(output, 2))

# Check correctness
prediction = 1 if output >= 0.5 else 0

if prediction == target:
    print("\nPrediction is CORRECT")
else:
    print("\nPrediction is INCORRECT")

from sklearn.neural_network import MLPClassifier

# Input data
X = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

# Target output (XOR)
y = [0, 1, 1, 0]

# Create MLP model
mlp = MLPClassifier(
    hidden_layer_sizes=(4,),
   # activation='tanh',
    #solver='lbfgs',
    max_iter=1000,
    random_state=1
)

# Train the model
mlp.fit(X, y)

# Predict output
prediction = mlp.predict(X)

# Display results
print("Input:")
print(X)

print("Actual Output:")
print(y)

print("Predicted Output:")
print(prediction)

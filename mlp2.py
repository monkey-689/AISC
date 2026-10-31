# Student Pass/Fail Prediction using MLP Classifier

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# 1. Create training dataset
X = [[1], [2], [3], [5], [6], [7]]
y = [0, 0, 0, 1, 1, 1]

# 2. Create and train MLP Classifier
model = make_pipeline(
    StandardScaler(),
    MLPClassifier(
        hidden_layer_sizes=(5,),
        max_iter=5000,
        random_state=1
    )
)

model.fit(X, y)

# 3. Accept input from user
hours = float(input("Enter hours studied: "))

# 4. Predict result
prediction = model.predict([[hours]])

if prediction[0] == 1:
    print("Result: Pass")
else:
    print("Result: Fail")

# 5. Display training accuracy
accuracy = model.score(X, y)
print("Training Accuracy:", accuracy * 100, "%")

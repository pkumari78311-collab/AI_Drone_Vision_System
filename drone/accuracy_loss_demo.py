# Example training values

loss_values = [1.0, 0.8, 0.6, 0.4, 0.2]

accuracy_values = [50, 65, 78, 89, 96]

epochs = len(loss_values)

for i in range(epochs):
    print("Epoch", i + 1)
    print("Loss =", loss_values[i])
    print("Accuracy =", accuracy_values[i], "%")
    print()
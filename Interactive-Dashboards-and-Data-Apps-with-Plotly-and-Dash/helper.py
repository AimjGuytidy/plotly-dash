def plot_loss_acc(history):
  loss = history.history["loss"]
  val_loss = history.history["val_loss"]

  accuracy = history.history["accuracy"]
  val_accuracy = history.history["val_accuracy"]

  epochs = history.epoch

  plt.figure()
  plt.plot(epochs,loss,label="loss",color = "magenta")
  plt.plot(epochs,val_loss,label="val_loss",color="green")
  plt.title("Loss")
  plt.legend()


  plt.figure()
  plt.plot(epochs,accuracy,label="accuracy",color = "orange")
  plt.plot(epochs,val_accuracy,label="val_accuracy",color="blue")
  plt.title("Accuracy")
  plt.legend()


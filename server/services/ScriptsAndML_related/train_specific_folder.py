from imageai.Prediction.Custom import ModelTraining

# thought it would improve training time (didn't improve for omri)
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("omri")
model_trainer.trainModel(num_objects=2, num_experiments=1, enhance_data=True, batch_size=3, show_network_summary=True)
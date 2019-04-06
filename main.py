import os
os.system('mkdir facesData')
os.system('python face_scanner.py')
os.system('python face_trainer.py')
os.system('python faceDETECTOR.py')

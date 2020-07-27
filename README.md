# Facepose

Estimating the pose of human face.

## Usage

Calibrate your camera before estimate pose.

### Calibration

Start chessboard web application.

`$ node http.js`

Open the web application with your phone and take pictures with your camera.

Put chessboard pictures in `/assets/img/`.

Calibration the camera.

`$ python -m calibration`

### Estimation

`$ python -m estimation`

## License

[MIT](https://github.com/akijoey/facepose/blob/master/LICENSE) © AkiJoey

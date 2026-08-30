# Browser Eye Tracking Tool

A static browser-based eye tracking experiment tool powered by WebGazer.js. The current project uses one webcam, runs entirely in the browser, and maps gaze estimates onto a printed landscape A4 paper coordinate system.

## Features

- Single-webcam WebGazer tracking
- Printed landscape A4 paper 9-point calibration with operator confirmation
- Camera preview step before calibration for eye-position alignment
- Participant ID input
- Up to five preloaded stimulus images
- Multi-image tracking sessions under one calibration
- A4-mapped heatmap, gaze path, and CSV export
- Time-range filtering for heatmaps and gaze paths
- Transparent PNG layer export for heatmaps and gaze paths
- Participant archive import and export

## Project files

- `index.html` defines the static UI.
- `style.css` contains all styling.
- `app.js` contains the app state, calibration flow, tracking flow, visualization, and import/export logic.
- `webgazer.js` is the local WebGazer bundle.
- `mediapipe/face_mesh/` is required by the bundled WebGazer tracker through `faceMeshSolutionPath`; keep this directory when publishing.

## Presentation Slide Deck

The repository also includes the master's research presentation deck:

- Install dependencies: `npm ci`
- Build the deck: `npm run build`
- Output artifact: `dist/index.html` (generated standalone HTML bundle, do not edit directly)
- Development server: `npm start`

## GitHub Pages

This project is a static site. Publish the repository from the `main` branch and the repository root.

# Scoping Assistant Plugin

A comprehensive scoping assistant for project analysis, service proposal generation, and scoping questions. This plugin helps analyze inputs, generate assumptions, and create project blueprints.

## Features

- **Project Analysis**: Analyze form inputs and transcripts to extract key information
- **Service Proposal Generation**: Generate service proposals with estimated days and assumptions
- **Scoping Questions**: Generate relevant scoping questions based on project context
- **Blueprint Creation**: Create project blueprints based on selected use cases
- **Interactive UI**: Modern Quasar/Vue.js interface for seamless user experience

## Installation

1. Copy this plugin directory to your Dataiku plugins folder
2. Install the plugin through the Dataiku interface
3. Create a new webapp using the "Scoping Assistant" template

## Configuration

The plugin provides several configuration options:

- **Data Storage**: Optional dataset for storing scoping history
- **Documents Folder**: Optional folder for storing uploaded documents
- **API Settings**: Configure timeouts and logging
- **Content Generation**: Enable/disable mock data for testing
- **UI Settings**: Theme and debug options

## API Endpoints

The plugin provides the following REST API endpoints:

- `GET /api/hello` - Health check
- `POST /api/generate-summary` - Generate project summary
- `POST /api/fetch-similar-docs` - Fetch similar documents
- `POST /api/generate-service-days` - Generate service day estimates
- `POST /api/generate-assumptions` - Generate project assumptions
- `POST /api/fetch-use-cases` - Fetch relevant use cases
- `POST /api/generate-blueprints` - Generate project blueprints
- `POST /api/scoping/analyze-inputs` - Analyze form inputs
- `POST /api/scoping/analyze-transcripts` - Analyze transcripts
- `POST /api/scoping/generate-questions` - Generate scoping questions
- `GET /api/config` - Get webapp configuration

## Development

The plugin is built using:

- **Backend**: Python Flask with Dataiku integration
- **Frontend**: Quasar/Vue.js framework
- **Build System**: Vite for modern frontend bundling

## License

MIT License

## Author

Reda Affane 
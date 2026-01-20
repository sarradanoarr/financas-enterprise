const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ 
    message: '🚀 Finanças Enterprise API v1.0 - Online!',
    status: 'success',
    timestamp: new Date().toISOString()
  });
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', uptime: process.uptime() });
});

app.get('/api', (req, res) => {
  res.json({ 
    endpoints: ['/api/health', '/api/usuarios', '/api/financeiro'],
    version: '1.0',
    deploy: 'Vercel'
  });
});

module.exports = app;

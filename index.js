module.exports = (req, res) => {
  res.json({ 
    message: '🚀 Finanças Enterprise API - FUNCIONANDO!',
    status: 'success',
    endpoints: ['/health', '/predict/PETR4.SA', '/dashboard']
  });
};

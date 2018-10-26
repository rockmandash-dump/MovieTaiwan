import React from 'react';
import { render } from 'react-dom';
import App from './App.jsx';

import { AppContainer } from 'react-hot-loader';

const renderApp = () => {
  render(
    <AppContainer>
      <App />
    </AppContainer>,
    document.getElementById('app')
  );
};

renderApp();

// ================================================
// HMR
// ================================================

if (module.hot) {
  module.hot.accept('./App.jsx', renderApp);
}

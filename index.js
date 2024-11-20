import React from "react";
import ReactDOM from "react-dom";
import { Auth0Provider } from "@auth0/auth0-react";
import App from "./App";

// Replace these with your Auth0 domain and client ID
const domain = "dev-adyj5zda1ywhc60l.us.auth0.com";
const clientId = "xxMiJp9xd25TaxCDjREWw5YEXlYsvpha";

ReactDOM.render(
  <Auth0Provider
    domain={domain}
    clientId={clientId}
    authorizationParams={{
      redirect_uri: window.location.origin, // Redirect after login
    }}
  >
    <App />
  </Auth0Provider>,
  document.getElementById("root")
);

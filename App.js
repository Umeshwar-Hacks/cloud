import React from "react";
import { useAuth0 } from "@auth0/auth0-react";

function App() {
  const { loginWithRedirect, logout, user, isAuthenticated, isLoading } =
    useAuth0();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="App">
      <h1>Welcome to Auth0 React SPA</h1>

      {!isAuthenticated ? (
        <button onClick={() => loginWithRedirect()}>Log In</button>
      ) : (
        <>
          <button onClick={() => logout({ logoutParams: { returnTo: window.location.origin } })}>
            Log Out
          </button>
          <h2>User Profile</h2>
          <img src={user.picture} alt={user.name} />
          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
        </>
      )}
    </div>
  );
}

export default App;

const authEndpoint = "https://accounts.spotify.com/authorize";
const redirectUri = "localhost:3000";
const clientId = "41aacb7de87347a28af75fa5a557c3a9";

const scopes = [
  "streaming",
  "user-read-email",
  "user-read-private",
];

export const loginUrl = `${authEndpoint}?client_id=${clientId}&response_type=code&redirect_uri=${redirectUri}&scope=${scopes.join(
  "%20"
)}`;
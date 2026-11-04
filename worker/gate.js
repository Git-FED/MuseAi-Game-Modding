// Cloudflare Worker sketch: server-side gate contract, not a provider webhook implementation.
// Configure ACCESS_KV and ACCESS_HMAC_SECRET as Worker bindings/secrets.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/advanced.html") return env.ASSETS.fetch(request);
    const token = request.headers.get("Cookie")?.match(/mg_access=([^;]+)/)?.[1];
    if (!token || !(await verifyToken(token, env.ACCESS_HMAC_SECRET))) {
      return Response.redirect(`${url.origin}/support.html`, 302);
    }
    return env.ASSETS.fetch(new Request(new URL("/advanced.html", url), request));
  }
};

async function verifyToken(token, secret) {
  // Replace with your reviewed JWT/HMAC implementation and entitlement lookup.
  // Never treat this sketch as production authentication.
  return false;
}

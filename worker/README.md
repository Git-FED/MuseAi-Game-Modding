# Cloudflare Worker gate

Static HTML cannot securely gate content after a payment. Do not trust a query string, local storage value, hidden HTML, or client-side JavaScript flag.

Use a Cloudflare Worker in front of `advanced.html`:

1. Verify provider webhooks using the provider's official signature verification and a Worker secret.
2. Store only the minimum entitlement record in KV or D1.
3. After an authenticated user session, issue a short-lived, signed access token.
4. On `/advanced.html`, verify the token with Web Crypto before returning protected HTML.
5. Keep provider secrets, webhook signing secrets, and HMAC keys out of GitHub and out of browser code.
6. Return an HTML response or an HTML redirect for every user-facing failure; do not return raw plaintext errors.

The payment buttons in `../support.html` are hosted-provider UI. A successful browser return is not proof of payment. The included `support-success.html` intentionally says so.

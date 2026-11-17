# RAMN IPA Portal

- Public frontend: GitHub Pages
- Private code verification: Flask API on Render
- Access codes are configured only as Render environment variables, never committed to this repository.
- Set `ACCESS_CODES` to the comma-separated list of 20 codes.
- Set `DOWNLOAD_URL` after the IPA is uploaded to a stable HTTPS download location.

The website does not bypass Apple's signing or provisioning requirements. It only gates access to downloading an already-signed IPA.

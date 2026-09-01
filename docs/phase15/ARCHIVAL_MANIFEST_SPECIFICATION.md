# Alice Greenfingers — Archival Manifest Specification

The archive manifest system uses canonical deterministic serialization:
- All paths are POSIX relative (`/`).
- File entries are sorted strictly alphabetically.
- All files record exact byte size and SHA-256 cryptographic digests.
- The manifest itself is cryptographically hashed in `manifest_hash.json`.

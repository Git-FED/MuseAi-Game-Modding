# Editability

Meta-GBA is intentionally organized as plain Markdown plus patch artifacts. Documentation can be edited with any text editor and reviewed in Git. Patch binaries should be treated as immutable release artifacts: replace them only with a documented, checksummed file and a matching changelog.

The preferred change is a small patch to an existing file, not a new parallel version. Every patch release should state source version, target version, format, expected checksum, tool, test emulator, and known limitations.

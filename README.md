# Unified Tool Vault

This repository is maintained automatically by the project updater.

It stores a compact source bundle for every successfully new project, grouped by
platform/category and programming language. Each JSON bundle contains the complete
file map required to reconstruct that project.

Layout:
archive/<category>/<language>/<repository>.json

Examples:
- archive/minecraft/java/...
- archive/discord/typescript/...
- archive/roblox-studio/luau/...
- archive/blender/python/...
- archive/general-tools/rust/...

The archive contains projects produced by this generator. Third-party projects should
only be imported when their licenses explicitly allow redistribution.

To restore a bundle:
python tools/unpack_bundle.py <bundle.json> <output-directory>

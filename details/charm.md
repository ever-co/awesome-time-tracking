# Charm

[Charm](https://github.com/charmbracelet/charm) is an open-source, cross-platform set of tools and libraries designed to simplify adding backend capabilities—such as user accounts, data storage, and encryption—to terminal-based applications. It is suitable for professionals and developers who want to quickly build modern CLI applications with features like time tracking, billable hours management, and more.

## Features

- **Charm Client**: A command-line utility for accessing Charm services directly, useful for scripting, standalone use, or testing.
- **Self-Hosting**: Easily run your own Charm Cloud instance with a single executable. No storage limits by default when self-hosted.
- **Cross-Platform Support**: Available for all major platforms and architectures, including FreeBSD and ARM.
- **Charm KV (Key-Value Store)**:
  - Built on BadgerDB.
  - Cloud backup, multi-machine syncing, end-to-end encryption.
  - Embeddable in applications; can enhance existing BadgerDB implementations.
- **Charm FS (Filesystem)**:
  - Provides a virtual personal filesystem for each user on the server.
  - Implements Go's `fs.FS` interface with additional write/delete methods.
  - 1GB storage cap per account on the public Charm Cloud; unlimited when self-hosted.
- **Charm Crypt**:
  - Client-side encryption for all data sent to the server.
  - Simple methods for encrypting/decrypting user data.
  - Automated key management and account linking.
- **Charm Accounts**:
  - Authentication via SSH keys—automatic creation and linking.
  - Frictionless multi-machine access and key revocation.
- **Backups**:
  - Backup and recovery of account keys using included CLI commands.
- **TLS Support**: Server can be configured to use TLS for secure connections.
- **Docker & Systemd**: Deployment instructions and support for both.

## Pricing

- **Open Source**: Charm is MIT licensed and free to use.
- **Public Charm Cloud**: 1GB storage per account limit.
- **Self-Hosted**: No storage limits by default; admins can set their own limits.

## Tags

`cross-platform` `billable-hours` `professionals` `open-source`

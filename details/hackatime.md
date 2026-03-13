## Overview

Hackatime is a minimalist, self-hosted time tracking solution for programmers that serves as a privacy-focused alternative to WakaTime. It's compatible with all WakaTime plugins, making it easy to switch while maintaining full ownership of your coding activity data.

## Features

### Core Capabilities
- **WakaTime Compatible**: Works with all existing WakaTime editor plugins
- **Self-Hosted**: Complete control over your data and infrastructure
- **Open Source**: Fully transparent codebase (MIT license)
- **Lightweight**: Minimal resource requirements
- **Privacy-First**: Your coding data never leaves your server
- **Multi-User**: Support for multiple developers on one instance

### Tracking Features
- Automatic time tracking through IDE plugins
- Language and project detection
- File and editor tracking
- Operating system tracking
- Branch tracking (for Git repositories)
- Time zone support

### Reporting & Analytics
- Daily coding activity summaries
- Language usage statistics
- Project time breakdowns
- Weekly and monthly reports
- Export capabilities
- API access for custom integrations

### Privacy & Security
- All data stored on your own server
- No third-party data sharing
- User authentication and access control
- Optional HTTPS/TLS encryption
- Configurable data retention policies

## Supported Editors & IDEs

Through WakaTime plugin compatibility:
- Visual Studio Code
- JetBrains IDEs (IntelliJ, PyCharm, WebStorm, etc.)
- Vim/Neovim
- Emacs
- Sublime Text
- Atom
- Android Studio
- Eclipse
- Xcode
- And 50+ others

## Installation Methods

### Docker (Recommended)
```bash
docker run -d -p 3000:3000 \
  -v hackatime-data:/data \
  ghcr.io/muety/hackatime:latest
```

### Binary
- Download pre-compiled binaries for Linux, macOS, or Windows
- Run standalone executable
- Configure via environment variables or config file

### From Source
- Clone the repository
- Build with Go
- Deploy to your infrastructure

## Configuration

### Database Options
- SQLite (default, simple setup)
- PostgreSQL (recommended for multi-user)
- MySQL/MariaDB

### Authentication
- Built-in user management
- API key generation
- Optional LDAP/OAuth integration

## Use Cases

- **Individual Developers**: Personal coding time tracking with full privacy
- **Development Teams**: Team-wide time tracking on self-hosted infrastructure
- **Companies**: Enterprise time tracking meeting data sovereignty requirements
- **Students**: Learning time tracking without external services
- **Open Source Projects**: Track contributions across distributed teams

## Advantages Over WakaTime

- **No Cost**: Completely free, no premium tiers
- **Data Ownership**: Your data stays on your servers
- **Privacy**: No external company access to your code activity
- **Customization**: Modify the code to fit your needs
- **No Limits**: Unlimited users, projects, and history
- **Air-Gapped**: Can run completely offline if needed

## Limitations

- Requires self-hosting infrastructure
- Less polished UI than commercial alternatives
- Smaller feature set than WakaTime Premium
- Self-managed updates and maintenance
- Community support only (no commercial support)

## Integration

- REST API for custom integrations
- Prometheus metrics export
- Webhook support
- CSV/JSON export
- Compatible with WakaTime API format

## System Requirements

- **Minimal**:
  - 512 MB RAM
  - 1 CPU core
  - 1 GB storage
  - Linux, macOS, or Windows

- **Recommended for teams**:
  - 2 GB RAM
  - 2 CPU cores
  - 10 GB storage
  - PostgreSQL database

## Pricing

Hackatime is completely free and open source. Costs are limited to:
- Server hosting (can be as low as $5/month)
- Optional domain and SSL certificate
- Your time for setup and maintenance

## Community & Support

- GitHub repository for issues and feature requests
- Community discussions
- Documentation and setup guides
- Regular updates and bug fixes
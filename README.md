# RailsClassToPath

A Sublime Text plugin that converts Ruby/Rails class names to file paths and back.

Useful for navigating between code and the Rails project structure — create a
file from a class name or infer a class name from a path.

## Features

- Class → path  
  `Api::V1::UsersController` → `api/v1/users_controller`
- Path → Class  
  `api/v1/users_controller` → `Api::V1::UsersController`
- Absolute namespace support  
  `::Api::V1` → `/api/v1`  
  `/api/v1` → `::Api::V1`
- snake_case → CamelCase conversion
- Multiple selections support

## Usage

To assign a key binding: *Preferences* → *Package Settings* → *RailsClassToPath* → *Key Bindings*

1. Select text (Ruby class name or path)
2. Press the hotkey (default `Ctrl+K, Ctrl+H`)

The selected text is replaced with the converted value.

## Examples

| Input | Output |
|------|--------|
| Api::V1::Catalogs::OfferSerializer | api/v1/catalogs/offer_serializer |
| api/v1/catalogs/offer_serializer | Api::V1::Catalogs::OfferSerializer |
| ::Api::V1 | /api/v1 |
| /api/v1 | ::Api::V1 |

## Installation

### Via Package Control

1. Open Command Palette (`Ctrl+Shift+P`)
2. Run `Package Control: Install Package`
3. Find `RailsClassToPath`

### Manual Installation

Clone the repository into the Packages directory:

`git clone git@github.com:Zlatov/RailsClassToPath.git ~/.config/sublime-text/Packages/RailsClassToPath`

## Requirements

- Sublime Text 4
- Linux

## License

MIT

## Author

Zlatov

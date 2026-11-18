# Modern WordPress Tooling: Gutenberg, Interactivity API & Testing

Modern WordPress plugin development leverages modern JavaScript, React, the Gutenberg block editor, and standard build toolchains.

---

## 1. Modern Build Tools with `@wordpress/scripts`

The official `@wordpress/scripts` package provides zero-configuration build scripts for Webpack, Babel, PostCSS, ESLint, and Prettier.

### Setup `package.json`:
```json
{
  "name": "my-awesome-plugin",
  "version": "1.0.0",
  "scripts": {
    "start": "wp-scripts start",
    "build": "wp-scripts build",
    "format": "wp-scripts format",
    "lint:css": "wp-scripts lint-style",
    "lint:js": "wp-scripts lint-js"
  },
  "devDependencies": {
    "@wordpress/scripts": "^27.0.0"
  }
}
```

Running `npm run build` will process files in `src/` and output them to `build/`, including asset metadata files (`*.asset.php`) which automatically detect dependencies (like `wp-element`, `wp-i18n`) and hash versions.

---

## 2. Gutenberg Block Registration (`block.json`)

All modern Gutenberg blocks use the metadata standard defined in `block.json`.

### `src/block.json`:
```json
{
  "$schema": "https://schemas.wp.org/trunk/block.json",
  "apiVersion": 3,
  "name": "my-plugin/custom-card",
  "version": "1.0.0",
  "title": "Custom Card",
  "category": "widgets",
  "icon": "id-alt",
  "description": "An interactive card block.",
  "supports": {
    "html": false,
    "align": true
  },
  "textdomain": "my-awesome-plugin",
  "editorScript": "file:./index.js",
  "editorStyle": "file:./index.css",
  "style": "file:./style-index.css",
  "render": "file:./render.php"
}
```

### Registering in PHP:
```php
add_action( 'init', function() {
    register_block_type( MY_AWESOME_PLUGIN_PATH . 'build' );
} );
```

---

## 3. WordPress Interactivity API (WP 6.5+)

The Interactivity API provides a lightweight, reactive standard for building dynamic, frontend interactive features without loading heavy monolithic frontend frameworks.

### Block Markup with Directives:
```html
<div
    data-wp-interactive="myPlugin/counter"
    data-wp-context='{ "count": 0 }'
    class="counter-box"
>
    <p>Current Count: <span data-wp-text="context.count"></span></p>
    <button data-wp-on--click="actions.increment">Increment</button>
    <button data-wp-on--click="actions.decrement">Decrement</button>
</div>
```

### Store Definition (`view.js`):
```javascript
import { store } from '@wordpress/interactivity';

store( 'myPlugin/counter', {
    actions: {
        increment: ( { context } ) => {
            context.count++;
        },
        decrement: ( { context } ) => {
            if ( context.count > 0 ) {
                context.count--;
            }
        },
    },
} );
```

---

## 4. Local Development Environment with `@wordpress/env`

`wp-env` creates a Docker-powered local WordPress environment with zero configuration:

```bash
npm install @wordpress/env --save-dev
npx wp-env start
```

### `.wp-env.json`:
```json
{
  "core": "WordPress/WordPress",
  "plugins": [ "." ],
  "config": {
    "WP_DEBUG": true,
    "WP_DEBUG_LOG": true,
    "WP_DEBUG_DISPLAY": false,
    "SCRIPT_DEBUG": true
  }
}
```

---

## 5. Coding Standards & Automated Testing

### PHP_CodeSniffer (`phpcs.xml.dist`):
```xml
<?xml version="1.0"?>
<ruleset name="WordPress Plugin Standards">
    <description>Apply WordPress Coding Standards</description>
    <file>includes</file>
    <file>my-awesome-plugin.php</file>
    <exclude-pattern>vendor/*</exclude-pattern>
    <exclude-pattern>node_modules/*</exclude-pattern>
    
    <rule ref="WordPress-Extra">
        <exclude name="WordPress.Files.FileName" />
    </rule>
    <rule ref="WordPress.Security.ValidatedSanitizedInput" />
    <rule ref="WordPress.Security.EscapeOutput" />
</ruleset>
```

Run checks:
```bash
./vendor/bin/phpcs
```

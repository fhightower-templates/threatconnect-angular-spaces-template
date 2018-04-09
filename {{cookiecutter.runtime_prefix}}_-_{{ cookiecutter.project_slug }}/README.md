# {{ cookiecutter.application_name }}

{{ cookiecutter.description }}

## Build App For Release

```
npm install
grunt buildProd
```

This will package the app as `target/{{cookiecutter.runtime_prefix}}_-_{{ cookiecutter.project_slug }}.tcx`.

## Build App in Development Mode (does not minify or uglify code, so it can be debugged in browser)

```
npm install
grunt buildDev
```

## Deploy
In the ThreatConnect UI install the App (the `.tcx` file) created in the [Build App for Release](#build-app-for-release) section.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and [Floyd Hightower's Spaces App Template](https://github.com/fhightower-templates/threatconnect-spaces-template).

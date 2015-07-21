Provides some tags and templates to design templates fastly combining Django and Semantic UI.

# Semantic UI Assets
You have to install the Semantic UI assets on your own (using either Gulp or Bower).

# Installation
Just add `semantic_ui` to your `INSTALLED_APPS`.

# Usage
Have a look at the `semantic_ui` template tags library.
Component supported for now are:

* Header
* Button
* Icon
* Form (through `include` template tag)

## Form

Simply use:

    {% include 'semantic-ui/form_popin.html' with button=_('Create') title=_('Create a new project') %}

Or if you want to customize the container:

    {% include 'semantic-ui/form.html' %}

# Release Notes Guidelines

A developer writing release notes needs to describe the change in terms of the enhanced experience to the end-user.


## Tenant Release Notes

It is a Developer Studio **requirement** for all tenants to document onboarding and ongoing changes to the content. This document describes:

  * github structure for release notes
  * location of release notes in document tree
  * release notes sections


**GitHub structure** for release notes is *tenant-name/docs/release-notes/year/month.md*. 
Developer Studio began mandating the specific location in order to make it uniform across all tenants and to index release notes in the future.

    developer-studio-support/docs/release-notes/2022/april.md
  

**The left navigation** structure for tenant documents is defined by *tenant-name/config/document-explorer-definition.yaml* file.

    developer-studio-support/config/document-explorer-definition.yaml


The requirement is to have Release notes section at the top tier of the document tree.

    - sections:
      - title: Getting Started
        link: docs/getting-started.md

    - sections:
      - title: Release notes
        sections:
        - title: May 2022
          link: docs/release-notes/2022/may.md


When creating release notes please include the following information:

  * Title of the document, the header (H1), is always *Release Notes*
  * Publication date, in format: Month date, year
  * Version of openAPI document, in header H3
  * Recommended sections, in H2
  
  **Release notes sections** are described in [release notes template](./release-notes-template.md).

  - *What's new*, in terms of additions to the documentation and endpoints.
  - *Enhancements*, are changes to the existng documentation and endpoints.
  - *Fixed*, is a list of mishaps that were patched or corrected with a work-arround.
  - *Know Issues*, is a list of persistent issue(s) that's known and not fixed.
  - *Deprecated*, is a document, an endpoint, or a payload field, regarded as obsolete and best avoided.

It is a requirement to have published release notes in order for a Tenant to be promoted to higher environments: 

  * QA
  * Stage
  * Production


Any changes to the content after the initial release should go into release notes. 
The addition to release notes files should be reflected in the doc tree.

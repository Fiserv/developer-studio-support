## Tabset

To add tabset to the document

    tabs: [title one, title two]
    
    tab: start
    
         tab content goes here
         
    tab:
    
         next tab content goes here
         
    tabs: end
    
    
Here is the example:

{tabs: [title one, title two]}

{tab: one}

[{(Card)(Content of tab one)(?path=docs/about-developer-studio.md)}]

{tab:}

content of tab two

{tabs: end}


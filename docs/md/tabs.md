## Tabsets

To add tabset to the document

    {tabs: [tab title, tab title]}
    
    {tab: start}
    
         tab content goes here
         
    {tab:}
    
         next tab content goes here
         
    {tabs: end}
    
    
Here is the example:

{tabs: [First tab, Second tab]}

{tab: one}

[{(Card)(Content of tab one)(?path=docs/about-developer-studio.md)}]

{tab:}

content of tab two

{tabs: end}


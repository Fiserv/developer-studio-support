## Tabsets

<!--
type: tab
titles: First Tab, Second Tab
-->

tab content

<!--
type: tab
-->

second tab content

<!-- type: tab-end -->

### To add tabset to the document

    {tabs: [tab title, tab title]}
    
    {tab: start}
    
      tab content goes here
         
    {tab:}
    
      next tab content goes here
         
    {tabs: end}
    
    
    
    
### Tabset example

{tabs: [First tab, Second tab]}

{tab: one}

[{(Card)(Content of tab one)(?path=docs/about-developer-studio.md)}]

{tab:}

content of tab two

{tabs: end}




### Another tabset example

{tabs: [Cards, Description]}

{tabs: one}

[{(Card One)(Card with a link)(?path=docs/about-developer-studio.md)},{(Card Two)(Card without a link)}]

{tab:}

content of tab two

{tabs: end}


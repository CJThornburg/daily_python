# Fruit Vizuilization

  ## Simple Vizulization with dash pandas and plotly


 - Imports
  ```
  import dash
  from dash import dcc, html
  from dash.dependencies import Input, Output
  import pandas as pd
  import plotly.express as px
  ```





 - dash
    - [Main](https://pypi.org/project/dash/)
    - [Components](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa2lsVEJmQW1XWmhWVjNhTkl3a0hndTFQalNId3xBQ3Jtc0trdFZpbVc5ajlwUE43eDMzYVdMZ3RJclBGbHBkSlNCc1RCNGNVN25mVTc1M293Uy1vSVVhVEVmQTAyb2pCRmQ0cXpoeVhOTjJsenJUY3pyOW9kSGp6LXo0QldYVUdKaTYzc1p5d0RYY0lzVlI5UmYtbw&q=https%3A%2F%2Fdash.plotly.com%2Fdash-core-components&v=hSPmj7mK6ng)
    - [Plotly](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazFIeGppTzVvUnVkX0RXY0IydUVDMUgxdFRmUXxBQ3Jtc0tsN2hlZzhHYVNSMk9vVVJzRUVwZzdmU0ZpUEpIWGRjY3RDQTlyR3RuRzl5NktqYWZnS3p6dVlwbE1TLVM3Q1IyNXpIa1N0eFUtZmtCa2ZVdERzcWhTUGhMeThxRnFJeExxY1dmaXVtTnA4S3NRY3hJWQ&q=https%3A%2F%2Fplotly.com%2Fpython%2F&v=hSPmj7mK6ng)
    - [Callback](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmpBdFB0S3I5a2N0ZGREaUpicTh0LWp4YU5PZ3xBQ3Jtc0trMGQ0RjN6RDZ5OVpBVnkzd3VhNW92NC00NG5VTEtOQTJfVGZBUmw4UUtDMkxJVDQ0ZmV6LXBNYlFOZXRzYlA3MUZwLUY5c3NUUF95T21aWGJqa0E3Y2M4Y1RNNnl0cm5pSEpLTUpOWV81NWFqYmluVQ&q=https%3A%2F%2Fdash.plotly.com%2Fbasic-callbacks&v=hSPmj7mK6ng)
      - is the thing connecting the components to the plots/graphs
      - outside of app layout
        - while plot and components are in the layout def

    - [plotly_barChar_exampl](https://plotly.com/python/bar-charts/)
      - [plotly_expreess_bar_char_docs](https://plotly.com/python-api-reference/generated/plotly.express.bar.html#plotly.express.bar)
    - [yt_video](https://www.youtube.com/watch?v=hSPmj7mK6ng&t=631s)

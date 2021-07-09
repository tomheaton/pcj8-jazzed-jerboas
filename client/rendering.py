from rich.text import Text

logo_text = Text.assemble(("""$$$$$$$$\ $$\                 
\__$$  __|$$ |                
   $$ |   $$$$$$$\   $$$$$$\  
   $$ |   $$  __$$\  \____$$\ 
   $$ |   $$ |  $$ | $$$$$$$ |
   $$ |   $$ |  $$ |$$  __$$ |
   $$ |   $$ |  $$ |\$$$$$$$ |
   \__|   \__|  \__| \_______|\n""", "bold magenta"), ("""$$$$$$$\                      
$$  __$$\                     
$$ |  $$ | $$$$$$\  $$\   $$\ 
$$$$$$$\ |$$  __$$\ \$$\ $$  |
$$  __$$\ $$ /  $$ | \$$$$  / 
$$ |  $$ |$$ |  $$ | $$  $$<  
$$$$$$$  |\$$$$$$  |$$  /\$$\ 
\_______/  \______/ \__/  \__|""", "bold cyan"))


def render_box(rows: list):
    """:rows: A list of strings that together make a box.
    There must be at least 16 rows/items in :rows:.
    Returns a Text-object which can be printed with console.print()
    Overall, this function gets the Text-object that is shown to the user once in a session."""
    logo_rows = logo_text.split("\n")
    rows = ["  "+x for x in rows]

    if len(rows) < 16:
        raise ValueError("The argument rows needs to contain at least 16 rows.")
    if len(rows) > 16:
        dummy_rows_to_add = len(rows) - len(logo_rows)
        dummy_rows = [Text.assemble(("-"*30, "red")) for i in range(dummy_rows_to_add)]
        for i in range(dummy_rows_to_add):
            logo_rows.append(dummy_rows[i])
        print(logo_rows)    

    new_rows = []
    for i in range(0, len(rows)):
        new_rows.append(Text.assemble(logo_rows[i], rows[i]+"\n"))
    return Text.assemble(*new_rows)




import os

ascii_art = """           .                               .                                .          .            
 .             .                                    . .                 . .       .                 
        ..   .                 .                        .                                .          
        .      .                     .      ..                 .  .        .          .             
          .                                   .    .          .           .   .             .   .   
      .     .                     .       .    .          .        .       .                        
                .  ..         .             .               .              . .          .    .      
                          .   .          .:#@#    .       .          .                              
             .         .        .     :@@@@@%@@@@@@@@@@@@@@*@@   .  .  .                 ..         
  .                                @@@@@@@#%@@@@@@@@%@%%#%@%= -@     .  . .                  . .    
 .                   .   .        +@@%#*++**#####%%%#+=+=+*%@@@+@                                   
    .           .        .       .@@#**##%##*##*#*#*#@@#@###**#@@+       .              .           
           .   .                :@@*++#%*+#%#*+++###*####+*#*##*%@@      .         . .    .     .   
               .    .    .     @@@###%++***+##*+#%#%#**%##@**+#%%@@@          .       .             
..    .                  .    @@@##*##*%+*+*+*+*@@%@*=@%+=*%##*=**@@@      .                 .      
 .   .        .              .%@##*##+**####%#%%#***+*++#*+%%*###*+%@       .    .  .               
         .       .           :-@#*#%#*#%%##%%###%***+#@*+##%#*####%#@@    .   .    .   .        .   
           .   .   .           @%#####*#*%@%#####++*+-+@+*#@+*%%####@@          .                   
         ..       .  .         @@###*%##+=::-::::.:::..#-::@=+#%%%##@@   .  .     .                 
             .                 =@%%+****%@%%#=:..::::::-#++%#+*@*#%@@  .    .   ..                  
                                @@+:=###*+*%@@@@%*+#@@@@@@%#*%%*+%@@   .               .            
                  .     .       =@= ++=+++++*#%@@@@@@#*+-:::-=- .#@@                      .         
         .            .    .  .  @=-@@@@@@%+%@##+. +**@@@@@@@@@%.@@         .             .  .   .  
                         .      -@.-:.:+*#%#=--=+-:+-:..=++=-..-.++@         .  .    ..       .     
                     . .     .   @ +=-: .....*#+:  -=*+.     .-=:-%@          . .    .  .           
    .. .      .      .     .   . @.#++=::.--=. .....  .@#-...:=-=+@=      .          .           .  
             . .     .        .  @:*======**@@@@@@@@@@@=@@*+===++=@                 .      .  .     
    .      . .         ..        %+++*#**#*:.:....:    ..#@%#**++*@           ..        .    .      
              .      .           @@#####*-==..=*%@@@@@#-::+=+***%*#        .                        
 . .          .                    #@*++=+%@@@@*= ...:*@@@+==++#@       .                           
                 .                  @@*++=:..:-==+*#%#+:..====*@=      .               .            
         .          .  .             @%****==+*%@@@@*+----+++*@=        .      .             .      
                                 .   .@#%#***+=-::...:=+*++****                 . .       .         
   .    .            .       .    .   %.-*#**+=--------=+**+.=@    .    .  .         .     ..       
                       .              %*=:-+++*##*****++=-:-##@       ..      .       .  .          
 .     .                             @@#%@#===++******+=+*@%*+@=.      .           .                
       .     .     .        .      :*@@*+##%%#*+*+++**#%%%#+-+@..=       .   .                      
          .                       .*  @@**##*####%@%##**+=-=+@% .:-.                          .     
  .                      .  ... -**=.  @@*+**#*#*+*++**+====@%  ..::-..             .   .     .     
               .          .:=+++=-::..  @@%++****#%##+==++=%@  .....::.:::..      .   .     .       
 .             .     ..:--:..  =:==:..   .@%++++++=+=+++==%@.        .:. ........              .    
            .    .::--..--::-:-= ==-:.    .@@%******++++*@@   @@@@*    :::.::::::.....        .   . 
   .        ..:=:. .::-  .... .: --=--   --  .++**##***#%    @@.@@@@@@   :.:.:::::::::::.         . 
          .=-...:=-  ::-: ::=.-- --:  .@@@@@@=:  --==+.  #@*.@ #@@ =+%@@  ::.......:..:::-          
        .=.=: .: .-= ..::::.-.:: .:  +@+++==+%@@@*.+.=@@@*. @@=@@  -=+*@%   ...:: .:.....:=.      . 
   .   :+:.-*. .:. -+.  .:::::-: .  +@@ ::-==-:   :==:=-:. #@.-@@ .::==+@%+:..... :.:::..:::-       
     .-+-.-.=* ..:::-=-   ..:.::   %@*% :-...----=+*: :::  @:-@@. ...:--+#=..:::..--::...-:::+   .  
   :**-:=.--.@ ..::::-=-. ..:.:*. +@#+@. =--... . :. --:. @@@@@  ..    .::::...:..-:::: --.-:--.    
  .@ :=-= =-.% .:-..:--:- : .. #-.*@.:#= .:-::.:%    .- .=-@..@. ..:..     ..... .-.::: #-.-::-- .  
 .#+  +-+ :-:% ...::..:--....:..@+ @.@+@  .--...- .   . -@+:-@  .....:.:..:..... :-..:: +:.--:..*.  
 +*:. ==+..=-*..:. .-...-- .... .  @@@#@@ :=+- :..::.  .@=+@*. :::-:.....::..:.:.--.::: +-.-=-: + . 
 -*..- =+-.--* ::+.:::: :.+:..:.. . @%:*@  :=+ .....   @@%+-@ .....::-.:::......:=:.:::.=:.-=- :+=  
 :#. +..*:.-=* -.:...-:.:.-::--.  @@+ @  .-=::....  :@#%@@  ::..:::::::::... .---..::.=-:=+. *:+. 
 -*- += *+.-+*.:...::---:::.:::::.-  @@+@@ .:+---...  @@@@#  :::-:::.:...:.-...:=:::::..=::=. .%.== 
               .                         *     .     ..          .  .                               """

def generate_svg(mode):
    if mode == "dark":
        bg = "#1a1b26"
        topbar = "#16161e"
        terminal = "#c0caf5"
        title = "#bb9af7"
        label = "#7aa2f7"
        value = "#a9b1d6"
        stats = "#f7768e"
        ascii_color = "#9ece6a"
        divider = "#565f89"
        filename = "dark_mode.svg"
    else:
        bg = "#d5d6db"
        topbar = "#c8c9ce"
        terminal = "#343b58"
        title = "#5a4a78"
        label = "#33467c"
        value = "#565f89"
        stats = "#8c4351"
        ascii_color = "#485e30"
        divider = "#9699a3"
        filename = "light_mode.svg"

    lines = ascii_art.split('\n')
    
    svg = f"""<svg width="1250" height="650" viewBox="0 0 1250 650" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .terminal {{ font-family: 'Fira Code', 'Consolas', 'Courier New', monospace; font-size: 16px; fill: {terminal}; }}
    .ascii {{ font-size: 9.5px; fill: {ascii_color}; font-weight: bold; }}
    .title {{ fill: {title}; font-weight: bold; }}
    .label {{ fill: {label}; font-weight: bold; }}
    .value {{ fill: {value}; }}
    .stats {{ fill: {stats}; font-weight: bold; }}
    .bg {{ fill: {bg}; }}
    .topbar {{ fill: {topbar}; }}
    .divider {{ fill: {divider}; }}
  </style>

  <!-- Terminal Window Background -->
  <rect width="1250" height="650" rx="10" class="bg" />
  
  <!-- Terminal Top Bar -->
  <rect width="1250" height="30" rx="10" class="topbar" />
  <rect width="1250" height="15" y="15" class="topbar" /> 
  
  <!-- macOS Buttons -->
  <circle cx="20" cy="15" r="6" fill="#ff5f56" />
  <circle cx="40" cy="15" r="6" fill="#ffbd2e" />
  <circle cx="60" cy="15" r="6" fill="#27c93f" />
  
  <text x="625" y="20" text-anchor="middle" font-family="monospace" font-size="12" fill="{value}">ralph@chex: ~</text>

  <!-- ASCII Art Left Column -->
"""
    y_pos = 60
    for line in lines:
        svg += f'  <text x="20" y="{y_pos}" class="terminal ascii" xml:space="preserve">{line}</text>\n'
        y_pos += 10

    # Right column layout
    svg += f"""
  <!-- Text Content Right Column (Explicit Y coordinates to prevent overlap) -->
  <text x="680" y="90" class="terminal" xml:space="preserve"><tspan class="title">ralph@chex</tspan> <tspan class="divider">------------------------------------------------------</tspan></text>
  
  <text x="680" y="115" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Role:       </tspan> <tspan class="value">Co-founder @Nanoprograms, Web/Mobile/Game Dev</tspan></text>
  <text x="680" y="140" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Languages:  </tspan> <tspan class="value">JS/TS, C++, Go, Rust, PHP, HTML/CSS, SQL</tspan></text>
  <text x="680" y="165" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Frameworks: </tspan> <tspan class="value">React, Next.js, Vue, Astro, Tailwind, Shadcn</tspan></text>
  <text x="680" y="190" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Backend:    </tspan> <tspan class="value">Node.js, Express, Django</tspan></text>
  <text x="680" y="215" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Databases:  </tspan> <tspan class="value">PostgreSQL, MySQL, SQLite, MariaDB, Firebase, Supabase</tspan></text>
  <text x="680" y="240" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">AI / ML:    </tspan> <tspan class="value">NumPy, Scikit-Learn, OpenAI</tspan></text>
  <text x="680" y="265" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Mobile:     </tspan> <tspan class="value">React Native</tspan></text>
  <text x="680" y="290" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">DevOps:     </tspan> <tspan class="value">Git, VS Code, Figma, Vite, GH Actions, Cloudflare</tspan></text>

  <text x="680" y="340" class="terminal" xml:space="preserve"><tspan class="title">Contact</tspan> <tspan class="divider">---------------------------------------------------------</tspan></text>
  
  <text x="680" y="370" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Email:      </tspan> <tspan class="value">ralphmonzales665@gmail.com</tspan></text>
  <text x="680" y="395" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">LinkedIn:   </tspan> <tspan class="value">ralph-chester-candido</tspan></text>
  <text x="680" y="420" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Portfolio:  </tspan> <tspan class="value">chxyyy.vercel.app</tspan></text>

  <text x="680" y="470" class="terminal" xml:space="preserve"><tspan class="title">GitHub Stats</tspan> <tspan class="divider">----------------------------------------------------</tspan></text>
  
  <text x="680" y="500" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Repos:   </tspan> <tspan class="stats" id="repos_data">---</tspan>  <tspan class="label">| Contributed To:</tspan> <tspan class="stats" id="contributed_data">---</tspan>  <tspan class="label">| Profile Views:</tspan> <tspan class="stats" id="views_data">---</tspan></text>
  <text x="680" y="530" class="terminal" xml:space="preserve"><tspan class="divider">.</tspan> <tspan class="label">Commits: </tspan> <tspan class="stats" id="commits_data">---</tspan>  <tspan class="label">| Followers:     </tspan> <tspan class="stats" id="followers_data">---</tspan>  <tspan class="label">| Lines of Code:</tspan> <tspan class="stats" id="loc_data">---</tspan></text>
  
  <!-- Custom Colored Blocks at the bottom to mimic terminal aesthetics -->
  <g transform="translate(1000, 580)">
"""
    
    if mode == "dark":
        colors = ["#15161e", "#f7768e", "#9ece6a", "#e0af68", "#7aa2f7", "#bb9af7", "#7dcfff", "#a9b1d6"]
    else:
        colors = ["#4c566a", "#8c4351", "#485e30", "#8f5e15", "#33467c", "#5a4a78", "#0f4b6e", "#343b58"]
        
    for i, color in enumerate(colors):
        svg += f'    <rect x="{i*25}" y="0" width="25" height="15" fill="{color}"/>\n'
        
    svg += "  </g>\n</svg>"
    
    with open(f"c:\\Projects\\RALPH22222\\{filename}", 'w', encoding='utf-8') as f:
        f.write(svg)

generate_svg("dark")
generate_svg("light")
print("SVGs generated successfully!")

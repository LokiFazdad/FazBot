import random
jokes = [
    "Do I look like the riddler to you?", "I don't always tell dad jokes, but when I do, he usually laughs.",
    "Pretend I said something funny.", "No seriously tho these are just test strings.", "for testing a randomizer.", 
    "The first rule of the Alzheimer’s club is… Wait, where are we again?", "Why do you smear peanut butter on the road? To go with the traffic jam.",
    'A bear walks into a bar and says, “Give me a whiskey and … cola.” “Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”',
    "https://cdn.discordapp.com/attachments/1013453649739006003/1015034157107257424/IMG_7357.jpg", "why don't we eat clocks? Cause that would be time consuming",
    'Do you think if you played Beyoncé in the background, it would be ambeyoncé?',"I used to work at a calendar factory, but I got fired for taking a couple days off.",
    "Why couldn't the life guard save the hippie? He was too far out, man.", "Wanna hear a construction joke? I'm still working on it.","A magician was driving down the street. Then he turned into a driveway.",
    "My friend was fired from a road contruction job for theft. I didn't believe it, but when I went over to his house, all the signs were there.", "Knock knock. Who's there? GHOSTS, I would tell them."
]

jimfotos = ["https://th.bing.com/th/id/OIP.H52jxiKVoDcZYGgmE-JW2gHaJ4?pid=ImgDet&rs=1", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/646f78b0-5b21-4446-a88f-d1ee44005881/dc2nq0f-05f0e656-40b9-478c-ad18-fd792c1c6e06.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzY0NmY3OGIwLTViMjEtNDQ0Ni1hODhmLWQxZWU0NDAwNTg4MVwvZGMybnEwZi0wNWYwZTY1Ni00MGI5LTQ3OGMtYWQxOC1mZDc5MmMxYzZlMDYuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.4aLgdEjc9JhJfXCpGAy9VAj6F_in8wwQHT6lcahVvHE",
"https://66.media.tumblr.com/bb7245129540e34e484b2b6fbf64ff39/tumblr_oxs8v2Uj2m1rutl0wo5_640.jpg", "https://i.pinimg.com/originals/1f/24/0f/1f240f5316993204aff28a96d6db1152.jpg",
"https://78.media.tumblr.com/e85d50e554a4b5144c69e3cb8b84b922/tumblr_p2nwqm0Qtc1vs985po2_400.gif"]
freddyfotos = ['https://th.bing.com/th/id/OIP.9xPIWk5kvBTyw-Xq3eo9xwHaEK?pid=ImgDet&rs=1', 'https://th.bing.com/th/id/R.08430fce735c4f338983c4c015f60aad?rik=TgV0gvLbGdHi8w&pid=ImgRaw&r=0',
'https://cdn.wallpapersafari.com/31/68/gIApZk.jpg']
chicafotos = ['https://th.bing.com/th/id/R.6c90b313fa80024f3a1630d74e65dbbe?rik=M92P2dVYRkKxZA&riu=http%3a%2f%2fimages6.fanpop.com%2fimage%2fphotos%2f39400000%2f-Chica-markiplier-39424860-540-304.gif&ehk=1BOgSkKHvtEToMKkB4nc9A%2bD8rgEW8z8nxzZxCE92QY%3d&risl=&pid=ImgRaw&r=0',
'https://pm1.narvii.com/6381/3c1e7355c9f3239cc025057174efaa3ed37d923b_hq.jpg', 'https://i.pinimg.com/736x/d0/e0/76/d0e076bccd2d3982cb8a59609601b385.jpg', "https://th.bing.com/th/id/R.e102d7e861bfa1999815ae0238db0a18?rik=eZFGJi13C%2bKBUQ&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/R.350f6a2e680a22156dfa1a76c1c41bb7?rik=hsYyNBIUs2xPKQ&pid=ImgRaw&r=0","https://th.bing.com/th/id/OIP.PB20eKpdIRkDwV0KlZOrYwHaEK?pid=ImgDet&rs=1",
"https://th.bing.com/th/id/OIP.bjNWVNIvWvuy7Xgx7HFCHgHaD2?pid=ImgDet&rs=1"]
bonniefotos = ['https://64.media.tumblr.com/1c1ad706fd0730c4a17cdc89ef4adbf7/34283a666240af0d-db/s1280x1920/d65fde40edfa62c4fb62319bd90dbd6b5ae6b896.png', 'https://th.bing.com/th/id/R.4d7540d7245afcac988c9d160d2d1a06?rik=VUfXa%2b7skgza%2fg&pid=ImgRaw&r=0',
'https://th.bing.com/th/id/R.b6179ff8516dd0a7a7b3fede1c6fb6cb?rik=morrLi86os7pmg&riu=http%3a%2f%2forig03.deviantart.net%2fd587%2ff%2f2015%2f157%2f8%2f3%2fcommission_01__fnaf_bonnie_full_body_by_christian2099-d8wbd7f.png&ehk=fPzYTkFo9ETF0lbEW7Q2XDtw1qDxieuH5lxLBAMv5gY%3d&risl=&pid=ImgRaw&r=0',
"https://th.bing.com/th/id/R.465165019300e80775c7e284b0902a11?rik=wv803P6U0jjOjA&riu=http%3a%2f%2forig02.deviantart.net%2f4ebe%2ff%2f2015%2f072%2f9%2fa%2fbonnie_wallpaper_by_drgenocidesfm-d8ll9j4.png&ehk=MX84eFACmBtGF69r8s3M%2bCysC7VvCn2He%2f0QCW5Zfgg%3d&risl=&pid=ImgRaw&r=0",
"https://th.bing.com/th/id/OIP.LEliPzcgyDy8RqnyNkmwfgHaJD?pid=ImgDet&rs=1", "https://i.pinimg.com/736x/84/72/52/847252e21cd8a2705b10d9af0574df51.jpg"]
foxyfotos = ['https://th.bing.com/th/id/OIP.r55K2lZzdfwH9MjhYqDCXQHaF8?pid=ImgDet&rs=1', 'https://th.bing.com/th/id/R.6554dabf771701833cd7c23635e7b41d?rik=6r3Ba9fJO%2fDoxg&riu=http%3a%2f%2fi1.kym-cdn.com%2fphotos%2fimages%2foriginal%2f000%2f977%2f176%2f8bc.png&ehk=0hw1AEWoGx9iOcU%2b2CdZvNTNmjaB1yX5E015sHEWhvk%3d&risl=&pid=ImgRaw&r=0',
'https://th.bing.com/th/id/OIP.oGiBAOhov7k0B0vp3M_gIwHaNo?pid=ImgDet&rs=1', "https://th.bing.com/th/id/OIP.5EnQVuOmJkw4GrUkzoUAbQHaNK?pid=ImgDet&rs=1", "https://th.bing.com/th/id/OIP.aLvoRoIyt-ae2ik67ra8gQHaJ4?pid=ImgDet&rs=1",
"https://i.pinimg.com/736x/19/e3/61/19e361d7ac1571ffab08e118a946df3a.jpg"]
fnaftonfotos = ['https://th.bing.com/th/id/OIP.FMMMnE_QAme5zsurL_Br2QHaFj?pid=ImgDet&rs=1', 'https://i.pinimg.com/originals/57/bb/28/57bb28f207a81d0b88658c50b6415800.jpg', "https://th.bing.com/th/id/OIP.imbt3JfjPZEXgd6E7OsgiQHaHE?pid=ImgDet&rs=1"
, "https://th.bing.com/th/id/R.a9bf16c0f93481a0561ad8be62982518?rik=bDa31ThZ1fVeGA&pid=ImgRaw&r=0"]
lokilist = ['https://noguiltlife.com/wp-content/uploads/2021/06/loki-memes-hands.jpg.webp','https://64.media.tumblr.com/677f0601a4c42e24f92dd6211fcae0a7/5d3f243d7a956a2e-b4/s540x810/a266647790a1ad80ed867b98edf4644225ae741d.jpg', 'https://img-9gag-fun.9cache.com/photo/a41mGNd_460s.jpg',
'https://img.buzzfeed.com/buzzfeed-static/static/2021-06/24/22/tmp/2fc989c342ef/tmp-name-2-4917-1624573216-22_dblbig.jpg?resize=1200:*']

cheersmessages = [
    "Cheers! Isn’t it time we celebrated being inebriated?", "Cheers! Hydrate or die-drate!", "Cheers! To great life decisions", "Cheers! Let’s get lit!",
    "Cheers! You do you, boo!", "Cheers! Pour one out for Fredward Fazbender.", "Cheers! *Make good choices.*", "Cheers! I'll drink to that!", "Cheers! No, no you definitely won't regret this in the morning!",
    "Cheers! Maybe have one for me?"
]


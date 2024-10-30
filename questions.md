# Questions

## Links:

Personal Website: https://aneeshmaganti.com
GitHub: https://github.com/aminoa
Linkedin: https://www.linkedin.com/in/aneesh-maganti/
Blog (new): https://stalereference.com

## Code CracklePop

Attached here: https://github.com/aminoa/rc-app/blob/main/cracklepop.py

## Please link to a program you've written from scratch

I looked through most of my projects and I realized it's been a while since I've written a totally framework-free program (also distinguishing between a library and framework is hard). Regardless, I wrote a Python script that provides a workout analysis based on the exercises I have logged within Hevy (a workout app). It's attached here: https://github.com/aminoa/weighty/blob/master/weighty.py.

## What's the most fascinating thing you've learned this month?

Learning about emulation law has been quite fascinating. I've written a couple of simple emulators in the last couple of years and have played with them for even longer, but more recently, after Nintendo took down Ryujinx (a Switch emulator) last month, I felt compelled to research more into the legal side and write a blog post (https://stalereference.com/posts/switch-emulation/).

To refresh, emulation is hardware simulation done via software. Copyright protects creative works, not functional ideas. For example, the concept of a toothbrush is functional but an Aneesh-branded toothbrush (with an in-vogue design) is copyrightable. Similarly, the PlayStation architecture is functional, whereas Sony's product is creative. Sony sued multiple emulator developers on potentially related copyright infringement but the courts ruled in favor of the developers twice.

However, the DMCA complicates this: circumvention of technological protection measures (encryption) is now illegal but there is a (mostly untested) exemption to permit reverse engineering to create an interoperable program. Earlier this year, Nintendo sued Yuzu (another Switch emulator) and argued that it broke the DMCA by breaking game encryption (Yuzu soon settled). It's unclear how a court would rule in a future hypothetical lawsuit between Nintendo/(insert game/tech company) and an emulation team, I hope they rely on the intention of the copyright rulings to foster competition and aid in preservation.

## What do you want to be doing in two years?

Starting with a couple deeper goals:

Work at a company/organization that has a mission statement I feel passionate about:
- I want to have a positive impact on others and communities I'm a part of. I would look to (but not limited to) places such as the Raspberry Pi Foundation (making computers accessible), the Internet Archive (preserving the web), the Electronic Frontier Foundation (protecting our digital rights/privacy) or Khan Academy (free online learning platform) as examples.
- Examples include:

Solving technically challenging and interesting problems within a smart team
- At NYU, the most memorable class I took was Algorithmic Machine Learning - I worked in a study group on the problem sets and it was intellectually stimulating (and a little tiring) to develop proofs for the problems our professor gave us. I felt energized because the answer was not obvious but working through the problems with the other students pushed me to be creative in my thinking and develop a deep understanding of the material. 

Here are some potential paths I would like to take:
  - Go into a Masters/PhD program and join a research group that focuses on low-level hardware optimization for ML models
  - Working at Red Hat Linux with other kernel engineers for performance optimization
  - Working at the Strong Museum of Play to develop software that provides remote video game access for researchers using emulation software
  - Working on a Duolingo ML team to develop their LLMs to make practice conversations natural for users

## Why do you want to attend RC? How would attending RC be different than working on your own?

I've enjoyed working on projects on my own, but I always found myself yearning to 1) bring others to work on collaborative projects and 2) bring myself to environments where I could push myself on these projects. 

For 1) I started BUGS (https://bugsnyu.com), the open source club at NYU, to bring people together to work on cool open source projects (the BUGS website, the NYU CS Wiki, and NYU Syllabi are three examples); the club evolved into helping teach the NYU CS community through workshops and speaker events.

For 2), I always pushed myself to be in collaborative academic environments. I spent a large amount of time at the OSIRIS lab, NYU's cybersecurity research lab in Brooklyn, to be with other motivated CS/cyber students. The environment was conducive to learn from my peers (CTFs, containerization knowledge, reverse engineering, etc), stay motivated to work on projects, and push myself to learn/create cooler things (I wrote 2 CTF challenges for NYU CSAW).

I find that the Recurse Center provides the same type of dedicated environment found in OSIRIS that would push me while having a project focus from BUGS. I would like to see new faces, ideas, and concepts to make me feel inspired! It humbles me but also boosts my excitement about what I work on, what others work on, and the field as a whole.

## What would you like to work on at RC?

It's hard to know the direction I would go in RC, especially since I believe in the idea of catching the waves (ideas) when they come by. The listed projects I chose are difficult and lack a straightforward implementation path; I find that the RC environment will keep me more motivated to wade through the unclear challenges.

Develop baseband emulation as part of researching a low-level iPhone 2G emulator
- Emulation is necessary for software preservation so I want to tackle this, even though this is a grand project
- Based on de Vos' iPod Touch emulation work, I'll research the baseband (cellular) component and write and incorporate a C++ reimplementation

De-QEMUize existing iPod touch emulator
- Related to the above item, I want to insert an existing ARM dynamic recompiler to improve performance (this would require a significant rewrite)

Rewrite my Game Boy emulator (in Rust 🦀)
- I wrote dot-matrix last summer but a) I didn't finish the graphics and b) I dare myself to attempt APU (audio) emulation. 
- I also wanted to use this opportunity to improve my Rust skills.

Write a Git re-implementation 
- Following the "Write Yourself a Git" guide (also using Rust)

Contribute to Dolphin Emulator an "FPS" matrix interpolation mode (allows doubling framerates in GameCube/Wii games)
- Using Dolphin's fast forward and monitoring the draw calls, interpolate all vertices between the current and next frame to create a buffer frame

## Do you plan to attend RC in-person, remotely, or some combination of the two? How will this affect your working style?

I plan on attending primarily in-person (which I find is much more collaborative than online).

# Background

## Describe your programming background in a few sentences.

I initially got into programming by making games in Scratch and doing some online JavaScript courses back in 8th grade and continued with some classes in high school. I got more into it while studying CS at NYU and doing research (in theoretical ML and later hardware). My personal projects have tended towards systems programming (C++) and web development (Next.js apps).

## Have you worked professionally as a programmer?

I interned at Qualcomm over the summer as a SWE intern within the AI/ML organization. I worked for some smaller startups before that.

## Do you have a Computer Science degree or are you seeking one?

I have completed my BS in CS at NYU on September 22nd, 2024.

## What other commitments (work, life, family) would you have during your batch?

I will have few commitments during this batch and they shouldn't interfere during the core hours at Recurse Center.

## How did you first hear about RC?

I originally mentioned it to a friend (Sachin Iyer) about a year ago and to a couple more friends in the months between but I'm not sure where I heard about it beforehand.

## How long ago did you first hear about RC?

1 year ago

## What convinced you to apply today?

[x] Other

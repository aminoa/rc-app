# Questions

## Links:

Personal Website: https://aneeshmaganti.com
GitHub: https://github.com/aminoa
Linkedin: https://www.linkedin.com/in/aneesh-maganti/

## Code CracklePop

Attached here: https://github.com/aminoa/rc-app/blob/main/cracklepop.py

## Please link to a program you've written from scratch

I looked through most of my projects and I realized it's been a while since I've written a totally framework-free program (also distinguishing betweena a library and framework is hard). Regardless, I wrote a Python script that provides a workout analysis based on the exercises I have logged within Hevy (a workout app). It's attached here: https://github.com/aminoa/weighty/blob/master/weighty.py.

## What's the most fascinating thing you've learned this month?

I would say learning about emulation law has been quite fascinating (especially how copyright law, fair use, the DMCA, and its reverse engineering exemption come into play). I've written a couple simple emulators in the last couple of years and have played with them for even more, but more recently, after Nintendo took down Ryujinx (a Switch emulator) last month, I felt compelled to research more into the legal side and write a blog post. (I'm also generally inclined to having a holistic understanding of anything I spend a lot of time with).

There is a lot to say on the topic but I'll try to be brief. To refresh ourselves, emulation is hardware simulation done via software. Copyright law generally protects creative works, not functional ideas. So for example, the concept of a toothbrush is functional. However, the Aneesh-branded toothbrush (with a very in-vogue design) is copyrightable. Similarly, the concept/system of the PlayStation 1 is functional, whereas Sony's product is creative. Even when Sony sued on potentially related copyright infringement of copying the Sony BIOS (boot) file in the process of an emulator, the courts ruled in favor of Connectix that it was fair use for reverse engineering (or getting access to the functional elements).

The Digital Millennium Copyright Act (1998) complicates this, specifically section 1201. Now circumvention of technological protection measures (encryption) is illegal (and all modern consoles use encryption in some form) but there is an exemption to permit reverse engineering for the sake of creating an interoperable program. Note this is all mostly untested. Earlier this year, Nintendo sued Yuzu (another Switch emulator) and argued that it broke the DMCA by breaking game encryption (Yuzu soon settled). It's unclear how a court would rule in a future hypothetical lawsuit between Nintendo/(insert game/tech company) and an emulation team; I certainly hope the courts would use current precedent to guide their decision. I wrote more in my post here (https://stalereference.com/posts/switch-emulation/) and you can see the reactions to it here (https://www.reddit.com/r/emulation/comments/1g8yf9b/nintendo_is_killing_switch_emulation_via_murky/).

## What do you want to be doing in two years?

Honestly, I'm not sure in terms of the work itself. Originally, I was going to write off potential career paths (working on open source emulation/getting back into theoretical ML from my previous NYU research) but it's hard to gauge where I'll end up in a couple of years, especially since I'm biased towards viewing things from a present point of view. Here's what I'd hope right now.

- Work at a company/organization that has a mission statement I feel passionate about.
  - This is slightly vague, but I'd want to have a positive impact on others and communities I'm a part of; I would look organizations (these happen to be charities/non-for-profits but I wouldn't restrict myself) such as the Raspberry Pi Foundation (making computers cheaper/accessible), the Internet Archive (preserving the web/digital media), the Electronic Frontier Foundation (protecting our digital rights/privacy) or Khan Academy (making a free online learning platform to improve education accessibility) as examples.

- Solving technically challenging and interesting problems within a smart team
  - To explain, at NYU, the most memorable class I took was Algorithmic Machine Learning - I worked in a study group on the problem sets and it was a lot of fun (and tiring too) to develop proofs for the 4 problems our professor gave us. I felt energized because the answer was not obvious but being able to work through the problems with the other masters/PhD was intellectually stimulating. I want to work in an environment that gives me this feeling again.

## Why do you want to attend RC? How would attending RC be different than working on your own?

I've enjoyed working on programming projects on my own, but I always found myself yearning to bring others to work on collaborative projects and bring myself to environments where I could push myself on these projects. For the first part, I initially started BUGS (https://bugsnyu.com), the open source club at NYU, based on the idea of bringing people together to work on open source projects to benefit the NYU community (the BUGS website, the NYU CS Wiki, and NYU Syllabi are three examples); the club would evolve into helping teach the NYU CS community through workshops (such as Git, web development, web automation, etc.) and speaker events (developers who worked in open source within JP Morgan, Amazon, HRT, etc). 

For the second part, I always pushed myself to be in collaborative academic environments. I spent a large amount of time at the OSIRIS lab, NYU's cybersecurity lab in Brooklyn, to be with other motivated CS/cyber students. The environment was conducive to 

- 1) Learn from my peers 
  - CTFs, containerization knowledge, reverse engineering, etc.
- 2) Remain motivated to work on projects
- 3) push myself to learn/create cooler things.
  - I crafted 2 CSAW (NYU Cybersecurity CTF competition) CTF challenges (one involved reverse engineering a PlayStation 3 controller test program).

I find that the Recurse Center provides the same type of dedicated environment that would push me much further than I would ever go on my own - it reminds of OSIRIS but instead purely dedicated to personal projects, in a way combining my excitement for BUGS. I would like to seeing new faces, ideas, and concepts to make me feel inspired and jealous! It humbles me but also boosts my excitement about what I work on, what others work on, and the field as a whole.

## What would you like to work on at RC?

It's hard to exactly know which direction I would go in Recurse Center, especially since I believe in the idea of catching the waves (ideas) when they come by rather than forcing myself to follow a checklist. With that being said, that doesn't mean I don't have a checklist of stuff that I would like to work on!

- Developing open source low-level iPhone 2G emulation
  - I briefly worked on this as a research project under Professor Brendan Dolan Gavitt but I wasn't able to commit as much as I wanted; the iPhone is the most important computing device of the 21st century so being able to access these apps and games in an preserved and accessible manner is important.
  - I expect this project to be what I focus on
  - (There is touchHLE but I'm looking to make something more lower level, something in line with Martijn de Vos' research: https://devos50.github.io/blog/2022/ipod-touch-qemu/)
  - My dream is to create the 'Dolphin Emulator' for iPhone emulation - a highly performant, accurate and user-friendly emulation platform that allows users to relieve their memories with the original hardware.
- Rewrite my Game Boy emulator in Rust 🦀
  - I wrote dot-matrix (https://github.com/aminoa/dot-matrix) last summer but a) I didn't finish the graphics/control side and b) I dare myself to attempt APU emulation. I also wanted to use this opportunity to improve my Rust skills.
- Write a Git re-implementation (following this guide: https://wyag.thb.lt/).
  - I like to 'de-abstract' tools and while most of the time I don't bother since I would rather spend my time on something novel, Git is just within the realm of simplicity where it would cool to do to get a better understanding of how it works under the hood.
- Developing "Feature", a story about a caterpillar with Tux the Penguin who goes on a journey to discover open source
  - Ok, this one probably caught you off guard. There is a mascot of BUGS named "Feature" (it's not a bug, it's a feature!): https://bugsnyu.com/images/logo/feature.png. While every organization should have some mission statement, I felt that it was important to embody some of the values that I found really important in an accessible and engaging text. To research this, I read a number of texts discussing the FOSS movement (I would highly recommend Tozzi's book "For Fun and Profit" on the subject). I think being able to develop the storyline and show it off for feedback would be really useful and fun.
  - While some of this I can certainly do on my own, getting feedback from a variety of Software Engineers would help a lot 
- A C compiler! 
  - I feel sad that I never got to learn this while at NYU despite me really wanting to. 

## Do you plan to attend RC in-person, remotely, or some combination of the two? How will this affect your working style?

I plan on attending primarily in-person.

# Background

## Describe your programming background in a few sentences.

I initially got into programming from making games in Scratch and doing some online JavaScript courses back in 8th grade and continued with some classes in high school. I got more into it while studying CS at NYU and doing research (in theoretical ML and later hardware). My personal projects have tended towards systems programming (C++) and web development (Next.js apps).

## Have you worked professionally as a programmer?

I interned at Qualcomm over the summer as a SWE intern within the AI/ML organization. I worked for some smaller startups before that.

## Do you have a Computer Science degree or are you seeking one?

I have completed my BS in CS at NYU on September 22nd, 2024.

## What other commitments (work, life, family) would you have during your batch?

I will have few commitments during this batch and they shouldn't interfere during the core hours at Recurse Center.

## How did you first hear about RC?

Good question! I (think?) I first heard about the program when I was rebuilding the NYU CS Wiki (https://nyucswiki.com) around 1.5 years ago. I looked at the old NYU CS Wiki website from the previous iteration of the club and found the link on the website; I thought it sounded really cool but I didn't have the time to commit. I kept it in mind though and even told some friends who I thought would enjoy this.

## How long ago did you first hear about RC?

1.5 years ago.

## What convinced you to apply today?

[x] Other

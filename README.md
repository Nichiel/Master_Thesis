# Master_Thesis
The aim of this thesis was to compare selected methods for predictive explanation of image-based neural networks. Three different methods were analysed, associated with different ways of generating explanations, viz: RISE, ProtoPNet and ACE. The main objective was to investigate their effectiveness in generating comprehensible explanations for deep learning models. The neural network on which the performance of the above methods was tested was designed and learned to detect 10 classes of animals. A study on human evaluation of explanations was conducted using a specially designed an online questionnaire that was distributed to both developers (researchers, students) and users of artificial intelligence systems. It was discovered that their preference towards selecting the best methods depended on the respondents' experience in the field of artificial intelligence, as well as their need to understand how artificial intelligence systems work. The ProtoPNet method was clearly identified as generating the best explanations, and a more detailed analysis of the survey results indicated that these explanations were perceived as interpretable by humans. A study in specialised areas was proposed as a future research direction.

In this repository, I have shared the code from the repository of the ProtoPNet method
```
@article{DBLP:journals/corr/abs-1806-10574,
  author       = {Chaofan Chen and
                  Oscar Li and
                  Alina Barnett and
                  Jonathan Su and
                  Cynthia Rudin},
  title        = {This looks like that: deep learning for interpretable image recognition},
  journal      = {CoRR},
  volume       = {abs/1806.10574},
  year         = {2018},
  url          = {http://arxiv.org/abs/1806.10574},
  eprinttype    = {arXiv},
  eprint       = {1806.10574},
  timestamp    = {Mon, 13 Aug 2018 16:47:37 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-1806-10574.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```
RISE method
```
@inproceedings{Petsiuk2018rise,
  title = {RISE: Randomized Input Sampling for Explanation of Black-box Models},
  author = {Vitali Petsiuk and Abir Das and Kate Saenko},
  booktitle = {Proceedings of the British Machine Vision Conference (BMVC)},
  year = {2018}
}
```
modified ACE method
```
@inproceedings{ghorbani2019towards,
  title={Towards automatic concept-based explanations},
  author={Ghorbani, Amirata and Wexler, James and Zou, James Y and Kim, Been},
  booktitle={Advances in Neural Information Processing Systems},
  pages={9273--9282},
  year={2019}
}
```

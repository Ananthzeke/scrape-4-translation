# scrape-4-translation
- Scraped data From a multilingual website and calculated  sacrebleu and chrf scores for the Translation models.
- ```IndicTrans``` model outperforms  on the translation of indic languages compared to ```mBART```.
- Both ```mBART``` and ```IndicTrans``` has a GPU support but IndicTrans lacks documentation on managing devices.
- ```IndicTrans GPU``` setup is faster than CPU setup on colab.
- ```mBart``` supports most of the indic languages but ```IndicTrans``` only supports 11 indic languages.
- ```IndicTrans``` translation is close to the original english text.
- IndicTrans inference faster than mBART inference due to less parameters in ```IndicTrans```
- Note that ```mBART``` model has a prefix in every translated sentence and these prefixes are not unique. This can be avoided by not using HF pipelines.
## SCOREBOARD
### IndicTrans
| language   |chrf score |   sacrebleu score |
|:-----------|--------:|------------------:|
| as         | 64.2577 |           37.4161 |
| bn         | 69.0357 |           42.8951 |
| gu         | 69.0042 |           43.7284 |
| hi         | 64.891  |           38.9535 |
| kn         | 66.5642 |           39.6866 |
| ml         | 68.2518 |           42.4296 |
| mr         | 67.2003 |           41.4007 |
| or         | 67.2258 |           41.92   |
| pa         | 68.7879 |           44.2421 |
| ta         | 64.673  |           38.3515 |
| te         | 70.0073 |           44.7336 |

### mBART 600M
| language   |chrf score |   sacrebleu score |
|:-----------|--------:|------------------:|
| as         | 40.7172 |          24.9171  |
| bn         | 46.3055 |          24.1139  |
| gu         | 44.3759 |          31.2434  |
| hi         | 42.7282 |          22.7422  |
| kn         | 49.652  |          27.4945  |
| ml         | 46.0775 |          29.1512  |
| mr         | 47.0965 |          27.2033  |
| ne         | 36.8627 |          29.9359  |
| or         | 38.8597 |          19.9419  |
| pa         | 37.8295 |          26.7644  |
| sd         | 15.0092 |           7.20823 |
| ta         | 34.5202 |          22.0321  |
| te         | 42.7685 |          31.5408  |
| ur         | 32.4221 |          17.3954  |

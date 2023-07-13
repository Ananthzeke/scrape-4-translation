git clone https://github.com/AI4Bharat/indicTrans.git
cd indicTrans
# clone requirements repositories
git clone https://github.com/anoopkunchukuttan/indic_nlp_library.git
git clone https://github.com/anoopkunchukuttan/indic_nlp_resources.git
git clone https://github.com/rsennrich/subword-nmt.git
cd ..
# Install the necessary libraries
pip install sacremoses pandas mock sacrebleu tensorboardX pyarrow indic-nlp-library
pip install mosestokenizer subword-nmt
# Install fairseq from source
git clone https://github.com/pytorch/fairseq.git
cd fairseq
pip install ./
pip install xformers
cd ..
wget https://ai4b-public-nlu-nlg.objectstore.e2enetworks.net/indic2en.zip
unzip /content/drive/MyDrive/indic2en.zip
cd indicTrans
pip install datasets transformers
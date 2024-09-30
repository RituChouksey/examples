from transformers import pipeline
chat = pipeline(
    "question-answering", model="ktrapeznikov/biobert_v1.1_pubmed_squad_v2", tokenizer="google-bert/bert-base-cased"
)


chat(context = "Symptoms of COVID-19 are variable, but often include fever, cough, fatigue, breathing difficulties, and loss of smell and taste. Symptoms may begin one to fourteen days after exposure to the virus. At least a third of people who are infected do not develop noticeable symptoms.[9] Of those people who develop noticeable symptoms enough to be classed as patients, most (81%) develop mild to moderate symptoms (up to mild pneumonia), while 14% develop severe symptoms (dyspnea, hypoxia, or more than 50% lung involvement on imaging), and 5% suffer critical symptoms (respiratory failure, shock, or multiorgan dysfunction).[10] Older people are more likely to have severe symptoms. Some people continue to experience a range of effects—known as long COVID—for months after recovery, and damage to organs has been observed.[11] Multi-year studies are underway to further investigate the long-term effects of the disease.",
     question = "What are the symptoms of COVID-19 ?")

import spacy

class NamedEntityExtractor:
    def extract(self, text: str) :
        spacy_nlp  = spacy.load('en_core_web_sm')
            # parse text into spacy document
        doc = spacy_nlp(text.strip())

        # create sets to hold words
        named_entities = set()
        money_entities = set()
        organization_entities = set()
        location_entities = set()
        time_indicator_entities = set()

        for i in doc.ents:
            entry = str(i.lemma_).lower()
            text = text.replace(str(i).lower(), "")
            # Time indicator entities detection
            if i.label_ in ["TIM", "DATE"]:
                time_indicator_entities.add(entry)
            # money value entities detection
            elif i.label_ in ["MONEY"]:
                money_entities.add(entry)
            # organization entities detection
            elif i.label_ in ["ORG"]:
                organization_entities.add(entry)
            # Geographical and Geographical entities detection
            elif i.label_ in ["GPE", "GEO"]:
                location_entities.add(entry)
            # extract artifacts, events and natural phenomenon from text
            elif i.label_ in ["ART", "EVE", "NAT", "PERSON"]:
                named_entities.add(entry.title())

        print(f"named entities - {named_entities}")
        print(f"money entities - {money_entities}")
        print(f"location entities - {location_entities}")
        print(f"time indicator entities - {time_indicator_entities}")
        print(f"organization entities - {organization_entities}")



if __name__ == '__main__':
    named_entity_extractor = NamedEntityExtractor()
    text = "NERRMya 2 ENT [ YAE L YAEME E LOGO badge target sign COPYRIGHT label tag sop 09c"
    named_entity_extractor.extract(text)
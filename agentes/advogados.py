# agentes/advogados.py
from utils.brain import get_llm

class Acusacao:
    def __init__(self):
        self.llm = get_llm(temperature=0.2)
        self.perfil = "Advogado do Diabo / Ministério Público"

    def construir_tese(self, dados_detetive, contexto_legal=""):
        prompt = f"""Tu és o Advogado do Diabo no Tribunal IA Portugal. Foco em tipicidade, dolo e punição.
Factos: {dados_detetive}
Contexto legal disponível: {contexto_legal[:2000]}...
Constrói uma tese de acusação formal, citando artigos relevantes do Código Penal ou Civil."""
        return self.llm.invoke(prompt).content

class Defesa:
    def __init__(self):
        self.llm = get_llm(temperature=0.2)
        self.perfil = "Defensor Garantista"

    def construir_tese(self, dados_detetive, contexto_legal=""):
        prompt = f"""Tu és o Defensor no Tribunal IA Portugal. Foco na CRP, in dubio pro reo, atenuantes e direitos fundamentais.
Factos: {dados_detetive}
Contexto legal: {contexto_legal[:2000]}...
Constrói uma tese de defesa formal."""
        return self.llm.invoke(prompt).content

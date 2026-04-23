# agentes/juiz.py
from utils.brain import get_llm

class ColetivoJuizes:
    def __init__(self):
        self.llm = get_llm(temperature=0.4)

    def deliberar(self, analise_detetive, tese_acusacao, tese_defesa, contexto_legal=""):
        prompt = f"""Tu és o Coletivo de Juízes do Tribunal IA Portugal. Analisa com rigor o Direito Português.
Relatório Detetive: {analise_detetive}
Acusação: {tese_acusacao}
Defesa: {tese_defesa}
Contexto legal (CRP e códigos): {contexto_legal[:3000]}...

Gera as 3 Realidades Paralelas:
1. Rigorosa (mão pesada, letra da lei)
2. Garantista (in dubio pro reo, direitos fundamentais)
3. Equilibrada (equidade/pragmática)

Para cada uma: veredito formal + fundamento breve."""
        resposta = self.llm.invoke(prompt).content
        # Aqui podes parsear se quiseres, mas por agora retorna o texto rico
        return {"realidades": resposta}

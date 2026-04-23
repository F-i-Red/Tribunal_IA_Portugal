# agentes/detetive.py
class DetetiveJudicial:
    def __init__(self):
        self.nome = "Agente de Instrução"
        self.termometro_evidencia = "🔴 FRÁGIL"
        self.evidencias_encontradas = []
        self.lacunas = []

    def analisar_caso(self, relato_utilizador):
        palavras_prova = ['sms', 'mensagem', 'whatsapp', 'foto', 'video', 'testemunha', 'email', 'fatura', 'contrato', 'queixa']
        encontradas = [p for p in palavras_prova if p in relato_utilizador.lower()]
        self.evidencias_encontradas.extend(encontradas)
        self._atualizar_termometro()
        return self.gerar_interrogatorio(relato_utilizador)

    def _atualizar_termometro(self):
        num = len(self.evidencias_encontradas)
        if num == 0:
            self.termometro_evidencia = "🔴 FRÁGIL (Apenas testemunho verbal)"
        elif num <= 2:
            self.termometro_evidencia = "🟡 MODERADA"
        else:
            self.termometro_evidencia = "🟢 SÓLIDA"

    def gerar_interrogatorio(self, relato):
        perguntas = []
        lower = relato.lower()
        if not any(x in lower for x in ["data", "hora", "dia", "22-04"]):
            perguntas.append("Qual a data e hora exata do incidente? (importante para prazos de prescrição)")
        if "testemunha" not in lower:
            perguntas.append("Havia testemunhas? Quem e o que viram?")
        if "prova" not in lower and "documento" not in lower:
            perguntas.append("Existem provas documentais, fotos, mensagens ou queixa na PSP/GNR?")
        self.lacunas = perguntas
        return perguntas

    def relatorio_para_o_juiz(self):
        return {
            "agente": self.nome,
            "status": self.termometro_evidencia,
            "provas": self.evidencias_encontradas,
            "conclusao": "Pronto para debate" if not self.lacunas else "Ainda há lacunas"
        }

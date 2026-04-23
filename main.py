# main.py - Tribunal IA Portugal
# O Maestro que coordena a inteligência multi-agente

from agentes.detetive import DetetiveJudicial
from agentes.advogados import Acusacao, Defesa
from agentes.juiz import ColetivoJuizes
from agentes.escrivao import EscrivaoDireito

class TribunalMaestro:
    def __init__(self):
        self.detetive = DetetiveJudicial()
        self.acusacao = Acusacao()
        self.defesa = Defesa()
        self.juiz = ColetivoJuizes()
        self.escrivao = EscrivaoDireito()
        
        self.caso_completo = ""
        self.debate_encerrado = False

    def iniciar_sessao(self):
        print("\n🏛️  TRIBUNAL IA PORTUGAL - Versão 2.0 (Excelência)")
        print("="* 50)
        caso_inicial = input("⚖️  Descreva o caso (ou submeta o relatório factual): ")
        self.caso_completo = caso_inicial
        self.correr_fluxo()

    def correr_fluxo(self):
        # --- FASE 1: INSTRUÇÃO (LOOP DO DETETIVE) ---
        while not self.debate_encerrado:
            print("\n🔍 Detetive analisando provas...")
            lacunas = self.detetive.analisar_caso(self.caso_completo)
            
            if lacunas and len(self.caso_completo) < 500: # Limite de iteração para o protótipo
                print(f"🌡️  STATUS: {self.detetive.termometro_evidencia}")
                print("❓ O Detetive identificou lacunas:")
                for i, pergunta in enumerate(lacunas, 1):
                    print(f"   {i}. {pergunta}")
                
                resposta = input("\n📝 Resposta (ou digite 'JULGAR' para avançar): ")
                if resposta.upper() == "JULGAR":
                    self.debate_encerrado = True
                else:
                    self.caso_completo += f" [Dados Adicionais: {resposta}]"
            else:
                self.debate_encerrado = True

        # --- FASE 2: DEBATE INSTRUTÓRIO ---
        print("\n⚖️  INICIANDO DEBATE ENTRE AS PARTES...")
        relatorio_detetive = self.detetive.relatorio_para_o_juiz()
        
        tese_a = self.acusacao.construir_tese(relatorio_detetive)
        tese_d = self.defesa.construir_tese(relatorio_detetive)
        
        print(f"\n📢 ACUSAÇÃO: {tese_a[:150]}...")
        print(f"📢 DEFESA: {tese_d[:150]}...")

        # --- FASE 3: DELIBERAÇÃO E SENTENÇA ---
        print("\n🔨 O COLETIVO DE JUÍZES ESTÁ A DELIBERAR...")
        realidades = self.juiz.deliberar(relatorio_detetive, tese_a, tese_d)
        
        # --- FASE 4: REDAÇÃO E TRADUÇÃO (ESCRIVÃO) ---
        traducoes = self.escrivao.traduzir_para_cidadao(realidades)
        custas = self.escrivao.calcular_custas_estimadas()
        
        ata_final = self.escrivao.redigir_ata_final(
            self.caso_completo, realidades, traducoes, custas
        )

        print(ata_final)

if __name__ == "__main__":
    tribunal = TribunalMaestro()
    tribunal.iniciar_sessao()

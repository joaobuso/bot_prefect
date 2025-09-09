# Bot Prefect - Projeto Completo

Este projeto contém um bot automatizado usando Prefect Cloud com sistema de logs detalhado e monitoramento completo.

## Estrutura do Projeto

```
projeto_bot_prefect/
├── bot/
│   └── bot_prefect.py      # Código principal do bot
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## Funcionalidades

- ✅ **Execução automatizada** com Prefect Cloud
- 📊 **Logs detalhados** com emojis para fácil identificação
- 🔄 **Retry automático** em caso de falhas
- 📈 **Monitoramento** via portal web
- ⏰ **Agendamento** flexível
- 🛡️ **Tratamento de erros** robusto

## Como Usar

### 1. Instalação Local (Opcional)

```bash
pip install -r requirements.txt
python bot/bot_prefect.py
```

### 2. Deploy no Prefect Cloud

```bash
# Login no Prefect Cloud
uvx prefect-cloud login

# Deploy do bot
uvx prefect-cloud deploy bot/bot_prefect.py:fluxo_bot_completo \
--name "Bot Automatizado" \
--from https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

# Executar manualmente
uvx prefect-cloud run "Bot Prefect - Execução Completa/Bot Automatizado"

# Agendar execução diária às 9h
uvx prefect-cloud schedule "Bot Prefect - Execução Completa/Bot Automatizado" "0 9 * * *"
```

## Versões Disponíveis

### Versão Completa (Recomendada)
- Flow: `fluxo_bot_completo`
- Funcionalidades: Logs detalhados, retry, relatórios
- Ideal para: Produção e monitoramento avançado

### Versão Simples (Compatibilidade)
- Flow: `fluxo_bot`
- Funcionalidades: Básicas, compatível com código original
- Ideal para: Testes rápidos e migração gradual

## Monitoramento

Acesse o [Prefect Cloud](https://app.prefect.cloud/) para:

- 📊 Visualizar logs em tempo real
- 📈 Acompanhar histórico de execuções
- ⚙️ Configurar alertas e notificações
- 📅 Gerenciar agendamentos

## Personalização

Para adaptar o bot às suas necessidades:

1. **Edite a função `executar_logica_principal()`** no arquivo `bot/bot_prefect.py`
2. **Adicione suas dependências** no arquivo `requirements.txt`
3. **Configure variáveis de ambiente** se necessário
4. **Ajuste os parâmetros de retry** conforme sua aplicação

## Suporte

Para dúvidas sobre o Prefect Cloud, consulte:
- [Documentação Oficial](https://docs.prefect.io/)
- [Prefect Community](https://discourse.prefect.io/)

---

**Desenvolvido com ❤️ usando Prefect Cloud**

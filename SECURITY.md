# Política de Segurança

## Classificação

O `Python-Repo` é um portefólio técnico pessoal de Rúben Cavaco, classificado como material pré-Portus Digital, anterior à estruturação da Portus Digital. O repositório contém exercícios e projetos iniciais em Python e não deve conter informação real sensível.

## Dados Proibidos

Não devem ser adicionados ao repositório:

- credenciais, tokens, palavras-passe reais, chaves de API ou chaves privadas;
- ficheiros `.env` ou configurações com segredos;
- emails pessoais privados;
- dados pessoais reais;
- caminhos locais absolutos;
- dados laborais, operacionais ou financeiros reais;
- informação interna de entidades, clientes, equipas ou processos.

## Dados Permitidos

São permitidos apenas:

- exemplos fictícios;
- código demonstrativo;
- documentação histórica e técnica;
- referências públicas necessárias à autoria e ao contexto do portefólio.

## Projetos de Password

Os scripts em `Password Generators/` são exemplos educativos. Não devem ser apresentados como ferramentas de geração de passwords seguras para uso real sem revisão técnica adicional.

## Validações Antes de Pull Request

Antes de abrir ou atualizar um pull request, executar no mínimo:

```powershell
git status --short
git diff --check
python -m py_compile "Password Generators/password_generator.py" "Password Generators/gerador_de_password.py" "Music-Players/ROTW_Music_Player.py"
```

Também deve ser feita pesquisa por credenciais, tokens, chaves privadas, emails pessoais, caminhos locais absolutos, dados pessoais, dados financeiros e informação laboral ou operacional.

## Resposta a Exposição de Informação

Se for detetada informação sensível:

1. Parar o envio de alterações para o remoto.
2. Identificar ficheiro, linha aproximada, categoria e gravidade sem reproduzir o valor sensível.
3. Remover a informação da árvore atual quando autorizado ou quando for uma correção conservadora de privacidade.
4. Rodar ou revogar qualquer segredo real que possa ter sido exposto.
5. Avaliar separadamente se existe necessidade de resposta histórica.

Qualquer reescrita de histórico deve ser tratada como medida excecional, documentada e autorizada previamente.

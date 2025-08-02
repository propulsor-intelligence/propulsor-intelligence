# Manual Completo do Fusione

Este guia resume os passos de instalação e uso do **Fusione**, integrando o padrão de projetos do Propulsor.

## Requisitos
- Windows 10 ou superior com XAMPP instalado
- Python 3.10+
- MySQL (fornecido pelo XAMPP)

Crie um arquivo `.env` baseado em `.env.example` contendo as credenciais do banco:

```ini
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=fusione
SQL_DIR=C:\xampp\fusione\sql
```

## Instalação
1. Clone o repositório `propulsor-intelligence` e mantenha a estrutura padrão de pastas.
2. Execute `importar_banco_fusione.bat` ou o script `scripts/importar_fusione.py` para carregar os arquivos `.sql` da pasta definida em `SQL_DIR`.
3. Inicie o Apache e o MySQL pelo XAMPP. Acesse `http://localhost/fusione/` para verificar.

### Importação via Python
Opcionalmente, rode:

```bash
python scripts/importar_fusione.py
```

O script processa todos os arquivos `.sql` presentes em `SQL_DIR` e executa no banco configurado no `.env`.

## Hospedagem com Domínio
Após o ambiente local estar funcionando:
1. Aponte o DNS do seu domínio para o IP público do computador.
2. Configure o redirecionamento de portas 80/443 no roteador para a máquina que executa o XAMPP.
3. Libere as mesmas portas no firewall do Windows.

Com isso, o Fusione poderá ser acessado em `http://seu-dominio.com.br`.

## Suporte
Dúvidas ou falhas podem ser reportadas diretamente ao time Propulsor.

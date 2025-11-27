# 📝 TASKO - Gerenciador de Tarefas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)

> **Projeto acadêmico desenvolvido na Uniruy Wyden para a disciplina de Paradigmas Python.**

## 🌐 Deploy
O projeto está online e pode ser acessado através do link abaixo:
🔗 **[Acessar TASKO Online](https://sitepython1-production.up.railway.app/)**

---

## 📖 Sobre o Projeto

O **TASKO** é uma aplicação web desenvolvida em Django que permite aos usuários gerenciar suas tarefas diárias. O sistema implementa um CRUD completo (Create, Read, Update, Delete) e conta com sistema de autenticação, garantindo que cada usuário tenha acesso apenas às suas próprias tarefas.

### 🚀 Funcionalidades Principais

* **Autenticação de Usuários:** Cadastro e Login seguros utilizando o sistema nativo do Django.
* **Gerenciamento de Tarefas:**
    * Criar novas tarefas com título e descrição.
    * Marcar tarefas como "Concluídas".
    * Visualizar data de criação.
    * Excluir tarefas.
* **Privacidade:** As tarefas são vinculadas ao `id` do usuário logado (`auth_user`), garantindo privacidade dos dados.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Django
* **Banco de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Produção/Railway)
* **Frontend:** HTML5, CSS3 (Django Templates)
* **Hospedagem:** Railway

---

## 🗂️ Modelagem do Banco de Dados

O banco de dados foi estruturado relacionando a tabela de tarefas com a tabela de usuários nativa do Django.

<img width="735" height="845" alt="image" src="https://github.com/user-attachments/assets/fc1b03f4-7eb6-498d-8694-d13a01624265" />



### Estrutura da Tabela `tarefas_tarefa`:
* `id`: Identificador único.
* `titulo`: Título da tarefa.
* `descricao`: Detalhes da tarefa.
* `concluida`: Booleano (True/False) para status.
* `data_criacao`: Timestamp automático.
* `usuario_id`: Chave estrangeira ligada à tabela `auth_user`.

---

## 👥 Autores

| Aluno |
| :--- |
| **Joao Vitor Ferreira da Silva** |
| **Rodrigo Santos** |

**Instituição:** Uniruy Wyden
**Professor:** Heleno Cardoso
**Disciplina:** Paradigmas Python

---

📝 *Desenvolvido para fins acadêmicos - 2025*



import streamlit as st
from dscoder import dscoder

def apply_custom_css():
    """Aplica estilos CSS modernos e profissionais."""
    st.markdown("""
        <style>
        /* Tema moderno */
        :root {
            --primary: #7C3AED;
            --primary-light: #9f67ff;
            --secondary: #2DD4BF;
            --background: #ffffff;
            --surface: #F4F4F5;
            --error: #EF4444;
            --text: #1F2937;
            --text-light: #6B7280;
        }
        
        /* Reset e estilos globais */
        .stApp {
            background: var(--background);
        }
        
        .main .block-container {
            padding: 2rem 3rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Header moderno */
        .custom-header {
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            padding: 2.5rem;
            border-radius: 16px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        }
        
        .header-title {
            color: white;
            font-size: 2rem;
            font-weight: 700;
            margin: 0;
            text-align: center;
            letter-spacing: -0.025em;
        }
        
        .header-subtitle {
            color: rgba(255, 255, 255, 0.9);
            text-align: center;
            margin-top: 0.5rem;
            font-size: 1rem;
        }
        
        /* Sidebar elegante */
        section[data-testid="stSidebar"] {
            background-color: var(--surface);
            border-right: 1px solid #E5E7EB;
        }
        
        section[data-testid="stSidebar"] .block-container {
            padding: 2rem;
        }
        
        /* Títulos e textos */
        h1, h2, h3 {
            color: var(--text);
            font-weight: 600;
            letter-spacing: -0.025em;
        }
        
        /* Labels modernos */
        .stMarkdown p, label {
            color: var(--text-light);
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
        }
        
        /* Inputs estilizados */
        .stTextInput > div > div > input {
            background-color: white;
            border: 2px solid #E5E7EB;
            color: var(--text);
            border-radius: 8px;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            transition: all 0.2s ease;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1);
        }
        
        .stTextInput > div > div > input::placeholder {
            color: #9CA3AF;
        }
        
        /* Selectbox moderno */
        .stSelectbox > div > div {
            background-color: white;
            border: 2px solid #E5E7EB;
            color: var(--text);
            border-radius: 8px;
            padding: 0.5rem;
            font-size: 0.875rem;
        }
        
        .stSelectbox > div > div:hover {
            border-color: var(--primary-light);
        }
        
        /* Botão principal */
        .stButton > button {
            background: linear-gradient(135deg, var(--secondary), #20B2AA);
            color: white;
            border: none;
            padding: 0.875rem 2rem;
            border-radius: 8px;
            font-weight: 600;
            letter-spacing: 0.025em;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
                       0 2px 4px -2px rgba(0, 0, 0, 0.1);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
                       0 4px 6px -4px rgba(0, 0, 0, 0.1);
        }
        
        /* Área de código */
        .stCodeBlock {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
                       0 2px 4px -2px rgba(0, 0, 0, 0.1);
        }
        
        .stCodeBlock > div {
            background-color: #1E293B !important;
            padding: 1.5rem !important;
        }
        
        /* Expander moderno */
        .streamlit-expanderHeader {
            background-color: white;
            border: 2px solid #E5E7EB;
            border-radius: 8px;
            color: var(--text) !important;
            font-size: 0.875rem;
            font-weight: 500;
            padding: 0.75rem 1rem;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: var(--surface);
            border-color: var(--primary-light);
        }
        
        /* Mensagens de status */
        .stSuccess, .stError {
            background-color: white;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1),
                       0 1px 2px -1px rgb(0 0 0 / 0.1);
        }
        
        .stSuccess {
            border-left: 4px solid var(--secondary);
        }
        
        .stError {
            border-left: 4px solid var(--error);
        }
        
        /* Spinner personalizado */
        .stSpinner > div > div {
            border-color: var(--primary) transparent !important;
        }
        
        /* Checkbox moderno */
        .stCheckbox > label > div[role="checkbox"] {
            border-color: #E5E7EB;
            background-color: white;
            border-radius: 4px;
        }
        
        .stCheckbox > label > div[role="checkbox"][aria-checked="true"] {
            background-color: var(--primary) !important;
        }
        
        /* Slider moderno */
        .stSlider > div > div > div {
            background-color: #E5E7EB;
        }
        
        .stSlider > div > div > div > div {
            background-color: var(--primary);
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="DSCoder",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    apply_custom_css()
    
    # Header moderno
    st.markdown("""
        <div class="custom-header">
            <h1 class="header-title">DSCoder</h1>
            <p class="header-subtitle">Gerador de código inteligente alimentado por IA</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ Configurações")
        
        language = st.selectbox(
            "🔤 Linguagem de Programação",
            options=["python", "cpp", "r", "julia", "rcpp"],
            index=0
        )
        
        provider = st.selectbox(
            "🤖 Provider de IA",
            options=["openai", "anthropic", "deepseek", "openrouter"],
            index=3
        )
        
        model_options = {
            "openai": ["Padrão", "gpt-4", "gpt-3.5-turbo"],
            "anthropic": ["Padrão", "claude-3-5-sonnet-20241022", "claude-instant-v1"],
            "deepseek": ["Padrão", "deepseek-chat"],
            "openrouter": ["Padrão", "google/gemini-2.0-pro-exp-02-05:free", "google/gemini-1.5"]
        }
        
        model = st.selectbox(
            "📚 Modelo",
            options=model_options.get(provider, ["Padrão"]),
            index=0
        )
        
        with st.expander("🛠️ Configurações Avançadas"):
            trace = st.checkbox("📝 Exibir logs detalhados")
            timeout = st.slider(
                "⏱️ Timeout (segundos)",
                min_value=10,
                max_value=300,
                value=120,
                step=10
            )
            max_attempts = st.slider(
                "🔄 Máximo de Tentativas",
                min_value=1,
                max_value=10,
                value=5,
                step=1
            )
    
    # Área principal
    container = st.container()
    with container:
        st.markdown("### 💭 O que você quer criar?")
        prompt = st.text_input(
            "",
            placeholder="Descreva o código que você precisa...",
            key="prompt_input"
        )
        
        if st.button("✨ Gerar Código", use_container_width=True):
            if not prompt:
                st.error("Por favor, descreva o código que você precisa gerar.")
            else:
                with st.spinner("🔮 Gerando seu código..."):
                    try:
                        generated_code = dscoder(
                            description=prompt,
                            language=language,
                            expected_output=None,
                            provider=provider,
                            trace=trace,
                            timeout=timeout,
                            model=None if model == "Padrão" else model,
                            max_attempts=max_attempts
                        )
                        
                        if generated_code:
                            st.success("✨ Código gerado com sucesso!")
                            st.code(generated_code, language=language)
                        else:
                            st.error("Não foi possível gerar o código. Tente novamente.")
                    except Exception as e:
                        st.error(f"Erro durante a geração: {str(e)}")

if __name__ == "__main__":
    main()













# import streamlit as st
# from dscoder import dscoder

# def apply_custom_css():
#     """Aplica estilos CSS customizados para emular o design moderno."""
#     st.markdown("""
#         <style>
#         /* Estilos globais */
#         .stApp {
#             background: linear-gradient(to bottom right, #1e293b, #0f172a);
#         }
        
#         /* Header customizado */
#         .custom-header {
#             background-color: rgba(30, 41, 59, 0.5);
#             padding: 1.5rem;
#             border-radius: 8px;
#             margin-bottom: 2rem;
#             display: flex;
#             align-items: center;
#             gap: 1rem;
#         }
        
#         .header-title {
#             color: white;
#             font-size: 2.5rem;
#             font-weight: bold;
#             margin: 0;
#         }
        
#         /* Sidebar customizada */
#         .css-1d391kg {
#             background-color: rgba(30, 41, 59, 0.5);
#             padding: 1rem;
#             border-radius: 8px;
#         }
        
#         /* Cards */
#         .custom-card {
#             background-color: rgba(30, 41, 59, 0.5);
#             padding: 1.5rem;
#             border-radius: 8px;
#             margin-bottom: 1rem;
#             border: 1px solid rgba(255, 255, 255, 0.1);
#         }
        
#         /* Inputs */
#         .stTextInput > div > div > input {
#             background-color: rgba(51, 65, 85, 0.5);
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             color: white;
#             border-radius: 6px;
#         }
        
#         /* Selectbox */
#         .stSelectbox > div > div {
#             background-color: rgba(51, 65, 85, 0.5);
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             color: white;
#             border-radius: 6px;
#         }
        
#         /* Botão */
#         .stButton > button {
#             background-color: #2563eb;
#             color: white;
#             border: none;
#             padding: 0.5rem 2rem;
#             border-radius: 6px;
#             font-weight: 600;
#             transition: all 0.3s ease;
#         }
        
#         .stButton > button:hover {
#             background-color: #1d4ed8;
#             transform: translateY(-1px);
#         }
        
#         /* Área de código */
#         .stCodeBlock {
#             background-color: rgba(30, 41, 59, 0.8) !important;
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             border-radius: 8px;
#         }
        
#         /* Expander */
#         .streamlit-expanderHeader {
#             background-color: rgba(51, 65, 85, 0.5);
#             border: 1px solid rgba(255, 255, 255, 0.1);
#             border-radius: 6px;
#             color: white !important;
#         }
        
#         /* Checkbox */
#         .stCheckbox > label > span {
#             color: white !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)

# def main():
#     # Configura a página
#     st.set_page_config(
#         page_title="DSCoder Interface",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )
    
#     # Aplica CSS customizado
#     apply_custom_css()
    
#     # Header customizado
#     st.markdown("""
#         <div class="custom-header">
#             <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-blue-400">
#                 <path d="M16 18 22 12 16 6"></path>
#                 <path d="M8 6 2 12 8 18"></path>
#             </svg>
#             <h1 class="header-title">DSCoder</h1>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Sidebar com configurações
#     with st.sidebar:
#         st.markdown('<div class="custom-card">', unsafe_allow_html=True)
#         st.subheader("⚙️ Configurações")
        
#         # Configurações básicas
#         language = st.selectbox(
#             "Linguagem",
#             options=["python", "cpp", "r", "julia", "rcpp"],
#             index=0
#         )
        
#         provider = st.selectbox(
#             "Provider",
#             options=["openai", "anthropic", "deepseek", "openrouter"],
#             index=3
#         )
        
#         # Opções de modelo baseadas no provider
#         model_options = {
#             "openai": ["Padrão", "gpt-4", "gpt-3.5-turbo"],
#             "anthropic": ["Padrão", "claude-3-5-sonnet-20241022", "claude-instant-v1"],
#             "deepseek": ["Padrão", "deepseek-chat"],
#             "openrouter": ["Padrão", "google/gemini-2.0-pro-exp-02-05:free", "google/gemini-1.5"]
#         }
        
#         model = st.selectbox(
#             "Modelo",
#             options=model_options.get(provider, ["Padrão"]),
#             index=0
#         )
        
#         # Configurações avançadas em um expander
#         with st.expander("🔧 Configurações Avançadas"):
#             trace = st.checkbox("Exibir logs detalhados", value=False)
#             timeout = st.slider(
#                 "Timeout (segundos)",
#                 min_value=10,
#                 max_value=300,
#                 value=120,
#                 step=10
#             )
#             max_attempts = st.slider(
#                 "Máximo de Tentativas",
#                 min_value=1,
#                 max_value=10,
#                 value=5,
#                 step=1
#             )
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Área principal
#     st.markdown('<div class="custom-card">', unsafe_allow_html=True)
#     prompt = st.text_input(
#         "Digite a descrição do código a ser gerado:",
#         placeholder="Ex: Crie uma função para calcular o fatorial",
#     )
    
#     # Botão centralizado
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         generate_button = st.button("🚀 Gerar Código", use_container_width=True)
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     # Área de código gerado
#     if generate_button and prompt:
#         with st.spinner("✨ Gerando código, por favor aguarde..."):
#             try:
#                 generated_code = dscoder(
#                     description=prompt,
#                     language=language,
#                     expected_output=None,
#                     provider=provider,
#                     trace=trace,
#                     timeout=timeout,
#                     model=None if model == "Padrão" else model,
#                     max_attempts=max_attempts
#                 )
                
#                 if generated_code:
#                     st.success("✅ Código gerado com sucesso!")
#                     st.code(generated_code, language=language)
#                 else:
#                     st.error("❌ Falha na geração do código. Verifique os logs para mais detalhes.")
#             except Exception as e:
#                 st.error(f"❌ Erro durante a geração: {str(e)}")

# if __name__ == "__main__":
#     main()








# import streamlit as st
# from dscoder import dscoder  # importa a função principal de dscoder.py

# def main():
#     # Configura a página
#     st.set_page_config(page_title="DSCoder Interface", layout="wide")
    
#     st.sidebar.header("Configurações de Geração de Código")
    
#     # Grupo Básico: Linguagem, Provider e Modelo
#     with st.sidebar.expander("Básico", expanded=True):
#         language = st.selectbox(
#             "Linguagem",
#             options=["python", "cpp", "r", "julia", "rcpp"],
#             index=0
#         )
#         provider = st.selectbox(
#             "Provider",
#             options=["openai", "anthropic", "deepseek", "openrouter"],
#             index=3  # padrão: openrouter
#         )
#         # Opções de modelo para cada provider
#         model_options = {
#             "openai": ["Padrão", "gpt-4", "gpt-3.5-turbo"],
#             "anthropic": ["Padrão", "claude-3-5-sonnet-20241022", "claude-instant-v1"],
#             "deepseek": ["Padrão", "deepseek-chat"],
#             "openrouter": ["Padrão", "google/gemini-2.0-pro-exp-02-05:free", "google/gemini-1.5"]
#         }
#         model = st.selectbox(
#             "Modelo",
#             options=model_options.get(provider, ["Padrão"]),
#             index=0
#         )
    
#     # Grupo Avançado: demais controles
#     with st.sidebar.expander("Avançado", expanded=False):
#         trace = st.checkbox("Exibir logs detalhados", value=False)
#         timeout = st.number_input(
#             "Timeout (segundos)",
#             min_value=10,
#             max_value=300,
#             value=120,
#             step=10
#         )
#         max_attempts = st.number_input(
#             "Máximo de Tentativas",
#             min_value=1,
#             max_value=10,
#             value=5,
#             step=1
#         )
    
#     # Área principal: input do prompt semelhante à barra de busca do Google
#     st.title("DSCoder - Gerador de Código via AI")
#     prompt = st.text_input(
#         "Digite a descrição do código a ser gerado:",
#         placeholder="Ex: Crie uma função para calcular o fatorial"
#     )
    
#     # Botão centralizado "Gerar Código"
#     cols = st.columns([1, 2, 1])
#     with cols[1]:
#         if st.button("Gerar Código"):
#             if not prompt:
#                 st.error("Por favor, insira uma descrição para gerar o código.")
#             else:
#                 with st.spinner("Gerando código, por favor aguarde..."):
#                     generated_code = dscoder(
#                         description=prompt,
#                         language=language,
#                         expected_output=None,
#                         provider=provider,
#                         trace=trace,
#                         timeout=timeout,
#                         model=None if model == "Padrão" else model,
#                         max_attempts=max_attempts
#                     )
#                 if generated_code:
#                     st.success("Código gerado com sucesso!")
#                     st.code(generated_code, language=language)
#                 else:
#                     st.error("Falha na geração do código. Verifique os logs para mais detalhes.")

# if __name__ == "__main__":
#     main()























# import streamlit as st
# import os
# import time
# import tempfile
# import shutil
# from datetime import datetime
# from pathlib import Path
# import sys
# from io import StringIO
# import threading
# import traceback
# import queue
# import re

# # Importando o módulo dscoder
# from dscoder import dscoder, AIAgent

# # Configurações da página
# st.set_page_config(
#     page_title="DSCoder - Gerador de Código com IA",
#     page_icon="⚙️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Estilos CSS
# st.markdown("""
# <style>
#     .main-header {
#         font-size: 2.5rem;
#         color: #c33c54;
#         text-align: center;
#         margin-bottom: 1rem;
#         font-weight: bold;
#     }
#     .sub-header {
#         font-size: 1.2rem;
#         color: #555;
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .config-title {
#         font-size: 1.2rem;
#         font-weight: bold;
#         margin-bottom: 0.5rem;
#     }
#     .info-box {
#         background-color: #f0f7ff;
#         border: 1px solid #c0d8ff;
#         border-radius: 5px;
#         padding: 10px;
#         margin-bottom: 1rem;
#     }
#     .stButton > button {
#         width: 100%;
#         background-color: #ff595e;
#         color: white;
#     }
#     .stButton > button:hover {
#         background-color: #e63946;
#     }
#     .reset-button > button {
#         background-color: #6c757d;
#         color: white;
#     }
#     .reset-button > button:hover {
#         background-color: #5a6268;
#     }
#     .status-running {
#         color: #ff9f1c;
#         font-weight: bold;
#     }
#     .status-success {
#         color: #2ec4b6;
#         font-weight: bold;
#     }
#     .status-error {
#         color: #e71d36;
#         font-weight: bold;
#     }
#     .file-path {
#         font-size: 0.8rem;
#         color: #666;
#         margin-top: 0.5rem;
#     }
#     .processing-status {
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         gap: 10px;
#         margin: 15px 0;
#         padding: 10px;
#         border-radius: 5px;
#         background-color: rgba(255, 159, 28, 0.1);
#     }
#     .stSpinner > div {
#         border-top-color: #ff9f1c !important;
#     }
#     .code-highlight {
#         background-color: rgba(46, 196, 182, 0.1);
#         border-left: 4px solid #2ec4b6;
#         padding: 10px;
#         margin: 10px 0 20px 0;
#         border-radius: 0 5px 5px 0;
#         animation: flash 1.5s ease-out;
#     }
#     @keyframes flash {
#         0% {background-color: rgba(46, 196, 182, 0.3);}
#         100% {background-color: rgba(46, 196, 182, 0.1);}
#     }
# </style>
# """, unsafe_allow_html=True)

# # Variáveis de estado da sessão
# if 'terminal_output' not in st.session_state:
#     st.session_state.terminal_output = ""
# if 'generated_code' not in st.session_state:
#     st.session_state.generated_code = None
# if 'generation_status' not in st.session_state:
#     st.session_state.generation_status = "idle"
# if 'output_files' not in st.session_state:
#     st.session_state.output_files = []
# if 'current_attempt' not in st.session_state:
#     st.session_state.current_attempt = 0
# if 'saved_downloads' not in st.session_state:
#     st.session_state.saved_downloads = []
# if 'language' not in st.session_state:
#     st.session_state.language = "python"
# if 'output_queue' not in st.session_state:
#     st.session_state.output_queue = queue.Queue()
# if 'last_update_time' not in st.session_state:
#     st.session_state.last_update_time = datetime.now()
# if 'screen_updated' not in st.session_state:
#     st.session_state.screen_updated = False
# if 'last_rerun_time' not in st.session_state:
#     st.session_state.last_rerun_time = datetime.now()
# if 'force_immediate_display' not in st.session_state:
#     st.session_state.force_immediate_display = False
# if 'code_just_generated' not in st.session_state:
#     st.session_state.code_just_generated = False
# if 'processing' not in st.session_state:
#     st.session_state.processing = False
# if 'max_attempts' not in st.session_state:
#     st.session_state.max_attempts = 1  # valor padrão

# # Classes auxiliares e funções
# class StdoutRedirect:
#     def __init__(self, output_queue):
#         self.content = ""
#         self.old_stdout = sys.stdout
#         self.output_queue = output_queue
        
#     def write(self, text):
#         self.content += text
#         self.output_queue.put(("output", text))
        
#     def flush(self):
#         pass

# def extract_attempt_number(log_text):
#     match = re.search(r'\[Attempt (\d+)/\d+\]', log_text)
#     if match:
#         return int(match.group(1))
#     return 0

# def reset_interface():
#     st.session_state.terminal_output = ""
#     st.session_state.generated_code = None
#     st.session_state.generation_status = "idle"
#     st.session_state.output_files = []
#     st.session_state.current_attempt = 0
#     st.session_state.screen_updated = False
#     st.session_state.force_immediate_display = False
#     st.session_state.code_just_generated = False
#     st.session_state.processing = False

# class ThreadCommunication:
#     def __init__(self):
#         self.output_queue = queue.Queue()
#         self.result_code = None
#         self.generation_status = "running"
#         self.files_generated = []
#         self.current_attempt = 0

# def run_code_generation(description, language, provider, model, trace, timeout, max_attempts, expected_output, comm):
#     redirect = StdoutRedirect(comm.output_queue)
#     sys.stdout = redirect
    
#     try:
#         params = {
#             "description": description,
#             "language": language,
#             "provider": provider,
#             "model": model if model and model.strip() else None,
#             "trace": trace,
#             "timeout": timeout,
#             "max_attempts": max_attempts,
#             "expected_output": expected_output if expected_output and expected_output.strip() else None
#         }
        
#         if trace:
#             agent = AIAgent(provider=provider, trace=True)
#             original_log = agent.log
            
#             def custom_log(message, level="info", force=False):
#                 original_log(message, level, force)
#                 if "[Attempt " in message:
#                     attempt_num = extract_attempt_number(message)
#                     if attempt_num > 0:
#                         comm.output_queue.put(("attempt", attempt_num))
            
#             agent.log = custom_log
            
#             result = agent.generate_code(
#                 description=description,
#                 language=language,
#                 expected_output=params["expected_output"],
#                 max_attempts=max_attempts
#             )
            
#             if result:
#                 output_dir = agent.base_dir
#                 output_files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.startswith("code_success_")]
#                 comm.output_queue.put(("files", output_files))
#         else:
#             result = dscoder(**params)
            
#             if result:
#                 output_dir = Path("output")
#                 if output_dir.exists():
#                     output_files = [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.startswith("code_success_")]
#                     comm.output_queue.put(("files", output_files))
        
#         if result:
#             comm.output_queue.put(("code", result))
#             comm.output_queue.put(("status", "success"))
#         else:
#             comm.output_queue.put(("status", "error"))
            
#     except Exception as e:
#         error_msg = f"\nErro na geração de código: {str(e)}\nDetalhes: {traceback.format_exc()}\n"
#         comm.output_queue.put(("output", error_msg))
#         comm.output_queue.put(("status", "error"))
#     finally:
#         sys.stdout = redirect.old_stdout

# def process_queue_updates():
#     updated = False
#     code_generated = False
    
#     if hasattr(st.session_state, 'comm'):
#         while not st.session_state.comm.output_queue.empty():
#             try:
#                 msg_type, msg_content = st.session_state.comm.output_queue.get_nowait()
                
#                 if msg_type == "output":
#                     st.session_state.terminal_output += msg_content
#                     updated = True
#                 elif msg_type == "status":
#                     old_status = st.session_state.generation_status
#                     st.session_state.generation_status = msg_content
#                     if old_status == "running" and msg_content in ["success", "error"]:
#                         st.session_state.screen_updated = False
#                         updated = True
#                 elif msg_type == "code":
#                     st.session_state.generated_code = msg_content
#                     code_generated = True
#                     st.session_state.code_just_generated = True
#                     st.session_state.force_immediate_display = True
#                     updated = True
#                     st.session_state.processing = False
#                 elif msg_type == "files":
#                     st.session_state.output_files = msg_content
#                     for file_path in msg_content:
#                         file_name = os.path.basename(file_path)
#                         st.session_state.saved_downloads.append({
#                             "path": file_path,
#                             "name": file_name,
#                             "language": st.session_state.language,
#                             "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                         })
#                     updated = True
#                 elif msg_type == "attempt":
#                     if st.session_state.current_attempt != msg_content:
#                         st.session_state.current_attempt = msg_content
#                         updated = True
#             except queue.Empty:
#                 break
            
#         st.session_state.last_update_time = datetime.now()
    
#     return updated

# def check_if_rerun_needed():
#     current_time = datetime.now()
#     time_since_last_rerun = (current_time - st.session_state.last_rerun_time).total_seconds()
    
#     if st.session_state.force_immediate_display:
#         st.session_state.force_immediate_display = False
#         st.session_state.last_rerun_time = current_time
#         return True
    
#     if st.session_state.generation_status == "running" and time_since_last_rerun >= 0.5:
#         st.session_state.last_rerun_time = current_time
#         return True
    
#     if st.session_state.generation_status in ["success", "error"] and not st.session_state.screen_updated:
#         st.session_state.screen_updated = True
#         st.session_state.last_rerun_time = current_time
#         return True
    
#     return False

# def generate_code_with_feedback(description, language, provider, model, trace, timeout, max_attempts, expected_output):
#     st.session_state.terminal_output = ""
#     st.session_state.generated_code = None
#     st.session_state.generation_status = "running"
#     st.session_state.current_attempt = 0
#     st.session_state.output_files = []
#     st.session_state.screen_updated = False
#     st.session_state.last_rerun_time = datetime.now()
#     st.session_state.force_immediate_display = False
#     st.session_state.code_just_generated = False
#     st.session_state.processing = True

#     # Armazena o máximo de tentativas na sessão para uso no progress bar
#     st.session_state.max_attempts = max_attempts
    
#     st.session_state.comm = ThreadCommunication()
    
#     thread = threading.Thread(
#         target=run_code_generation,
#         args=(description, language, provider, model, trace, timeout, max_attempts, expected_output, st.session_state.comm)
#     )
#     thread.daemon = True
#     thread.start()

# # Interface principal

# # Sidebar
# with st.sidebar:
#     st.markdown("⚙️ **Configurações**", unsafe_allow_html=True)
    
#     # Seleção de linguagem
#     language_labels = {"python": "Python 🐍", "r": "R 📊", "cpp": "C++ ⚡", "julia": "Julia 🔬", "rcpp": "Rcpp 🔄"}
#     if 'language' not in st.session_state:
#         st.session_state.language = "python"
    
#     st.session_state.language = st.selectbox(
#         "Linguagem",
#         options=list(language_labels.keys()),
#         format_func=lambda x: language_labels[x],
#         index=list(language_labels.keys()).index(st.session_state.language),
#         help="Selecione a linguagem de programação"
#     )
    
#     st.markdown("### Provedor e Modelo", unsafe_allow_html=True)
#     provider = st.selectbox(
#         "Provedor",
#         options=["openai", "anthropic", "deepseek", "openrouter"],
#         index=2,
#         help="Selecione o provedor de IA"
#     )
    
#     default_models = {
#         "openai": "gpt-4-turbo",
#         "anthropic": "claude-3-5-sonnet-20241022",
#         "deepseek": "deepseek-chat",
#         "openrouter": "google/gemini-2.0-pro-exp-02-05:free"
#     }
    
#     model = st.text_input(
#         "Modelo específico (opcional)",
#         value=default_models.get(provider, ""),
#         help="Nome do modelo ou deixe em branco para usar o padrão"
#     )
    
#     with st.expander("Configurações Avançadas", expanded=False):
#         trace = st.checkbox("Modo trace", value=True, help="Exibir logs detalhados durante a geração")
#         timeout = st.number_input("Timeout (segundos)", min_value=30, max_value=300, value=120, help="Tempo máximo para gerar o código")
#         max_attempts = st.slider("Máximo de Tentativas", min_value=1, max_value=10, value=5, help="Número máximo de tentativas para gerar código válido")
#         expected_output = st.text_area("Saída esperada (opcional)", value="", help="Se fornecido, o código é validado contra essa saída esperada", height=100)
    
#     with st.expander("Sobre o DSCoder", expanded=False):
#         st.markdown("""
#         **DSCoder** é uma ferramenta de geração de código usando modelos de IA de última geração.  
#         - Geração de código em Python, R, C++, Julia e Rcpp  
#         - Integração com múltiplos provedores de IA  
#         - Validação automática do código gerado  
#         - Execução e teste do código  
#         """)

# # Título
# st.markdown("<h1 class='main-header'>DSCoder</h1>", unsafe_allow_html=True)
# st.markdown("<p class='sub-header'>Gerador de código inteligente com múltiplos modelos de IA</p>", unsafe_allow_html=True)

# # Área de descrição
# description = st.text_area(
#     "Descreva o código que você deseja gerar",
#     placeholder="Ex: Criar uma função em Python que implemente QuickSort...",
#     height=120
# )

# # Pequeno indicador da linguagem selecionada
# st.info(f"📌 Linguagem selecionada: {language_labels[st.session_state.language]}")

# # Botões (Gerar e Limpar)
# col1, col2 = st.columns([4, 1])
# with col1:
#     generate_btn = st.button(
#         "🚀 Gerar Código",
#         disabled=(st.session_state.generation_status == "running"),
#         help="Iniciar geração do código"
#     )
# with col2:
#     reset_btn = st.button(
#         "🔄 Limpar",
#         help="Limpar terminal e resultados",
#         key="reset_button"
#     )
#     st.markdown('<style>.reset-button button {background-color: #6c757d;}</style>', unsafe_allow_html=True)

# if generate_btn:
#     if not description.strip():
#         st.error("Por favor, insira uma descrição para o código a ser gerado.")
#     else:
#         # Armazena max_attempts na sessão para uso no progress bar
#         st.session_state.max_attempts = max_attempts
#         generate_code_with_feedback(
#             description,
#             st.session_state.language,
#             provider,
#             model,
#             trace,
#             timeout,
#             max_attempts,
#             expected_output
#         )

# if reset_btn:
#     reset_interface()

# # Processa atualizações da fila
# process_queue_updates()

# # --- SISTEMA DE LOADING ---
# if st.session_state.generation_status == "running" and st.session_state.max_attempts > 0:
#     progress_val = int((st.session_state.current_attempt / st.session_state.max_attempts) * 100)
#     st.progress(progress_val)
# # -----------------------------

# # Exibe status
# if st.session_state.generation_status == "running":
#     st.markdown(
#         f"<p class='status-running'>⏳ Gerando código... (Tentativa {st.session_state.current_attempt}/{st.session_state.max_attempts})</p>",
#         unsafe_allow_html=True
#     )
# elif st.session_state.generation_status == "success":
#     st.markdown("<p class='status-success'>✅ Código gerado com sucesso!</p>", unsafe_allow_html=True)
# elif st.session_state.generation_status == "error":
#     st.markdown("<p class='status-error'>❌ Erro na geração de código. Consulte os logs.</p>", unsafe_allow_html=True)

# # Exibe o código gerado imediatamente após a finalização
# if st.session_state.generated_code:
#     if st.session_state.code_just_generated:
#         st.markdown("<div class='code-highlight'>⚡ Novo código gerado!</div>", unsafe_allow_html=True)
#         st.session_state.code_just_generated = False

#     st.markdown("### Código Gerado")
#     st.code(st.session_state.generated_code, language=st.session_state.language)
    
#     if st.session_state.output_files:
#         st.markdown("### Arquivos Gerados")
#         for file_path in st.session_state.output_files:
#             try:
#                 with open(file_path, 'r') as f:
#                     file_content = f.read()
#                     file_name = os.path.basename(file_path)
#                     st.download_button(
#                         label=f"⬇️ Download: {file_name}",
#                         data=file_content,
#                         file_name=file_name,
#                         mime="text/plain"
#                     )
#                 st.markdown(f"<p class='file-path'>Salvo em: {file_path}</p>", unsafe_allow_html=True)
#             except Exception as e:
#                 st.error(f"Erro ao ler arquivo: {str(e)}")

# # Tabs para logs e histórico
# tab_logs, tab_previous = st.tabs(["Logs", "📚 Códigos Anteriores"])

# with tab_logs:
#     st.markdown("### Logs de Execução")
#     if st.session_state.terminal_output:
#         st.code(st.session_state.terminal_output, language="text")
#     else:
#         st.info("Nenhum log disponível no momento.")

# with tab_previous:
#     st.markdown("### Histórico de Códigos Gerados")
#     if st.session_state.saved_downloads:
#         downloads_by_language = {}
#         for download in st.session_state.saved_downloads:
#             lang = download["language"]
#             if lang not in downloads_by_language:
#                 downloads_by_language[lang] = []
#             downloads_by_language[lang].append(download)
        
#         for lang, downloads in downloads_by_language.items():
#             lang_header = st.expander(f"{language_labels.get(lang, lang)} ({len(downloads)} arquivos)", expanded=False)
#             with lang_header:
#                 for download in downloads:
#                     st.markdown(f"**{download['name']}**")
#                     st.markdown(f"Gerado em: {download['timestamp']}")
#                     try:
#                         with open(download['path'], 'r') as file:
#                             file_content = file.read()
#                             st.download_button(
#                                 label="⬇️ Download",
#                                 data=file_content,
#                                 file_name=download['name'],
#                                 mime="text/plain"
#                             )
#                             toggle_key = f"toggle_{download['name']}_{download['timestamp']}"
#                             if toggle_key not in st.session_state:
#                                 st.session_state[toggle_key] = False
#                             show_code = st.checkbox(f"Mostrar código", key=toggle_key)
#                             if show_code:
#                                 st.code(file_content, language=lang)
#                     except Exception as e:
#                         st.error(f"Erro ao ler arquivo: {str(e)}")
#                     st.markdown("---")
#     else:
#         st.info("Nenhum código gerado ainda. Use o campo acima para criar seu primeiro código.")

# # Verifica se precisa atualizar a interface
# if check_if_rerun_needed():
#     st.rerun()

# # Rodapé
# st.markdown("""
# <div style="text-align: center; margin-top: 30px; padding: 10px; border-top: 1px solid #ddd;">
#     <p style="color: #666; font-size: 0.8rem;">
#         DSCoder © 2025 | Desenvolvido para pesquisa e programação científica
#     </p>
# </div>
# """, unsafe_allow_html=True)

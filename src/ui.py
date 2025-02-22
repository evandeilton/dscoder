import streamlit as st
from dscoder import dscoder
import glob
import os
from datetime import datetime
import subprocess
import sys
import tempfile
from typing import Tuple, Optional

class CodeExecutor:
    """
    Classe responsável por executar código em diferentes linguagens de programação.
    Suporta R, Python, Julia e C++.
    """
    
    def __init__(self):
        """Inicializa o executor de código verificando as dependências necessárias."""
        self.check_dependencies()
    
    def check_dependencies(self) -> None:
        """Verifica se todas as dependências necessárias estão instaladas."""
        self.available_langs = {'python': True}
        which_cmd = 'where' if os.name == 'nt' else 'which'
        
        # Verifica R
        try:
            result = subprocess.run(['R', '--version'], capture_output=True, text=True)
            self.available_langs['r'] = True
        except FileNotFoundError:
            self.available_langs['r'] = False
            
        # Verifica Julia
        try:
            result = subprocess.run([which_cmd, 'julia'], capture_output=True, text=True)
            self.available_langs['julia'] = result.returncode == 0
        except:
            self.available_langs['julia'] = False
            
        # Verifica G++
        try:
            result = subprocess.run([which_cmd, 'g++'], capture_output=True, text=True)
            self.available_langs['cpp'] = result.returncode == 0
        except:
            self.available_langs['cpp'] = False

    def execute_code(self, code: str, language: str) -> Tuple[str, str]:
        """
        Executa o código na linguagem especificada.
        
        Args:
            code (str): Código a ser executado
            language (str): Linguagem do código (python, r, julia, cpp)
            
        Returns:
            Tuple[str, str]: (stdout, stderr) da execução
        """
        if language not in self.available_langs or not self.available_langs[language]:
            return '', f'{language.upper()} não está instalado no sistema'
            
        execute_method = getattr(self, f'execute_{language}', None)
        if execute_method:
            return execute_method(code)
        return '', f'Linguagem {language} não suportada'

    def execute_python(self, code: str) -> Tuple[str, str]:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py') as f:
            f.write(code)
            f.flush()
            process = subprocess.run([sys.executable, f.name], capture_output=True, text=True)
        return process.stdout, process.stderr

    def execute_r(self, code: str) -> Tuple[str, str]:
        if not self.available_langs.get('r', False):
            return '', 'R não está instalado no sistema'
        with tempfile.NamedTemporaryFile(mode='w', suffix='.R') as f:
            f.write(code)
            f.flush()
            process = subprocess.run(['Rscript', f.name], capture_output=True, text=True)
        return process.stdout, process.stderr

    def execute_julia(self, code: str) -> Tuple[str, str]:
        if not self.available_langs.get('julia', False):
            return '', 'Julia não está instalada no sistema'
        with tempfile.NamedTemporaryFile(mode='w', suffix='.jl') as f:
            f.write(code)
            f.flush()
            process = subprocess.run(['julia', f.name], capture_output=True, text=True)
        return process.stdout, process.stderr

    def execute_cpp(self, code: str) -> Tuple[str, str]:
        if not self.available_langs.get('cpp', False):
            return '', 'G++ não está instalado no sistema'
        
        code = code.replace('\r\n', '\n').strip()
        if not code:
            return '', 'Código vazio'
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                src_path = os.path.join(temp_dir, 'source.cpp')
                exe_path = os.path.join(temp_dir, 'program')
                if os.name == 'nt':
                    exe_path += '.exe'
                
                with open(src_path, 'w', encoding='utf-8') as src_file:
                    src_file.write(code)
                
                compile_process = subprocess.run(
                    ['g++', src_path, '-o', exe_path, '-std=c++11'],
                    capture_output=True,
                    text=True
                )
                
                if compile_process.returncode != 0:
                    return '', f'Erro de compilação:\n{compile_process.stderr}'
                
                run_process = subprocess.run(
                    [exe_path],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                return run_process.stdout, run_process.stderr
                
        except subprocess.TimeoutExpired:
            return '', 'Erro: Execução excedeu o tempo limite de 10 segundos'
        except Exception as e:
            return '', f'Erro durante execução: {str(e)}'

def get_latest_failure_code():
    """
    Busca o arquivo de código de falha mais recente.
    Retorna o conteúdo do arquivo ou None se não encontrar.
    """
    try:
        # Obtém o diretório atual
        current_dir = os.getcwd()
        st.write(f"Diretório atual: {current_dir}")
        
        # Lista todos os arquivos no diretório atual
        all_files = os.listdir(current_dir)
        st.write(f"Todos os arquivos: {all_files}")
        
        # Filtra arquivos de falha
        failure_files = [f for f in all_files if f.startswith('code_failure')]
        st.write(f"Arquivos de falha encontrados: {failure_files}")
        
        if not failure_files:
            st.info("Nenhum arquivo de fallback encontrado")
            return None
            
        # Pega o arquivo mais recente
        latest_file = max(failure_files, key=lambda x: os.path.getctime(os.path.join(current_dir, x)))
        st.write(f"Arquivo mais recente: {latest_file}")
        
        # Caminho completo do arquivo
        file_path = os.path.join(current_dir, latest_file)
        
        # Lê o conteúdo do arquivo
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                st.write(f"Conteúdo lido com sucesso (tamanho: {len(content)})")
                return content
            else:
                st.warning("Arquivo encontrado mas está vazio")
                return None
                
    except Exception as e:
        st.error(f"Erro ao ler arquivo de fallback: {str(e)}")
        import traceback
        st.write("Traceback completo:", traceback.format_exc())
        return None

def apply_custom_css():
    """Aplica estilos CSS modernos inspirados no Claude AI."""
    st.markdown("""
        <style>
        /* Tema inspirado no Claude AI */
        :root {
            --primary: #6B7280;
            --primary-light: #9CA3AF;
            --secondary: #8B5CF6;
            --background: #F9FAFB;
            --surface: #FFFFFF;
            --error: #EF4444;
            --text: #111827;
            --text-light: #4B5563;
        }
        
        /* Reset e estilos globais */
        .stApp {
            background: var(--background);
        }
        
        .main .block-container {
            padding: 2rem 3rem;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        /* Header minimalista */
        .custom-header {
            background: var(--surface);
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            border: 1px solid #E5E7EB;
        }
        
        .header-title {
            color: var(--text);
            font-size: 1.875rem;
            font-weight: 600;
            margin: 0;
            text-align: center;
            letter-spacing: -0.025em;
        }
        
        .header-subtitle {
            color: var(--text-light);
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
            padding: 1.5rem;
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
        
        /* Text area redimensionável */
        .stTextArea > div > div > textarea {
            resize: vertical;
            min-height: 150px;
            max-height: 400px;
            background-color: var(--surface) !important;
        }
        
        /* Container do textarea */
        .stTextArea > div {
            background-color: var(--surface) !important;
        }
        
        /* Inputs minimalistas */
        .stTextInput > div > div > input {
            background-color: white;
            border: 1px solid #E5E7EB;
            color: var(--text);
            border-radius: 6px;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            transition: all 0.2s ease;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: var(--secondary);
            box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.1);
        }
        
        /* Selectbox suave */
        .stSelectbox > div > div {
            background-color: white;
            border: 1px solid #E5E7EB;
            color: var(--text);
            border-radius: 6px;
            padding: 0.5rem;
            font-size: 0.875rem;
        }
        
        .stSelectbox > div > div:hover {
            border-color: var(--secondary);
        }
        
        /* Botão elegante */
        .stButton > button {
            background-color: var(--secondary);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 6px;
            font-weight: 500;
            letter-spacing: 0.025em;
            transition: all 0.2s ease;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        }
        
        .stButton > button:hover {
            background-color: #7C3AED;
            transform: translateY(-1px);
        }
        
        /* Área de código */
        .stCodeBlock {
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #E5E7EB;
        }
               
        /* Ajusta a cor do texto selecionado */
        .stCodeBlock > div::selection,
        .stCodeBlock > div *::selection {
            background-color: rgba(139, 92, 246, 0.2) !important;
            color: inherit !important;
        }
        
        /* Expander suave */
        .streamlit-expanderHeader {
            background-color: white;
            border: 1px solid #E5E7EB;
            border-radius: 6px;
            color: var(--text) !important;
            font-size: 0.875rem;
            font-weight: 500;
            padding: 0.75rem 1rem;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: #F9FAFB;
            border-color: var(--secondary);
        }
        
        /* Mensagens de status */
        .stSuccess, .stError {
            background-color: white;
            border-radius: 6px;
            padding: 1rem;
            border: 1px solid #E5E7EB;
        }
        
        .stSuccess {
            border-left: 3px solid #10B981;
        }
        
        .stError {
            border-left: 3px solid var(--error);
        }
        
        /* Spinner suave */
        .stSpinner > div > div {
            border-color: var(--secondary) transparent !important;
        }
        
        /* Checkbox moderno */
        .stCheckbox > label > div[role="checkbox"] {
            border-color: #E5E7EB;
            background-color: white;
            border-radius: 4px;
        }
        
        .stCheckbox > label > div[role="checkbox"][aria-checked="true"] {
            background-color: var(--secondary) !important;
        }
        
        /* Slider suave */
        .stSlider > div > div > div {
            background-color: #E5E7EB;
        }
        
        .stSlider > div > div > div > div {
            background-color: var(--secondary);
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
    
    # Header minimalista
    st.markdown("""
        <div class="custom-header">
            <h1 class="header-title">DSCoder</h1>
            <p class="header-subtitle">Gerador de código inteligente alimentado por IA</p>
        </div>
    """, unsafe_allow_html=True)

    # Inicializar o executor de código na sessão
    if 'executor' not in st.session_state:
        st.session_state.executor = CodeExecutor()
    
    # Tabs para geração e execução
    tab_gerar, tab_executar = st.tabs(["Gerar Código", "Executar Código"])
    
    with tab_gerar:
        # Sidebar original
        with st.sidebar:
            st.markdown("### Configurações")
            
            language = st.selectbox(
                "Linguagem de Programação",
                options=["python", "cpp", "r", "julia", "rcpp"],
                index=0
            )
            
            provider = st.selectbox(
                "Provider de IA",
                options=["openai", "anthropic", "deepseek", "openrouter"],
                index=3
            )
            
            model_options = {
                "openai": ["Padrão", "gpt-4o","gpt-4o-mini","o1-mini","o3-mini"],
                "anthropic": ["Padrão", "claude-3-5-haiku-latest", "claude-3-5-sonnet-latest"],
                "deepseek": ["Padrão", "deepseek-chat"],
                "openrouter": ["Padrão",
                               "openai/o3-mini-high",
                                "openai/o3-mini",
                                "openai/chatgpt-4o-latest",
                                "openai/gpt-4o-mini",
                                "google/gemini-2.0-flash-001",
                                "google/gemini-2.0-flash-thinking-exp:free",
                                "google/gemini-2.0-flash-lite-preview-02-05:free",
                                "google/gemini-2.0-pro-exp-02-05:free",
                                "deepseek/deepseek-r1-distill-llama-70b:free",
                                "deepseek/deepseek-r1-distill-qwen-32b",
                                "deepseek/deepseek-r1:free",
                                "qwen/qwen-plus",
                                "qwen/qwen-max",
                                "qwen/qwen-turbo",    
                                "mistralai/codestral-2501",
                                "anthropic/claude-3.5-haiku-20241022:beta",
                                "anthropic/claude-3.5-sonnet"
                                ]
            }
            
            model = st.selectbox(
                "Modelo",
                options=model_options.get(provider, ["Padrão"]),
                index=0
            )
            
            with st.expander("Configurações Avançadas"):
                trace = st.checkbox("Exibir logs detalhados")
                timeout = st.slider(
                    "Timeout (segundos)",
                    min_value=10,
                    max_value=600,
                    value=120,
                    step=10
                )
                max_attempts = st.slider(
                    "Máximo de Tentativas",
                    min_value=1,
                    max_value=20,
                    value=5,
                    step=1
                )

        # Área principal de geração
        container = st.container()
        with container:
            st.markdown("### O que você quer criar?")
            prompt = st.text_area(
                "",
                placeholder="Descreva o código que você precisa...",
                key="prompt_input",
                height=150
            )
            
            if st.button("Gerar Código", use_container_width=True):
                if not prompt:
                    st.error("Por favor, descreva o código que você precisa gerar.")
                else:
                    with st.spinner("Gerando seu código..."):
                        generated_code = None
                        error_msg = None
                        
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
                        except Exception as e:
                            error_msg = str(e)
                            st.error(f"Erro durante a geração: {error_msg}")
                            st.write("Buscando código no arquivo de fallback...")
                            
                            fallback_code = get_latest_failure_code()
                            if fallback_code:
                                generated_code = fallback_code
                                st.warning("⚠️ Usando código recuperado do arquivo de fallback")
                            else:
                                st.warning("Não foi possível recuperar código do arquivo de fallback")
                        
                        if generated_code:
                            if error_msg:
                                st.error("⚠️ Código gerado com falha. Código de fallback utilizado:")
                            else:
                                st.success("✨ Código gerado...")
                            st.code(generated_code, language=language)
                            
                            # Salvar o código gerado na sessão para uso na aba de execução
                            st.session_state.last_generated_code = generated_code
                            st.session_state.last_language = language
                        else:
                            st.error("Não foi possível gerar o código. Verifique os logs acima para mais detalhes.")
    
    with tab_executar:
        st.markdown("### Executar Código")
        
        # Opção para usar o último código gerado
        if 'last_generated_code' in st.session_state:
            if st.checkbox("Usar último código gerado"):
                code_to_execute = st.session_state.last_generated_code
                selected_language = st.session_state.last_language
            else:
                selected_language = st.selectbox(
                    "Linguagem",
                    options=["python", "r", "julia", "cpp"],
                    index=0
                )
                code_to_execute = st.text_area(
                    "Digite ou cole o código para executar",
                    height=200
                )
        else:
            selected_language = st.selectbox(
                "Linguagem",
                options=["python", "r", "julia", "cpp"],
                index=0
            )
            code_to_execute = st.text_area(
                "Digite ou cole o código para executar",
                height=200
            )

        if st.button("Executar", use_container_width=True):
            if code_to_execute:
                with st.spinner("Executando..."):
                    output, error = st.session_state.executor.execute_code(
                        code_to_execute, 
                        selected_language
                    )
                    
                    if output:
                        st.success("Execução concluída!")
                        st.code(output, language=selected_language)
                        
                    if error:
                        st.error("Erros durante a execução:")
                        st.code(error, language=selected_language)
            else:
                st.warning("Por favor, digite ou cole algum código para executar.")

if __name__ == "__main__":
    main()

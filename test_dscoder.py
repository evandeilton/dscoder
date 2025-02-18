from dscoder import dscoder
import unittest
from unittest.mock import patch, MagicMock
from dscoder import dscoder, AIAgent, LLMClient, ErrorHandler, MetricsCollector, LLMResponse

code = dscoder(
    description="""
    Develop an R script that:
    1. Performs comprehensive statistical analysis
    2. Implements hypothesis testing
    3. Generates visualization using ggplot2
    4. Calculates effect sizes and power
    5. Exports results to a report
    6. Use palmerpenguins data as example
    7. Check missing packages. If any is missing, please install.
    """,
    language="r",
    provider="openai",
    model="gpt-4o-mini"
)


print(code)

class TestDSCoder(unittest.TestCase):

    @patch('dscoder.LLMClient')
    def test_dscoder_success(self, MockLLMClient):
        mock_client = MockLLMClient.return_value
        mock_response = LLMResponse(
            content="```r\nprint('Hello, world!')\n```",
            tokens_used=10,
            model="gpt-4",
            provider="openai"
        )
        mock_client.generate_completion.return_value = mock_response

        code = dscoder(
            description="Print 'Hello, world!' in R",
            language="r",
            provider="openai",
            model="gpt-4"
        )

        self.assertIn("print('Hello, world!')", code)

    @patch('dscoder.LLMClient')
    def test_dscoder_failure(self, MockLLMClient):
        mock_client = MockLLMClient.return_value
        mock_client.generate_completion.side_effect = Exception("API error")

        with self.assertRaises(RuntimeError):
            dscoder(
                description="Print 'Hello, world!' in R",
                language="r",
                provider="openai",
                model="gpt-4"
            )

    def test_error_handler(self):
        handler = ErrorHandler()
        error_message = handler.handle_error(ValueError("Test error"), "Test context")
        self.assertEqual(error_message, "Test context: ValueError: Test error")

    def test_metrics_collector(self):
        collector = MetricsCollector()
        collector.update_metrics(100, True)
        collector.update_metrics(50, False, "Test error")

        self.assertEqual(collector.total_tokens, 150)
        self.assertEqual(collector.successful_generations, 1)
        self.assertEqual(collector.failed_generations, 1)
        self.assertEqual(len(collector.errors), 1)
        self.assertEqual(collector.errors[0], "Test error")

    @patch('dscoder.LLMClient')
    def test_ai_agent_generate_code(self, MockLLMClient):
        mock_client = MockLLMClient.return_value
        mock_response = LLMResponse(
            content="```r\nprint('Hello, world!')\n```",
            tokens_used=10,
            model="gpt-4",
            provider="openai"
        )
        mock_client.generate_completion.return_value = mock_response

        agent = AIAgent(provider="openai", trace=False)
        code = agent.generate_code(
            description="Print 'Hello, world!' in R",
            language="r"
        )

        self.assertIn("print('Hello, world!')", code)

    @patch('dscoder.LLMClient')
    def test_ai_agent_generate_code_failure(self, MockLLMClient):
        mock_client = MockLLMClient.return_value
        mock_client.generate_completion.side_effect = Exception("API error")

        agent = AIAgent(provider="openai", trace=False)
        code = agent.generate_code(
            description="Print 'Hello, world!' in R",
            language="r"
        )

        self.assertIsNone(code)

if __name__ == '__main__':
    unittest.main()

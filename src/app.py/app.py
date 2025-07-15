import gradio as gr

# Import your RAG pipeline function from Task 3
# For example:
from task3_rag_pipeline import answer_question_with_sources

def chat_interface(user_question):
    answer, sources = answer_question_with_sources(user_question)
    # sources can be a list of text chunks
    sources_display = "\n\n---\n\n".join(sources)
    return answer, sources_display

with gr.Blocks() as demo:
    gr.Markdown("# Customer Complaint Chatbot")
    user_input = gr.Textbox(label="Ask a question about complaints:")
    output_answer = gr.Textbox(label="Answer")
    output_sources = gr.Textbox(label="Sources")

    submit_btn = gr.Button("Ask")
    clear_btn = gr.Button("Clear")

    submit_btn.click(chat_interface, inputs=user_input, outputs=[output_answer, output_sources])
    clear_btn.click(lambda: ("", ""), inputs=None, outputs=[user_input, output_answer])

demo.launch()

import gradio as gr
import os
from main import solve_quiz_task

def solve_endpoint(email, secret, url):
    """Gradio interface for the quiz solver"""
    try:
        # Validate credentials
        if email != os.getenv("EMAIL") or secret != os.getenv("SECRET"):
            return {"error": "Invalid credentials", "status": 403}
        
        # Start the quiz solving process
        solve_quiz_task(email, secret, url)
        return {"status": "ok", "message": "Quiz solving started"}
    
    except Exception as e:
        return {"error": str(e), "status": 500}

# Create Gradio interface
iface = gr.Interface(
    fn=solve_endpoint,
    inputs=[
        gr.Textbox(label="Email"),
        gr.Textbox(label="Secret", type="password"),
        gr.Textbox(label="Quiz URL")
    ],
    outputs=gr.JSON(label="Response"),
    title="LLM Analysis Quiz Solver",
    description="Submit quiz tasks for autonomous solving"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
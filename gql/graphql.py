import requests

def enviar_diagnostico_a_backend(json_data):
    query = """
    mutation CrearDiagnostico($input: DiagnosticoInput!) {
      crearDiagnostico(input: $input) {
        id
        diagnostico
        pacienteId
      }
    }
    """
    variables = {"input": json_data}
    response = requests.post(
        "http://localhost:4000/graphql",
        json={"query": query, "variables": variables},
        headers={"Authorization": "Bearer tu_token_aqui"}
    )
    return response.json()

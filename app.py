import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from voice.transcriptor import transcribir_audio
from symtoms.extractor import extraer_datos

@strawberry.type
class Diagnostico:
    sintomas: str
    diagnostico: str
    tratamiento: str

@strawberry.type
class Query:
    # Se requiere al menos un campo para que sea válido
    @strawberry.field
    def ping(self) -> str:
        return "pong"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def procesar_audio(self, path: str) -> Diagnostico:
        texto = transcribir_audio(path)
        datos = extraer_datos(texto)
        return Diagnostico(**datos)

# Aquí se incluye `query=Query` para cumplir con Strawberry
schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")

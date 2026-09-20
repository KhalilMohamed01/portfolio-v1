interface AskResponse {
  question: string
  answer: string
}

const API_URL = import.meta.env.VITE_API_URL

export const askQuestion = async (question: string): Promise<AskResponse> => {
  const response = await fetch(
    `${API_URL}/api/ask?q=${encodeURIComponent(question)}`,
  )

  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`)
  }

  return response.json() as Promise<AskResponse>
}

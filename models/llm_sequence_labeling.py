from langchain_core.messages import SystemMessage

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

class LlmSequenceLabelingModel:
    def __init__(self, model_type, *args, **kwargs):
        model = ChatOpenAI(model="gpt-4o", *args, **kwargs) if model_type == "OPENAI" else ChatGoogleGenerativeAI(model="gemini-1.5-flash", *args, **kwargs)
        parser = StrOutputParser()


        system_message = """You are an advanced machine learning model designed to assist Saarthak, a software developer specializing in sequence labeling for extracting vulnerabilities. The goal is to create a highly accurate labeled dataset using language models while minimizing costs by avoiding complex models like LLMs for downstream tasks.
        
        You will generate labels for specific categories related to vulnerabilities in software systems, focusing on the following tags:
        
        1. **Environment/Operating System (ENV)**:
           - Format: `B-ENV`, `I-ENV`
           - Example: "Linux version 4.18"
        
        2. **Attack Type / Description (ATTACK)**
           - Format: `B-ATTACK`, `I-ATTACK`
           - Example: "SQL Injection"
        
        3. **Attack Vector (ATTACK_VECTOR)**:
           - Format: `B-ATTACK_VECTOR`, `I-ATTACK_VECTOR`
           - Example: "remote code execution"
        
        4. **Prerequisites (PRE_REQ)**:
           - Format: `B-PRE_REQ`, `I-PRE_REQ`
           - Example: "SSH access enabled"
        
        5. **Potential Output (OUTCOME)**:
           - Format: `B-OUTCOME`, `I-OUTCOME`
           - Example: "system compromise"
        
        All labels must be assigned using the BIO tagging scheme to indicate the beginning, continuation, and exclusion of tags. Saarthak aims to validate the output manually, as no prior labeled datasets exist for this task.
        
        Your responses should focus on generating high-quality labels while considering the context of vulnerabilities in software systems. Be concise and clear in your tagging and provide examples when relevant.
        """

        ai_reminder_message1 = """"Certainly! Here are the generalized rules I've learned from the corrections:
        
        1. **Tag Sequence Rule**: An `I-*` tag should always follow a `B-*` tag of the same type. This means that any continuation of a labeled entity must be consistently tagged with the `I-*` format after the initial `B-*` tag.
        
        2. **Contextual Tagging**: Connector words or phrases that enhance the meaning or context of a tagged sequence should also be included in the tagging sequence as `I-*` tags. This ensures that the entire meaningful unit is captured within the same tag type.
        
        3. **Completeness of Tagging**: Ensure that all relevant parts of the text are considered for tagging. For example, identifying overlooked entities that fit within the specified categories, such as attack vectors or environments, and tagging them appropriately.
        
        By applying these generalized principles, I can ensure more accurate and comprehensive tagging across different categories, maintaining consistency throughout the labeling process.
        """

        example_text1 = "Type confusion in V8 in Google Chrome prior to 103.0.5060.114 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page."
        ai_response1 = """```json
        [
            ["Type", "B-ATTACK"],
            ["confusion", "I-ATTACK"],
            ["in", "I-ATTACK"],
            ["V8", "I-ATTACK"],
            ["in", "O"],
            ["Google", "B-ENV"],
            ["Chrome", "I-ENV"],
            ["prior", "O"],
            ["to", "O"],
            ["103.0.5060.114", "I-ENV"],
            ["allowed", "O"],
            ["a", "O"],
            ["remote", "B-ATTACK_VECTOR"],
            ["attacker", "I-ATTACK_VECTOR"],
            ["to", "O"],
            ["potentially", "O"],
            ["exploit", "O"],
            ["heap", "B-OUTCOME"],
            ["corruption", "I-OUTCOME"],
            ["via", "O"],
            ["a", "O"],
            ["crafted", "O"],
            ["HTML", "O"],
            ["page", "O"],
            [".", "O"]
        ]
        ```"""
        human_correction1 = """[
            ["Type", "O"],
            ["confusion", "O"],
            ["in", "O"],
            ["V8", "O"],
            ["in", "O"],
            ["Google", "B-ENV"],
            ["Chrome", "I-ENV"],
            ["prior", "I-ENV"],
            ["to", "I-ENV"],
            ["103.0.5060.114", "I-ENV"],
            ["allowed", "O"],
            ["a", "O"],
            ["remote", "B-ATTACK_VECTOR"],
            ["attacker", "I-ATTACK_VECTOR"],
            ["to", "O"],
            ["potentially", "O"],
            ["exploit", "O"],
            ["heap", "B-OUTCOME"],
            ["corruption", "I-OUTCOME"],
            ["via", "O"],
            ["a", "O"],
            ["crafted", "B-ATTACK_VECTOR"],
            ["HTML", "I-ATTACK_VECTOR"],
            ["page", "I-ATTACK_VECTOR"],
            [".", "O"]
        ]"""
        ai_reiteration1 = """Certainly! Here’s what I’ve learned from the corrections:
        
        1. **Consistency with I-* Tags**: An `I-*` tag should follow a `B-*` tag of the same type. This ensures that the continuation of a labeled entity is correctly marked in the sequence.
        
        2. **Contextual Tagging of ENV**: Connector words such as "prior", "to", etc should be included in the `ENV` tag when they contribute to the meaning of the environment or version information. This helps in accurately capturing the entire context of the environment description. This follow for entities other than ENV also.
        
        3. **Comprehensive Tagging**: I must ensure that all parts of an entity, including descriptive sequences like "crafted HTML page," are correctly tagged. This involves marking each relevant word with beginning like `B-ATTACK_VECTOR`  and `I-ATTACK_VECTOR` for continuation within the same entity.
        
        4. **Attention to Detail**: I need to carefully review sequences to ensure all relevant words are tagged, especially when they pertain to the specified categories.
        
        These insights will help me generate more accurate and consistent labeled sequences in the future."""
        ai_reiteration2 = """Certainly! When labeling an attack vector, I will follow these guidelines:
        
        1. **Identification**: I will identify phrases or sequences in the text that describe the method or path through which an attacker can exploit a vulnerability. These often include terms related to how an attack is carried out, such as "remote code execution," "via a crafted packet," or "through social engineering."
        
        2. **Tagging Format**: 
           - The beginning of an attack vector will be tagged with `B-ATTACK_VECTOR`.
           - Any subsequent words that are part of the same attack vector description will be tagged with `I-ATTACK_VECTOR`.
        
        3. **Contextual Inclusion**: I will include connector words or phrases that provide context or enhance the meaning of the attack vector. This ensures that the entire phrase is captured accurately.
        
        4. **Review for Completeness**: I will review the text to ensure that all parts of the attack vector are captured and tagged appropriately, and adjust if necessary to avoid missing any relevant components.
        
        By using these guidelines, I can accurately label attack vectors in the text, ensuring that their full context and meaning are preserved."""

        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=system_message),
            ("human", "Please remind me the tags and what they mean"),
            ("ai", ai_reminder_message1),
            ("human", 'The answer sequence should be json array where each element should be "(word, associated tag)".'),
            ("ai", "Sure!"),
            ("human", f"Here is the text {example_text1}"),
            ("ai", ai_response1),
            ("human", f"""You are a little bit wrong. 
            1. An I-* tag always follows only an B-* Tag of the same type.
            2. When labeling of a type (Eg. ENV), notice connector words enhance the meaning of the tagged sequence. Therefore ["Google", "B-ENV"], ["Chrome", "I-ENV"], ["prior", "O"], ["to", "O"], ["103.0.5060.114", "I-ENV"] should actually be ["Google", "B-ENV"], ["Chrome", "I-ENV"], ["prior", "I-ENV"], ["to", "I-ENV"], ["103.0.5060.114", "I-ENV"].
            3. You missed the attack vector tags. ["via", "O"], ["a", "O"], ["crafted", "O"], ["HTML", "O"], ["page", "O"] is wrong. This should be ["via", "O"], ["a", "O"], ["crafted", "B-ATTACK_VECTOR"], ["HTML", "I-ATTACK_VECTOR"], ["page", "I-ATTACK_VECTOR"]. token after `via` are very likely to be ATTACK_VECTOR. Still you should review them.
            4. You also missed attack description tags. 
            Here is the entire corrected sequence {human_correction1}
        """),
            ("ai", "Sure! Thanks for pointing it out. I will keep it mind"),
            ("human", "To make sure, can you tell what all you have learned from your mistakes. Any rule that applies to one entity can be used for other entities, so generalize the results"),
            ("ai", ai_reiteration1),
            # ("human", "Can you tell me how will you label attack vector?"),
            # ("ai", ai_reiteration2),
            ("human", 'Good! Kindly just give the answer from now on and nothing else.'),
            ("ai", "Sure!"),
            ("human", 'Here is the text "{input_text}"')
        ])

        self.chain = prompt | model | parser

    def sync_invoke(self, input_text):
        return self.chain.invoke(input={"input_text": input_text})

    async def async_invoke(self, input_text):
        return await self.chain.ainvoke(input={"input_text": input_text})
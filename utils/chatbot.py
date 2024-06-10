import code1
while True: 
    question = input("Nhập câu hỏi: ")
    context = code1.context
    model = code1.model
    tokenizer = code1.tokenizer
    context1 = code1.get_context(context, question)
    
    answer = code1.answer_question(context1, question, model, tokenizer)
    print(f"Câu trả lời: {answer}")

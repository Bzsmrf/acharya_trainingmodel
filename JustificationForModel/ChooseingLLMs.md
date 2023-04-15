### Comparison Of Different LLMs

### Introduction
This report will justify my choice of a language model for Text Summarization. After conducting research on several available models, I have chosen chat-gpt 3.5 turbo for the following reasons:
### Leading LLMs 
According to Data + Ai Summit 2022 by Databricks a leading contributor in the field of Data Science and creator of Apache Spark. There are a lot of LLMs the leading LLMs on the Glue score benchmark are 
![](https://github.com/Bzsmrf/Summerize/blob/master/JustificationForModel/fig1.png) 
Now, Recently in 2023, the leading LLMs are from the article published on dataconomy.com  “The role of LLMs in Ai war” is
 
Here the benchmark was on the Size of parameters and Training Tokens
We can see that Chat-gpt3 and LaMDA models like(BERT, and BARD) are the leading ones based on GLUE score.
![](https://github.com/Bzsmrf/Summerize/blob/master/JustificationForModel/fig%202.png)
### Comparison of Language Models
Open Ai models
Chat-gpt
Accessibility-API available
Cost-freemium with monthly compute limitations 
Chat-gpt 3
Accessibility-API available 
Cost-freemium with monthly compute limitations 
LaMDA models
BARD 
Accessibility-API is available but the long waitlist
Cost-freemium with monthly compute limitations 
Google/Flan models
Flan-t5 11B model
Accessibility-API available 
Cost-freemium with monthly compute limitations 



Now take these models and let them perform some tasks and rate them on a scale of 1-8:
### Performance Comparison
### Task1- Testing1 General Knowledge base 
Input:
what is sustainability and environment?

Output:

Chatgpt3

Params: {'model_name': 'gpt-3.5-turbo', 'temperature': 0.1, 'max_tokens': 256}
Sustainability refers to the ability to maintain or preserve something over time. In the context of the environment, sustainability refers to the ability to maintain the natural resources and ecosystems that support life on Earth for future generations. This includes reducing waste and pollution, conserving resources, and promoting renewable energy sources. The environment refers to the natural world around us, including the air, water, land, and living organisms. It is the foundation of all life on Earth and is essential for human health and well-being. Protecting and preserving the environment is crucial for ensuring a sustainable future for ourselves and future generations.

chatgpt

Params: {'model_name': 'text-davinci-003', 'temperature': 0.1, 'max_tokens': 256, 'top_p': 1, 'frequency_penalty': 0, 'presence_penalty': 0, 'n': 1, 'best_of': 1, 'request_timeout': None, 'logit_bias': {}}
 Sustainability is the practice of using resources in a way that meets the needs of the present without compromising the ability of future generations to meet their own needs. This includes preserving natural resources, reducing pollution, and promoting economic growth. The environment is the natural world and all the living and non-living things in it, including air, water, land, plants, and animals. It is the sum of all the conditions and influences that affect an organism or an ecological community.

Flan-t5 11B

Params: {'repo_id': 'google/flan-t5-xxl', 'task': None, 'model_kwargs': {'temperature': 0.1, 'max_new_tokens': 200}}
Sustainability is the ability of an organism or system to continue to exist indefinitely in the face of a changing environment. The environment is the natural world in which organisms live. Sustainability is the ability of an organism or system to continue to exist in the face of a changing environment.

Score: ChatGPT3 -6
       ChatGPT  -5
       Flan-T5  -4

### Task2- Testing2 General Knowledge base 
Input:
Answer the following question by reasoning step by step. Can you provide some practical ways that individuals and communities can help protect the environment? Please list at least five actionable steps that can be taken to reduce waste, conserve resources, and promote sustainability. These suggestions should be easy to implement and effective in making a positive impact on the environment  

Output:

Chatgpt3

Params: {'model_name': 'gpt-3.5-turbo', 'temperature': 0.1, 'max_tokens': 256}
Step 1: Identify areas where waste can be reduced. One practical way to reduce waste is to use reusable bags, water bottles, and containers instead of disposable ones. This can significantly reduce the amount of plastic waste that ends up in landfills and oceans.

Step 2: Conserve resources by using energy-efficient appliances and light bulbs. This can help reduce energy consumption and lower utility bills. Additionally, turning off lights and electronics when not in use can also help conserve energy.

Step 3: Promote sustainability by supporting local farmers and businesses that use sustainable practices. This can help reduce the carbon footprint associated with transportation and support the local economy.

Step 4: Reduce food waste by planning meals and only buying what is needed. This can help reduce the amount of food that ends up in landfills and save money on groceries.

Step 5: Plant trees and support reforestation efforts. Trees absorb carbon dioxide and help clean the air, making them an important part of the ecosystem. Planting trees in urban areas can also help reduce the urban heat island effect and provide shade. 

Overall, these five actionable steps can be easily implemented by individuals and communities to help protect the environment. By reducing waste, conserving resources, and promoting sustainability, we can all make a




Chatgpt

Params: {'model_name': 'text-davinci-003', 'temperature': 0.1, 'max_tokens': 256, 'top_p': 1, 'frequency_penalty': 0, 'presence_penalty': 0, 'n': 1, 'best_of': 1, 'request_timeout': None, 'logit_bias': {}}
 

1. Reduce, Reuse, Recycle: This is the most basic and effective way to reduce waste and conserve resources. Reduce the amount of waste you produce by buying only what you need, and reuse items whenever possible. When you can't reuse something, recycle it instead of throwing it away. 

2. Conserve Energy: Turn off lights and electronics when not in use, and switch to energy-efficient light bulbs. Unplug appliances when not in use, and use natural light whenever possible. 

3. Conserve Water: Take shorter showers, turn off the tap when brushing your teeth, and use a bucket to collect water for gardening. 

4. Eat Sustainable Foods: Buy locally-sourced food whenever possible, and reduce your consumption of meat and dairy products. 

5. Use Sustainable Transportation: Walk, bike, or take public transportation whenever possible. If you must drive, carpool with friends or family.

Flan-t5 11B

Params: {'repo_id': 'google/flan-t5-xxl', 'task': None, 'model_kwargs': {'temperature': 0.1, 'max_new_tokens': 200}}
Individuals can reduce waste by reducing the amount of paper they use. Communities can reduce waste by reducing the amount of water they use. Individuals can promote sustainability by promoting the use of renewable resources.
Score: ChatGPT3 -7
       ChatGPT  -5
       Flan-T5  -3





### Task3-Fact Extraction
Input:
Please answer the question:

What is sustainable development?


"Sustainable development is development that meets the needs of the present, without compromising the ability of future generations to meet their own needs."
The concept of sustainable development can be interpreted in many different ways, but at its core is an approach to development that looks to balance different, and often competing, needs against an awareness of the environmental, social and economic limitations we face as a society.

All too often, development is driven by one particular need, without fully considering the wider or future impacts. We are already seeing the damage this kind of approach can cause, from large-scale financial crises caused by irresponsible banking, to changes in global climate resulting from our dependence on fossil fuel-based energy sources. The longer we pursue unsustainable development, the more frequent and severe its consequences are likely to become, which is why we need to take action now.  

So is it all just about the environment?
Living within our environmental limits is one of the central principles of sustainable development. One implication of not doing so is climate change.

But the focus of sustainable development is far broader than just the environment. It's also about ensuring a strong, healthy and just society. This means meeting the diverse needs of all people in existing and future communities, promoting personal wellbeing, social cohesion and inclusion, and creating equal opportunity.


Output:

Chatgpt3

Params: {'model_name': 'gpt-3.5-turbo', 'temperature': 0.1, 'max_tokens': 256}
Sustainable development is an approach to development that balances different needs against an awareness of the environmental, social, and economic limitations we face as a society. It aims to meet the needs of the present without compromising the ability of future generations to meet their own needs. It is not just about the environment, but also about ensuring a strong, healthy, and just society by meeting the diverse needs of all people, promoting personal wellbeing, social cohesion and inclusion, and creating equal opportunity.

Chatgpt

Params: {'model_name': 'text-davinci-003', 'temperature': 0.1, 'max_tokens': 256, 'top_p': 1, 'frequency_penalty': 0, 'presence_penalty': 0, 'n': 1, 'best_of': 1, 'request_timeout': None, 'logit_bias': {}}
 Sustainable development is an approach to development that looks to balance different, and often competing, needs against an awareness of the environmental, social and economic limitations we face as a society. It is focused on ensuring a strong, healthy and just society by meeting the diverse needs of all people in existing and future communities, promoting personal wellbeing, social cohesion and inclusion, and creating equal opportunity, while living within our environmental limits.

Flan-t5 11B

Params: {'repo_id': 'google/flan-t5-xxl', 'task': None, 'model_kwargs': {'temperature': 0.1, 'max_new_tokens': 200}}
development that meets the needs of the present, without compromising the ability of future generations to meet their own needs

Score: ChatGPT3 -6
       ChatGPT  -4
       Flan-T5  -2

Now taking the mean of the results of the test
 Final Score: ChatGPT3 -6.3
              ChatGPT  -4.6
              Flan-T5  -3

### Justification for Choice
Based on the brief test ChatGpt3 has a clear advantage over the other LLMs 
•	It is easily accessible
•	It is trained on large parameters
•	GLUE Score is at par or higher than other LLMs


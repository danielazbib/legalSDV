# SimpliSafe: Safe Summaries Made Simple

## Inspiration

We were inspired to create a tool that enhances data privacy by anonymizing sensitive information in legal documents while retaining semantic context, crucial for legal analysis without compromising confidentiality.

As the use of data for machine learning and training artificial intelligence has become ubiquitous across all kinds of fields, maintaining data privacy has risen to the forefront of many people’s internet safety concerns. Although data is essential for these functions, we wanted to think of how we could strip the information we needed from data while separating the non-essential personal information that may be associated with it. By extension,**this would clean up data and mitigate any data contamination or memorization issues when training AI models.**

## What it does

SimpliSafe produces standardized model-ready datasets, stripped of private information, that machine learning engineers can easily input into LLMs to mitigate data contamination and memorization. This can be applied to any field that utilizes private information, like the legal, medical, and financial fields. We test the use case of the legal field by running descriptions of legal contracts from the [Contract Understanding Atticus Dataset (CUAD)](https://github.com/neelguha/legal-ml-datasets) through the service and producing a summary that strips away personal information, replacing it with relevant synthetic data using Python’s synthetic data vault (SDV) library. In addition, we can ensure our output comes out in a standard format. **This standardized form will be easily recognizable for the technology ML engineers may be training on so that it is properly trained on that data rather than simply memorizing it and can easily find the relevant data it needs to perform its function without data contamination.**

## How we built it

We used the SDV library to identify private keywords and replace them with synthesized words. We used scikit-learn to perform a **semantic similarity analysis** to assess if the synthesized descriptions maintained the meaning of the original descriptions. We used Flask as a backend to provide information to the frontend. We used React for a dynamic frontend, and integrated Matplotlib to display semantic similarity scores through interactive visuals.

## Challenges we ran into

We encountered integration challenges with data processing and achieving accurate similarity scores while preserving essential context.

## Accomplishments that we're proud of

We’re proud of creating a seamless and accessible interface that makes privacy protection simple, alongside a reliable backend that supports real-time data analysis.

## What we learned

We learned the importance of fine-tuning data anonymization to balance security and context, especially in legal fields where accuracy is essential.

## What's next for SimpliSafe

Next, we plan to expand SimpliSafe’s capabilities to other domains, such as healthcare and finance, and enhance its analysis accuracy through advanced natural language processing models.

We would also want this use case to serve as a stepping stone for future applications at organizations or companies internally, where they may have actual sensitive data that our program would be able to pick up and extract appropriately.

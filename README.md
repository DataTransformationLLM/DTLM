
# Data transformation using Large language models(DTLM)

## Description
DTLM is a Python library designed to simplify data transformation tasks in data science projects using the power of large language models. This library enables users, regardless of their coding expertise, to perform complex data transformations through a user-friendly interface. without coding.

## Features

- **Simple Data Transformation**: Utilize a straightforward widget to transform data. Users can select a column from their dataframe and provide either a descriptive transformation requirement or input-output pair examples. The transformation is applied based on this user-provided information.
- **User-Friendly Interface**: Designed with simplicity and flexibility in mind, making it accessible for users of all levels, from beginners to advanced.
- **Powered by Large Language Models**: Initially integrated with OpenAI's models, with plans to expand support for other large language models.

## License

[MIT](https://choosealicense.com/licenses/mit/)



## Usage/Examples
```python

from dtlm import simple_transformation
import openai
openai.api_key =API_kEY
# Assume df is your DataFrame
simple_transformation(df)
```

![image](https://github.com/DataTransformationLLM/DTLM/assets/165834205/80005467-6ea3-46f5-81c3-48c793dabbfd)

## Installation through guithub

```bash
 !pip install git+https://github.com/GhazzaiSkander/DTLM.git@dtlm#egg=dtlm
```
    
## Demo

Insert gif or link to demo


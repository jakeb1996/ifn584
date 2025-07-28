# Marking rubrics

Inspiration from `canvastools/canvas_rubric` tool: https://github.com/mckaguem/canvastools/tree/281561c7b1d494b21feda943593d0b77f8528cd8/canvas_rubric

## Deployment

To deploy the marking criteria,

1. Make sure you have a Canvas credential file in `$HOME/.canvas`, and contains:

```ini
[Credentials]
url=https://canvas.qut.edu.au/
access_token=21862~abc123
```

   or highjack the tool by modifying the source code to point directly at your credentials file (it is right at the end of the source).

1. Run the tool


Where 
- `21188` is the Canvas course number
- `192697` is the Canvas assignment number

Find those values in the URL of a Canvas assignment

   e.g, `https://canvas.qut.edu.au/courses/21188/assignments/192697`



```bash
# This command is useful for IFN666_25se1 Assessment 02
cd /mnt/c/git/ifn666/src
python3 assessments/deploy-rubric.py /mnt/c/git/ifn666/src/assessments/rubric-a02.yaml 21188 192697
```


```bash
# This command is useful for IFN666_25se1 Assessment 03
cd /mnt/c/git/ifn666/src
python3 assessments/deploy-rubric.py /mnt/c/git/ifn666/src/assessments/rubric-a03.yaml 21188 192710
```


```bash
# This command is useful for IFN666_25se1 Assessment 03 essay
cd /mnt/c/git/ifn666/src
python3 assessments/deploy-rubric.py /mnt/c/git/ifn666/src/assessments/rubric-a03-essay.yaml 21188 193803
```

from projen.python import PythonProject

project = PythonProject(
    author_email="nico@nicolas-byl.io",
    author_name="Nicolas Byl",
    module_name="taskman",
    name="taskman",
    version="0.1.0",
    deps=[
        'fastapi',
        'uvicorn[standard]'
    ]
)

dev_task = project.add_task('dev')
dev_task.exec('uvicorn taskman.main:app --reload')


project.synth()